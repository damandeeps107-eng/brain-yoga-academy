import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://brainyogaacademy.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

print("Has 'For Adults':", 'For Adults' in html)
print("Has 'brain-yoga-for-busy-minds':", 'brain-yoga-for-busy-minds' in html)

# Find all links in nav
nav_links = re.findall(r'<li[^>]*class=[\'"][^\'"]*menu-item[^\'"]*[\'"][^>]*>.*?<a[^>]*href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>', html, re.DOTALL)
for href, title in nav_links:
    print(f"  --> Title: '{title.strip()}' | Href: '{href}'")
