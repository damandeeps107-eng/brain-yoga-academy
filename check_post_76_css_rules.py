import urllib.request, ssl

ctx = ssl._create_unverified_context()

req = urllib.request.Request('https://brainyogaacademy.com/wp-content/uploads/elementor/css/post-76.css', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    css = resp.read().decode('utf-8')

print("Length of post-76.css:", len(css))
# Print all rules
for line in css.split('}'):
    if 'accc0c6' in line or 'bbb6f2d' in line or 'img' in line or 'logo' in line:
        print(line + '}')
