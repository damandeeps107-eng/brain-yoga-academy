import urllib.request, ssl

ctx = ssl._create_unverified_context()

css_urls = [
    'https://brainyogaacademy.com/wp-content/uploads/elementor/css/post-76.css',
    'https://brainyogaacademy.com/wp-content/uploads/elementor/css/post-1111.css',
    'https://brainyogaacademy.com/wp-content/uploads/elementor/css/post-1242.css'
]

for cu in css_urls:
    try:
        req = urllib.request.Request(cu, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = resp.read()
            print(f"CSS: {cu} -> Status: {resp.status} | Length: {len(data)} bytes")
    except Exception as e:
        print(f"CSS: {cu} -> ERROR: {e}")
