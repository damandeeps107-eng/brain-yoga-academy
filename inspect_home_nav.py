import urllib.request, ssl, re

ctx = ssl._create_unverified_context()

req = urllib.request.Request('https://brainyogaacademy.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

print("Homepage length:", len(html))
# Search for nav or menu tags
navs = re.findall(r'<nav[^>]*>.*?</nav>', html, re.DOTALL)
print(f"Total <nav> elements on homepage: {len(navs)}")
for i, n in enumerate(navs):
    print(f"\nNav {i+1}:")
    print(n[:300])

# Search for any menu links
links = re.findall(r'<li[^>]*class=[\'"][^\'"]*menu-item[^\'"]*[\'"][^>]*>.*?</li>', html, re.DOTALL)
print(f"\nTotal menu-item <li> elements on homepage: {len(links)}")
for l in links[:5]:
    print("Item:", re.sub(r'\s+', ' ', l))
