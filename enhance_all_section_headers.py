import re

files = [
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html"
]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Add reveal-on-scroll to any section header not yet having it
    # Pattern: class="text-center max-w-3xl mx-auto
    content = re.sub(
        r'class="text-center max-w-(?:3xl|4xl) mx-auto',
        'class="reveal-on-scroll text-center max-w-3xl mx-auto',
        content
    )
    # Avoid duplicate reveal-on-scroll
    content = content.replace("reveal-on-scroll reveal-on-scroll", "reveal-on-scroll")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"[{fpath}] Enhanced section headers with reveal-on-scroll.")
