import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://brainyogaacademy.com/brain-yoga-for-busy-minds/', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

# Find the header element
header_m = re.search(r'<header[^>]*>.*?</header>', html, re.DOTALL)
if header_m:
    print("=== HEADER IN BUSY MINDS ===")
    print(header_m.group(0)[:1500])
