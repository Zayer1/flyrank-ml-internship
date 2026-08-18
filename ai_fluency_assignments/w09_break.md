# Week 8+ Deliverable (Part 1): Break Your Own Site — Checkpoint 2

## Hardening Attempt Log

I systematically tried to break every part of the deployed system before the hardening review.

---

## What I Tried and What Happened

### Form: Empty Submission
**Action:** Clicked "Run Prediction" with all fields blank.  
**Result:** JavaScript's `fetch()` sent an empty JSON object `{}`. FastAPI's Pydantic schema raised a `422 Unprocessable Entity` and returned a JSON error body listing every missing field. The frontend showed nothing — the page just sat there.  
**Fix-Now:** Added client-side validation before the fetch that checks all required fields are non-empty and shows an inline error message if not. Also added a user-facing catch block to display `"Please check your inputs and try again."` on any non-200 response.

### Form: Garbage String Input
**Action:** Typed `"hello world"` into the `days_since_update` (numeric) field.  
**Result:** HTML `type="number"` input silently coerced `"hello world"` to an empty string before sending. FastAPI caught the type mismatch with a 422 error. Same invisible failure.  
**Fix-Now:** The client-side validation now explicitly checks that numeric fields contain valid numbers using `isNaN()` before allowing the request.

### Form: Double Submit (Spam)
**Action:** Double-clicked the "Run Prediction" button rapidly.  
**Result:** Two simultaneous POST requests fired. Render's free tier rate limit (`slowapi`: 100/hour) wasn't hit in testing, but on a real high-traffic day this could exhaust the allowance.  
**Fix-Now:** The button is now immediately disabled on first click and its text changes to `"Running..."` until the response (or error) returns.

### Demo Link: Clicked All External Links
**Action:** Clicked every link including the GitHub repo link, V2 proposal link, and the capstone demo link.  
**All passed.** All links resolve correctly to their targets.

### Old Browser: Firefox ESR
**Action:** Opened the portfolio in Firefox ESR (Extended Support Release — the oldest common browser in enterprise environments).  
**Result:** The `fetch()` API and CSS Grid both worked. The Google Fonts didn't load (privacy settings blocked the external font request), falling back to `system-ui`. The layout remained intact. Acceptable.

---

## Triage Summary

### Fix-Now (addressed before this submission):
1. Empty form submission — silent failure → now shows inline error
2. Garbage string input — silent failure → now shows validation warning
3. Double-click spam — duplicate requests → button now disables on first click

### Known Limitations (named, not hidden):
- **Render cold-start latency:** The first prediction request after 15 minutes of inactivity takes 30-50 seconds while the free instance wakes up. A warning message now appears in the UI: *"First prediction may take up to 60 seconds — the server is waking up."*
- **Firefox font fallback:** Google Fonts blocked by strict privacy settings causes font fallback to `system-ui`. Layout is unaffected but typography differs from Chrome.
- **No input history:** The form has no memory. If a visitor refreshes the page their inputs are cleared. This is acceptable for a demo tool.

---

## Hardening Review Outcome

Submitted the above triage log to a peer reviewer. Their verdict: the fix-nows are resolved, the known limitations are named honestly, and the cold-start warning in the UI correctly sets expectations. Checkpoint 2 passed.
