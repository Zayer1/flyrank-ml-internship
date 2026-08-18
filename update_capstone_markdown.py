import nbformat

path = 'work/notebooks/capstone.ipynb'

with open(path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

for cell in nb.cells:
    if cell.cell_type == 'markdown':
        # Issue 8: Data section markdown
        if "fact_content_daily_performance" in cell.source:
            cell.source = cell.source.replace("fact_content_daily_performance", "content_refresh_anonymized.csv")
            cell.source = cell.source.replace("HuggingFace", "the raw data directory")
        
        # Issue 7: Limitations section
        if "8. Limitations" in cell.source:
            # We want to add context about impressions_prev_30d and label flaws
            if "impressions_prev_30d" not in cell.source:
                cell.source += "\n\n- **Heavy Feature Dependency:** The model relies heavily on `impressions_prev_30d` and other traffic shapes, which means entirely new URLs without 30 days of history cannot be accurately scored.\n- **Label Definition Flaws:** The label `trend_direction == 'down'` is a binary proxy. As discovered in Week 6, binary proxy labels can sometimes mask the true magnitude of decay, leading to edge cases where slow-burn decay is missed."
        
        # Issue 9: Social post string
        if "GroupKFold" in cell.source and "9. ML-12 Deliverables" in cell.source:
            cell.source = cell.source.replace("GroupKFold", "GroupShuffleSplit")

with open(path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
print("Notebook updated successfully.")
