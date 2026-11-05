import re

files = [
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html"
]

grids_to_stagger = [
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-4">',
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">',
    '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">',
    '<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">',
    '<div class="grid grid-cols-1 md:grid-cols-2 gap-6">'
]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    for g in grids_to_stagger:
        repl = g.replace('class="grid', 'class="stagger-grid grid')
        content = content.replace(g, repl)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[{fpath}] Added stagger-grid to all remaining card grids.")
