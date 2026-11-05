import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://brainyogaacademy.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

print("Homepage status: 200 OK")
print("Has 'For Adults' in homepage:", 'For Adults' in html or 'brain-yoga-for-busy-minds' in html)

# Find all links in nav
nav_links = re.findall(r'<li[^>]*class=[\'"][^\'"]*menu-item[^\'"]*[\'"][^>]*>.*?<a[^>]*href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>', html, re.DOTALL)
print(f"Total nav links rendered on homepage: {len(nav_links)}")
for href, title in nav_links:
    print(f"  --> Title: '{title.strip()}' | Href: '{href}'")
