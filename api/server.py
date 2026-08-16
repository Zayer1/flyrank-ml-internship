import os
import json
import logging
import traceback
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import xgboost as xgb
from dotenv import load_dotenv
import pandas as pd
import io

load_dotenv()

# Configure OpenAI client to route to Groq
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

app = FastAPI(title="FlyRank Triage API")

# Allow CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    context: str = ""

@app.post("/api/score")
async def score_data(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Must be a CSV file")
    
    contents = await file.read()
    try:
        df = pd.read_csv(io.BytesIO(contents))
        print("Columns in uploaded CSV:", df.columns.tolist())
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing CSV: {str(e)}")
    
    # Load the trained model globally if not already loaded
    try:
        global model
        if 'model' not in globals() or model is None:
            model = xgb.XGBClassifier(enable_categorical=True)
            model_path = os.path.join(os.path.dirname(__file__), 'xgb_model.json')
            model.load_model(model_path)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error loading model. Did you run the capstone notebook? Details: {str(e)}")
        
    # Preprocess incoming CSV (Identical to training pipeline)
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    DROP_FOR_TRAIN = config.get("DROP_FOR_TRAIN", [])
    cols_to_drop = [c for c in DROP_FOR_TRAIN if c in df.columns]
    X_score = df.drop(columns=cols_to_drop)

    cat_cols = X_score.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        X_score[col] = X_score[col].astype('category')

    # Execute actual ML inference
    try:
        # Re-order columns to match model strictly, checking for missing ones
        expected_cols = model.feature_names_in_
        missing = [c for c in expected_cols if c not in X_score.columns]
        if missing:
            raise HTTPException(status_code=400, detail=f"Uploaded CSV is missing required columns: {missing}")
            
        X_score = X_score[expected_cols]
        probs = model.predict_proba(X_score)[:, 1]
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

    results = []
    for index, prob in enumerate(probs):
        row = df.iloc[index]
        
        # Action Playbook Rules
        impressions = row.get('impressions_prev_30d', 0)
        search_volume = row.get('search_volume', 0)
        
        if impressions == 0:
            action = "Stable / No Action"
        elif prob > 0.7 and search_volume > 100:
            action = "Urgent Refresh"
        elif prob > 0.4:
            action = "Standard Review"
        else:
            action = "Stable / No Action"
            
        # Try to find a good ID column
        url_id = row.get("url_id", row.get("content_id", f"url_{index}"))
            
        results.append({
            "url_id": str(url_id),
            "decay_probability": float(prob),
            "action": action
        })
        
    return {"scored_pages": sorted(results, key=lambda x: x['decay_probability'], reverse=True)}

@app.post("/api/chat")
async def chat(req: ChatRequest):
    if not os.environ.get("GROQ_API_KEY"):
        raise HTTPException(status_code=500, detail="GROQ_API_KEY is not set in the environment.")
    if not client:
        raise HTTPException(status_code=500, detail="OpenAI API not configured.")

    system_prompt = f"""You are an intelligent SEO data assistant. You must answer the user's questions strictly based on the following JSON payload.

    CRITICAL RULES:
    1. The JSON contains a 'total_urls_in_dataset' field. If the user asks "how many URLs are there" or "how large is the dataset", you MUST reply with this exact number.
    2. The JSON contains a 'top_urls_preview' array. This is ONLY a preview of the top 50 URLs because the full dataset is too large. 
    3. DO NOT manually count the items in the preview array to determine the total size of the dataset.

    DATA CONTEXT:
    {req.context}
    """

    try:
        response = client.chat.completions.create(
            model='llama-3.1-8b-instant',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": req.message}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        print(f"ERROR OCCURRED: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Chat API Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
