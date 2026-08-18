# Week 7 Deliverable: Make It Real (Checkpoint 1)

## 1. Mobile & Readability Fix Log

I audited my portfolio site on a physical mobile device and ran a PageSpeed check to clean up the user experience.

| What Was Broken / Heavy | Why It Mattered | What I Changed |
| :--- | :--- | :--- |
| **XGBoost Feature Importances chart spilling offscreen** | The high-resolution PNG chart had a fixed width of 800px, which pushed the screen out of bounds on mobile screens. | Replaced the raw PNG with a responsive CSS grid element and set `max-width: 100%; height: auto` on all figures. |
| **Model input form buttons too small** | The "Run Inference" button was hard to tap on a mobile device (violating touchscreen size target guidelines). | Increased the button padding to `14px 28px` to ensure a touch target of at least 48x48px. |
| **Contrast on math formulas** | The LaTeX formula blocks used a light-gray color on a dark-slate background, failing the WCAG AA accessibility check. | Updated the LaTeX text color to a crisp off-white (`#f8fafc`) to ensure strong contrast. |
| **Uncompressed metric plots** | The model's Precision-Recall curve was 4MB, severely dragging down page speed on 3G mobile networks. | Compressed the image using WebP formatting, reducing the file size from 4MB to 110KB without losing readability of the curve labels. |

---

## 2. Design Review (Crit) Sort

I submitted the portfolio to a peer reviewer alongside my Week 1 proof statement (*"I will prove I can train and deploy a production-grade XGBoost classifier to predict SEO growth/decay with a Precision@50 that beats the baseline"*).

### Must-Fix (Blocked Understanding or Trust):
1. **Unclear input fields:** The peer reviewer did not know what values to enter into the feature input boxes (like "internal_link_count") to run a mock inference.
2. **Missing baseline comparison:** The reviewer could see my XGBoost metrics, but they had no idea if they were actually "good" because I didn't visually contrast them with the Week 4 heuristic baseline.

### Nice-to-Have (Optional / Polish):
1. **No dark mode toggle:** The reviewer suggested adding a toggle for dark/light mode. (Nice to have, but doesn't impact the proof statement).
2. **Dynamic chart animation:** The reviewer thought animating the features bar chart would look slick. (Pure visual fluff).

---

## 3. Evidence of Must-Fixes Solved
- **Input Field Guidance:** Added placeholder text to every form input showing realistic default bounds (e.g., `Default: 12 (Min: 0, Max: 100)`).
- **Baseline Comparison Table:** Added a prominent, high-contrast side-by-side table comparing the XGBoost model's Precision@50 and Global Recall against the simple heuristic baseline on the test split, mathematically proving the performance lift.
