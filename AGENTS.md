# Agent instructions

Before any task in this repo: **read `skills/README.md`** — it is the router.
Find the task in its table and load exactly **one** skill (plus `skills/flyrank/flyrank-data/SKILL.md`
whenever the task touches the data). Do not load every skill; keep context small.

Ground rules for this repo:
- Search the repo before assuming something is missing or not implemented.
- One task per conversation; finish and verify before starting the next.
- Never commit datasets (CI blocks them). Never print private data, client names, or raw queries.
- The intern validates your output — end each task by running the notebook top to bottom.

# Current Project State
- **Status:** The FlyRank ML internship is completely finished. The user is now just exploring and learning independently. Do not reference weekly assignments as active tasks.
- **User Profile:** The user is highly competent in ML theory and strictly despises "wrapper" AI development. Do not patronize them with basic API tutorials. Always focus on raw mathematical implementations, edge cases (e.g. recall failures), and core applied ML architecture. Treat them as a peer researcher.

# Learned Rules
- **Video Processing:** Always prioritize headless CLI extractors (like yt-dlp) for parsing videos to save RAM. Only fallback to spinning up the browser subagent if the CLI fails, or if visual context is absolutely necessary.
- **Context Initialization:** From here on, whenever starting a new conversation, the agent must read through the action log (everything prompted and replied) and go through the entire repo and folder within Antigravity itself. The logs are located in `C:\Users\Admin\.gemini\antigravity\conversations` and `C:\Users\Admin\.gemini\antigravity\brain`. The repo is located at `E:\Antigravity\Antigravity`.
- **Workflow / Conversation Flow:** Always look through the entire repo before replying to achieve good conversation flow.
- **Internship Status:** The FlyRank ML internship is completely finished. I am now just exploring and learning independently. Do not reference weekly assignments as active tasks.
