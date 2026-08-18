# Week 5 Deliverable: Ship the Ugly Version

**The Live URL:**
[https://zayer1.github.io/flyrank-ml-internship](https://zayer1.github.io/flyrank-ml-internship)

**Real Person's Reaction:**
I sent the link to a senior ML engineer friend. 
*What they saw:* They immediately clicked on the interactive frontend and the Capstone paper. 
*What confused them:* They mentioned that the API documentation for the V2 Zero-Shot Cascade wasn't immediately obvious from the homepage, so they had to dig a bit to find how the LLaMA/XGBoost integration worked.
*Did the work land?:* Yes! They were highly impressed that I actually deployed a working FastAPI backend connected to an XGBoost model rather than just leaving the project in a Jupyter notebook.

**The "Still Ugly" List:**
1. The CSS for the frontend app (`docs/index.html` UI) is extremely basic and lacks responsive padding on mobile screens.
2. The navigation between the interactive Capstone and the raw notebooks (`w01` to `w07`) is a bit disjointed; they look like two completely different styles.
3. The LaTeX mathematical formulas in the HTML export of the notebooks sometimes overflow horizontally on smaller screens, forcing the user to scroll.
