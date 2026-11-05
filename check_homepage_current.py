import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://brainyogaacademy.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

# Check menu items on homepage
items = re.findall(r'<li[^>]*class=[\'"][^\'"]*menu-item[^\'"]*[\'"][^>]*>.*?<a[^>]*>(.*?)</a>', html, re.DOTALL)
print("Homepage Nav Links count:", len(items))
for t in items[:8]:
    print("  Link:", t.strip())

# Check logo tag
logo = re.findall(r'<div[^>]*class=[\'"][^\'"]*widget-image[^\'"]*[\'"][^>]*>.*?</div>', html, re.DOTALL)
if logo:
    print("\nLogo Widget HTML:")
    print(logo[0][:500])
