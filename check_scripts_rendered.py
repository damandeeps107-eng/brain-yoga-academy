import urllib.request, ssl

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://brainyogaacademy.com/brain-yoga-for-busy-minds/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

print("Has 'cdn.tailwindcss.com':", 'cdn.tailwindcss.com' in html)
print("Has 'tailwind.config':", 'tailwind.config' in html)
print("Has 'unpkg.com/lucide':", 'unpkg.com/lucide' in html)
print("Has '<style>':", '<style>' in html)
print("Has '<header':", '<header' in html)
