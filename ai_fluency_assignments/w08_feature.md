# Week 8 Deliverable: Make It Do Something

## The One Dynamic Feature

**Feature:** A live XGBoost decay-probability prediction form embedded in the capstone project detail page.

This is not a contact form — it is a working demo of the actual ML model. A visitor enters real page metrics, presses "Run Prediction," and the form queries my FastAPI backend, runs inference on the trained XGBoost model in memory, and returns the decay probability in under 2 seconds (on a warm server).

**Live evidence:** The form is working and reachable at `https://zayer1.github.io/flyrank-ml-internship`. A test submission with sample inputs returns a valid JSON response containing `decay_probability`.

---

## The Plain-Words Explainer

### What is a "backend"?

A static portfolio page — the HTML and CSS files served by GitHub Pages — is read-only. It can display text, show images, and run simple JavaScript animations, but it has no ability to perform complex calculations, load a trained ML model into memory, or store data. It is just a document.

A backend is a separate program running on a remote server that stays active, waiting for requests. It can do things the static page cannot: load a 15MB serialized XGBoost model, run NumPy matrix operations, and return predictions. My backend is a Python FastAPI application hosted on Render.

### How the feature works and where the data goes

When a visitor clicks "Run Prediction," this is the exact sequence of events:

1. **Browser collects input.** JavaScript in `app.js` reads the values from each form field and packages them into a JSON object: `{"word_count": 1200, "days_since_update": 180, "internal_links": 12, ...}`.

2. **Browser sends a POST request.** The `fetch()` function sends this JSON object over HTTPS to my Render server's `/predict` endpoint. The request includes an `X-API-Key` header for authentication.

3. **FastAPI authenticates the request.** The server checks the API key against its stored value. If it doesn't match, it immediately returns a `403 Forbidden` response and the prediction never runs.

4. **The model runs.** FastAPI passes the JSON values to a NumPy array, feeds it into the loaded XGBoost model's `predict_proba()` method, and receives a float between 0 and 1 representing the probability of traffic decay.

5. **Server responds.** The server wraps the probability in a JSON response: `{"decay_probability": 0.74, "risk_tier": "High"}` and sends it back.

6. **Browser displays the result.** The JavaScript updates the DOM with the risk tier and formatted percentage. If the request fails (timeout, 422 validation error), a user-facing error message is shown instead of a frozen screen.

The whole flow runs over HTTPS. No user data is stored anywhere — the server processes the request and discards the inputs immediately.
