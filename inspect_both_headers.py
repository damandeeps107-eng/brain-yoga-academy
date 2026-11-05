import urllib.request, ssl, re

ctx = ssl._create_unverified_context()

pages = [
    ('HOMEPAGE', 'https://brainyogaacademy.com/'),
    ('BUSY MINDS', 'https://brainyogaacademy.com/brain-yoga-for-busy-minds/')
]

for label, url in pages:
    print(f"\n==================== {label}: {url} ====================")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        with urllib.request.urlopen(req, context=ctx) as resp:
            html = resp.read().decode('utf-8')
        
        print("Page Length:", len(html))
        # Look for headers
        headers = re.findall(r'<header[^>]*>.*?</header>', html, re.DOTALL)
        print(f"Total <header> tags: {len(headers)}")
        for idx, h in enumerate(headers):
            print(f"--- Header {idx+1} ---")
            print(h[:600])
            # Check img tags in header
            imgs = re.findall(r'<img[^>]+>', h)
            print("  Images in header:", imgs)
    except Exception as e:
        print("Error fetching:", e)
