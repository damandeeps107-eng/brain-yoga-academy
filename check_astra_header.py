import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://brainyogaacademy.com/brain-yoga-for-busy-minds/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

# Search for ast-theme-transparent-header
pos = html.find('ast-theme-transparent-header')
if pos != -1:
    print("Found 'ast-theme-transparent-header' at char", pos)
    print("Context around it:")
    print(html[pos-100:pos+300])
else:
    print("NOT found!")
