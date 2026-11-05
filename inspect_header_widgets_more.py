import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://brainyogaacademy.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

header_m = re.findall(r'<header[^>]*>.*?</header>', html, re.DOTALL)
if header_m:
    # Print all widgets inside header
    widgets = re.findall(r'<div[^>]*class=[\'"][^\'"]*elementor-widget[^\'"]*[\'"][^>]*>.*?</div>\s*</div>\s*</div>', header_m[0], re.DOTALL)
    print("Found header widget chunks:", len(widgets))
    for w in widgets:
        print("--- WIDGET ---")
        print(w[:300])
