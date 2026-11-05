import urllib.request
# We can use chrome to run javascript and log or use playwright/selenium or inspect the HTML directly.
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html') as f:
    html = f.read()

# Let's check where .by-brand-logo is defined and what other rules exist
import re
print("Matching rules for by-brand-logo:")
for m in re.finditer(r'([^{}]*by-brand-logo[^{}]*\{[^}]*\})', html):
    print(m.group(0))

print("\nMatching rules for header img:")
for m in re.finditer(r'([^{}]*header\s+img[^{}]*\{[^}]*\})', html):
    print(m.group(0))
