import urllib.request, ssl, re

ctx = ssl._create_unverified_context()

req = urllib.request.Request('https://brainyogaacademy.com/brain-yoga-for-busy-minds/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

# Search for official_logo.png in html
logo_tags = re.findall(r'<img[^>]*official_logo\.png[^>]*>', html)
print("Logo tags on busy minds page:")
for lt in logo_tags:
    print(" ", lt)

# Check inline style on logo: does it have style="height: 44px; width: auto;"?
