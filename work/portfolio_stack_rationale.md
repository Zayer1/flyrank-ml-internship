# Stack Rationale: Portfolio Architecture

**Constraints:**
- Cost: $0 (Free tier only).
- Skill Level: Advanced (Systems/ML Engineer).
- Requirement: Must natively support raw code blocks, external GitHub links, and future integration of a live ML inference engine.
- Backend: Not required for V1 (static display).

## The Three Options Evaluated:

### 1. Simplest (No-Code GUI - Framer / Webflow)
- **Architecture:** Visual canvas builder. Hosted on proprietary free tiers. No backend.
- **Trade-off:** High velocity, but completely violates my positioning as an engineer who builds from the ground up. Integrating custom DOM elements or raw Python inference scripts requires fighting brittle iframe constraints.

### 2. Most Powerful (Next.js / React on Vercel)
- **Architecture:** Component-based SSR framework. Hosted on Vercel. Serverless backend available.
- **Trade-off:** Massive architectural overkill. Introduces Node dependency hell, build pipelines, and hydration overhead just to serve three sections of static text. High maintenance cost as framework versions deprecate.

### 3. Front-Runner (Vanilla HTML/CSS/JS on GitHub Pages)
- **Architecture:** Raw DOM manipulation. Hosted on GitHub Pages. No backend.
- **Trade-off:** Requires manual CSS layout structuring, but provides absolute flexibility and zero framework bloat.

## The Decision:
I chose **Vanilla HTML/CSS/JS on GitHub Pages**. 

I discarded the simplest option (Framer) because it undermines my technical credibility and restricts raw code integration. I discarded the most powerful option (Next.js) because introducing a complex dependency tree to serve a static portfolio is poor systems design.

Vanilla HTML/CSS gives me absolute control over the DOM to display my work exactly as intended. A backend is currently unnecessary, as this is a read-only presentation layer. 

**Regarding maintenance:** It is mathematically zero. Because there are zero external dependencies, package managers, or build steps involved, the codebase will not rot. It can sit untouched for five years and continue to execute perfectly.
