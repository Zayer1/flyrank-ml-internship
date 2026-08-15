import json
import re
import markdown

notebook_path = 'work/notebooks/capstone.ipynb'
html_path = 'docs/index.html'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

markdown_blocks = []
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        
        # 1. Skip the skeleton instructions, Colab badge, and the internal H1
        if "Capstone — mirrors your deployed research paper" in source or "This skeleton is yours to fill" in source or "Working with an AI assistant" in source:
            continue
            
        # Skip the self-check list
        if "[x] Notebook runs top to bottom" in source:
            continue
            
        # Stop before ML-12 Deliverables
        if "9. ML-12 Deliverables" in source:
            break
            
        # 5. Fix Limitations section
        if "5. Limitations" in source and "impressions_prev_30d" not in source:
            source = source.replace(
                "weights overnight.", 
                "weights overnight.\n\n- **Heavy Feature Dependency:** The model relies heavily on `impressions_prev_30d` and other traffic shapes, meaning entirely new URLs without 30 days of history cannot be accurately scored.\n- **Label Definition Flaws:** The label `trend_direction == 'down'` is a binary proxy. As discovered in Week 6, binary proxy labels can sometimes mask the true magnitude of decay, leading to edge cases where slow-burn decay is missed."
            )
            
        markdown_blocks.append(source)

# 3. Join and convert to HTML, enabling standard extensions for lists and tables
full_markdown = "\n\n".join(markdown_blocks)
html_content = markdown.markdown(full_markdown, extensions=['tables', 'fenced_code', 'sane_lists'])

# 4. Remove duplicate H1 tags if any somehow survived, but we skipped it above.
# Also fix the <em> instructions from the skeleton (e.g. "*What this work cannot claim.*")
html_content = re.sub(r'<p><em>.*?</em></p>', '', html_content, flags=re.DOTALL)

# Add IDs to H2 tags for the TOC
html_content = html_content.replace('<h2>Abstract</h2>', '<h2 id="abstract">Abstract</h2>')
html_content = html_content.replace('<h2>1. Question</h2>', '<h2 id="sec-1">1. Question</h2>')
html_content = html_content.replace('<h2>2. Data</h2>', '<h2 id="sec-2">2. Data</h2>')
html_content = html_content.replace('<h2>3. Methodology</h2>', '<h2 id="sec-3">3. Methodology</h2>')
html_content = html_content.replace('<h2>4. Results (vs baseline)</h2>', '<h2 id="sec-4">4. Results</h2>')
html_content = html_content.replace('<h2>5. Limitations</h2>', '<h2 id="sec-5">5. Limitations</h2>')
html_content = html_content.replace('<h2>6. Ranked recommendations</h2>', '<h2 id="sec-6">6. Recommendations</h2>')
html_content = html_content.replace('<h2>7. Artifacts the paper embeds</h2>', '<h2 id="sec-7">7. Artifacts</h2>')
html_content = html_content.replace('<h2>8. Acknowledgments &amp; Data Credit</h2>', '<h2 id="sec-8">8. Acknowledgments</h2>')

with open(html_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# 2. Update the Sidebar TOC to include all 8 sections
new_toc = """
                <ul>
                    <li><a href="#abstract">Abstract</a></li>
                    <li><a href="#sec-1">1. Question</a></li>
                    <li><a href="#sec-2">2. Data</a></li>
                    <li><a href="#sec-3">3. Methodology</a></li>
                    <li><a href="#sec-4">4. Results</a></li>
                    <li><a href="#sec-5">5. Limitations</a></li>
                    <li><a href="#sec-6">6. Recommendations</a></li>
                    <li><a href="#sec-7">7. Artifacts</a></li>
                    <li><a href="#sec-8">8. Acknowledgments</a></li>
                </ul>
"""
index_html = re.sub(r'<ul>\s*<li><a href="#abstract">1\. Abstract</a></li>.*?</ul>', new_toc.strip(), index_html, flags=re.DOTALL)

# Replace the content inside <div class="paper-body"> ... </div>
pattern = r'(<div class="paper-body">).*?(</div>\s*</div>\s*</section>)'
replacement = r'\1\n' + html_content.replace('\\', '\\\\') + r'\n\2'
new_index_html = re.sub(pattern, replacement, index_html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_index_html)

print("Paper polished successfully.")
