# Week 6 Deliverable: Explain Your Build

**The Mystery Code I Picked: CORS Middleware in FastAPI**

When I was deploying the V2 Zero-Shot Cascade, my Python FastAPI backend was working perfectly locally, but the moment I tried to connect it to my live GitHub Pages frontend, the browser threw a massive red error and blocked the request. 

I pasted the error to my AI, and it told me to add this block of code to `api/server.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://zayer1.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

It instantly fixed the problem, but it felt like pure magic. I didn't want to leave it as a mystery, so I had the AI tutor me on what this actually does.

**My Plain-Words Explanation:**

Think of web browsers as incredibly paranoid security guards. By default, if a website loaded from one domain (like my GitHub Pages frontend) tries to ask for data from a completely different domain (like my backend server), the browser immediately blocks it to prevent malicious scripts from stealing data. 

This security rule is called the "Same-Origin Policy." 

CORS (Cross-Origin Resource Sharing) is simply the backend server formally handing the browser's security guard a guest list. 

The code `allow_origins=["https://zayer1.github.io"]` is my server explicitly saying: *"Hey browser, it's okay, I recognize this specific GitHub Pages website. You can let their requests through."* 

Instead of just pasting it and moving on, I now understand that CORS isn't just an annoying error to bypass—it's a fundamental security layer that protects my API, and this middleware is how I explicitly grant my frontend permission to talk to my XGBoost model.
