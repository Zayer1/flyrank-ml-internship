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
        markdown_blocks.append(source)

# Convert all markdown to a single HTML string
full_markdown = "\n\n".join(markdown_blocks)
# Quick fix for markdown headers to give them IDs if needed, but standard markdown lib does some
html_content = markdown.markdown(full_markdown, extensions=['tables', 'fenced_code'])

with open(html_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace the content inside <div class="paper-body"> ... </div>
# Use regex to find <div class="paper-body"> ... </div>
pattern = r'(<div class="paper-body">).*?(</div>\s*</div>\s*</section>)'
replacement = r'\1\n' + html_content.replace('\\', '\\\\') + r'\n\2'
new_index_html = re.sub(pattern, replacement, index_html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_index_html)

print("Updated docs/index.html with full paper content.")
