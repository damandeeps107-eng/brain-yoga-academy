#!/usr/bin/env python3
import re

HTML_FILE = "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html"
CSS_FILE = "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/compiled_tailwind.css"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

with open(CSS_FILE, "r", encoding="utf-8") as f:
    compiled_css = f.read()

start_marker = "<!-- Tailwind CSS CDN -->"
end_marker = "<!-- Lucide Icons CDN -->"

s_pos = html.find(start_marker)
e_pos = html.find(end_marker)

if s_pos == -1 or e_pos == -1:
    print("Markers not found!")
    exit(1)

replacement = f"""<!-- Pre-compiled Ultra-Fast Static Tailwind CSS (Zero Runtime Overhead) -->
    <style id="by-compiled-tailwind">
{compiled_css}
    </style>

    """

new_html = html[:s_pos] + replacement + html[e_pos:]

# Defer Lucide
new_html = new_html.replace(
    '<script src="https://unpkg.com/lucide@latest"></script>',
    '<script defer src="https://unpkg.com/lucide@latest"></script>'
)

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"✅ Replaced successfully! New size: {len(new_html)} chars")
