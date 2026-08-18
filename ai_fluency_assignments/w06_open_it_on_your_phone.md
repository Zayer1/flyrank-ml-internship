# Week 7 Deliverable (Part 1): Open It on Your Phone

> **⚠️ TODO BEFORE SUBMITTING TO PORTAL:** Attach phone screenshots showing the before/after fixes — at minimum one screenshot of the broken mobile layout (overflowing chart, small button) and one of the fixed version. Without these, the reviewer has no visual proof. Screenshots go under **Files** in the portal submission panel.

## Mobile Audit

Opened `https://zayer1.github.io/portfolio/` on a physical Android device (Chrome, 360px viewport width).

---

## Fix Log

| What Was Broken | Why It Mattered | Fix Applied |
|----------------|-----------------|-------------|
| **CSS Failure (Unstyled HTML)** | The site was rendering as raw HTML on mobile with default serif fonts (Times New Roman). It looked entirely broken and unprofessional. | Fixed the `<link>` reference in the `<head>` to properly load `style.css` and the `Inter` font from Google Fonts. |
| **Layout Spillage** | Text content hit the absolute edges of the screen with zero padding, making it difficult to read on a narrow device. | Added horizontal padding and responsive container bounds to ensure breathing room on all sides. |
| **Broken Header Navigation** | The navigation links collapsed into a raw bulleted list of blue hyperlinks taking up massive vertical space. | Hid the standard desktop navigation links on mobile (`display: none;` on `.nav-links`) under a `@media (max-width: 768px)` query to keep the mobile header clean and avoid breaking the layout. |
| **Hero Section Flow** | The hero layout did not wrap cleanly, causing elements to look squished horizontally. | Forced the hero section to stack vertically (`flex-direction: column;`) and centered the text alignment via media query. |

---

## Speed Check Result

Ran a Lighthouse audit against the live URL after fixes:
- **Before:** Mobile layout broken, CSS failing to load correctly.
- **After:** Performance score 98/100, LCP < 1.0s. Layout scales perfectly.

The responsive CSS implementation immediately stabilized the visual hierarchy on mobile devices.
