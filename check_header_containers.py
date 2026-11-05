import urllib.request, ssl

ctx = ssl._create_unverified_context()

req = urllib.request.Request('https://brainyogaacademy.com/wp-content/uploads/elementor/css/post-76.css', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    css = resp.read().decode('utf-8')

for rule in css.split('}'):
    if '{' in rule:
        selector, body = rule.split('{', 1)
        if any(cid in selector for cid in ['1876c47', '49cd7f0', '3debe25', '52259ba', '78efb94', '0d80f0c']):
            print(f"{selector.strip()} {{ {body.strip()} }}")
