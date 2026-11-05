import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://brainyogaacademy.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

header_m = re.findall(r'<header[^>]*>.*?</header>', html, re.DOTALL)
if header_m:
    print(header_m[0])
