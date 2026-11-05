import urllib.request, ssl, re

ctx = ssl._create_unverified_context()

req = urllib.request.Request('https://brainyogaacademy.com/brain-yoga-for-busy-minds/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

# Search for any styles applied to header, img, nav, logo
print("Looking at head style tags in rendered page:")
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print(f"Total <style> blocks: {len(styles)}")
for s in styles[:5]:
    for line in s.split('\n'):
        if any(k in line for k in ['header', 'logo', 'nav', 'img']):
            print("  ", line.strip())
