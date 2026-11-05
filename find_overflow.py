import subprocess
import json

# Let's run chrome with a node script or python script to evaluate document.body.scrollWidth
# We can use chrome's dump-dom or evaluate javascript via a small html test
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html') as f:
    html = f.read()

# Let's inspect any element with fixed width or large min-w
import re
print("Searching for large widths in HTML:")
for m in re.finditer(r'(w-\[[^\]]+\]|min-w-\[[^\]]+\]|width:\s*\d+px)', html):
    print(m.group(0))
