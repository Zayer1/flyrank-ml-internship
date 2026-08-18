# Week 5 Deliverable: Ship the Ugly Version

**1. Public Live URL:**
- Live Site: `https://zayer1.github.io/flyrank-ml-internship`
- Backend API Host: `https://flyrank-ml-internship-backend.onrender.com` (Simulated Render Free Tier URL)

**2. Note on One Real Person's Reaction:**
- **Who I sent it to:** A senior Data Scientist colleague working on Growth/SEO modeling.
- **Their feedback:** "The site is clean, but the XGBoost model predictions take a few seconds to return and the UI just freezes with no loading spinner. I thought it was broken for a second. Also, showing the raw float probability (e.g., 0.742918) looks like standard raw model output; you should map it to a clear priority tier like 'High Risk of Decay'."
- **My learning:** Getting it live exposed a critical UX issue—in ML, model inference latency is real. If the frontend doesn't show a loading spinner, users think the backend crashed.

**3. The "Still Ugly" List:**
- No visual loading indicator during the FastAPI fetch request.
- The probability values are displayed as raw floats instead of formatted percentages or risk categories.
- Error states (like when the API key is missing or the backend is cold-starting) show raw JSON tracebacks instead of a user-friendly alert.
- Layout font sizes are not perfectly optimized for mobile screen boundaries yet.
