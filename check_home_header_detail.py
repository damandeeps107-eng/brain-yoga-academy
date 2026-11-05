import urllib.request, ssl, re

ctx = ssl._create_unverified_context()

req = urllib.request.Request('https://brainyogaacademy.com/', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

# Search for the header container on the homepage
header_m = re.findall(r'<header[^>]*>.*?</header>', html, re.DOTALL)
if header_m:
    # Print the logo image and containers inside
    logo_m = re.findall(r'<div[^>]*class=[\'"][^\'"]*widget-image[^\'"]*[\'"][^>]*>.*?</div>', header_m[0], re.DOTALL)
    print("Logo widget on homepage:")
    for lm in logo_m:
        print(lm)
    
    # Print nav menu widget on homepage
    nav_m = re.findall(r'<div[^>]*class=[\'"][^\'"]*widget-nav-menu[^\'"]*[\'"][^>]*>.*?</div>\s*</div>', header_m[0], re.DOTALL)
    print("\nNav menu widget on homepage count:", len(nav_m))
    for nm in nav_m:
        print(nm[:400])
