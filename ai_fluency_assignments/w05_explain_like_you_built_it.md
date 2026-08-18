# Week 6 Deliverable: Explain It Like You Built It

## The Piece I Picked: Quarto's `_quarto.yml` Configuration File

When I set up my portfolio stack, I followed a tutorial that told me to create a `_quarto.yml` file and paste in a configuration block. I did, and it worked. But I had no idea what any of it actually meant. I understood Quarto was "building" my site but the config file felt like an incantation I had to trust blindly.

I went back and had my AI tutor me on exactly what each line does.

---

## My Plain-Words Explanation

### What `_quarto.yml` actually is

Quarto is a document publishing system. When you run `quarto render`, it looks for a file called `_quarto.yml` in your project root first — this is its instruction manual. Every setting in it tells Quarto how to interpret your content files and what to produce as output.

Think of it like a recipe card sitting on top of all your ingredients (the `.md` and `.ipynb` files). Quarto reads the recipe first, then uses it to decide what to cook.

### The three lines that matter most in mine

**`project: type: website`**  
This tells Quarto to treat the whole folder as a multi-page website rather than a single document. Without this, `quarto render` would try to output one big PDF.

**`output-dir: docs`**  
This tells Quarto to put all the built HTML files into a folder called `docs/`. This is critical for GitHub Pages — GitHub Pages only looks in two places for your site: the root of the repository, or a folder called `/docs`. If I had left this off, GitHub Pages would have served a blank page because it couldn't find any HTML.

**`format: html: theme: cosmo`**  
This tells Quarto to apply a pre-built CSS theme called "cosmo" to the generated HTML. I overrode the theme's default colors with my own palette in a separate `custom.css` file. If I hadn't understood this line, I would have had no idea where to look when my custom colors weren't appearing.

### Why this matters for my capstone

When my GitHub Actions deployment workflow broke in week 4 and the site stopped rebuilding, the error message was `"output directory 'docs' does not exist"`. Because I had taken the time to understand what `output-dir: docs` actually does, I immediately knew the fix: Quarto needs a `docs/` folder to already exist before it writes to it. I added a `mkdir -p docs` step to the workflow, and the problem disappeared in one commit.

I could not have debugged that without genuinely owning what I had built.
