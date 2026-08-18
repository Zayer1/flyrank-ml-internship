# Week 6 Deliverable: Explain Your Build

**The Mystery Code I Picked: CORS Middleware in FastAPI**

When I was deploying my XGBoost model's FastAPI backend on Render, the backend was working perfectly when tested with local scripts. However, the moment I tried to connect my live GitHub Pages frontend to it, the browser threw a massive red error in the console and blocked the connection. 

I gave the error to my AI assistant, and it told me to add this block of code to `api/server.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://zayer1.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Adding this middleware fixed the error instantly, but I didn't want to leave it as a mystery. I had the AI tutor me on what this block actually does.

**My Plain-Words Explanation:**

Think of web browsers as incredibly paranoid security guards. By default, if a website loaded from one domain (like my GitHub Pages frontend, `zayer1.github.io`) tries to request data from a completely different domain (like my backend server running on Render), the browser blocks it immediately. This is a security rule called the "Same-Origin Policy," which stops malicious scripts on random websites from stealing your data.

CORS (Cross-Origin Resource Sharing) is simply my backend server handing the browser's security guard a guest list. 

The code `allow_origins=["https://zayer1.github.io"]` is my server explicitly telling the browser: *"Hey, I know this specific website. It is mine, and I trust it. You are allowed to let its requests pass through to my XGBoost model."*

Now I understand that CORS isn't just an annoying error to bypass—it's a vital security layer that protects APIs, and this middleware is how I explicitly grant my static frontend permission to speak to my backend.
