# Week 7 Deliverable (Part 1): Open It on Your Phone

## Mobile Audit

Opened `https://zayer1.github.io/portfolio/` on a physical Android device (Chrome, 360px viewport width).

---

## Fix Log

| What Was Broken | Why It Mattered | Fix Applied |
|----------------|-----------------|-------------|
| **Precision-Recall curve PNG overflowing right edge** | The image had a hardcoded `width="800"` attribute. On a 360px screen it pushed the layout sideways, causing a horizontal scrollbar on the entire page. | Replaced `width="800"` with `style="max-width: 100%; height: auto;"` on all `<img>` tags in the project detail page. |
| **"Run Prediction" button too small to tap accurately** | Button padding was `8px 16px` — the touch target was under 40px tall, making it easy to miss-tap on a phone. | Increased padding to `14px 28px`, bringing the touch target above 48px (the WCAG recommended minimum). |
| **LaTeX math formula text too pale** | The inline LaTeX rendered in a light gray (`#aaa`) on the slate background. Contrast ratio was approximately 2.8:1, failing WCAG AA (which requires 4.5:1 for body text). | Changed LaTeX text color to `#f1f5f9` (near-white), bringing contrast above 7:1. |
| **Uncompressed PR curve asset (4.2MB PNG)** | Page speed test showed this single image accounting for 71% of total page weight. On a 3G mobile connection, load time was approximately 9 seconds. | Re-exported the chart as WebP at 85% quality. File size dropped from 4.2MB to 94KB with no visible quality loss at portfolio display sizes. |
| **Navigation links not tappable on narrow screens** | The nav bar items were close together with no padding. On a phone, tapping "Capstone" would frequently trigger "Home" or miss entirely. | Added `padding: 8px 12px` to all nav `<a>` elements and switched the layout to a stacked column below 600px. |

---

## Speed Check Result

Ran a Lighthouse audit against the live URL after fixes:
- **Before:** Performance score 51/100, LCP 9.2s
- **After:** Performance score 89/100, LCP 1.4s

The image compression alone accounted for the majority of the improvement.
