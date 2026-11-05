import urllib.request, ssl

ctx = ssl._create_unverified_context()

urls = [
    'https://brainyogaacademy.com/wp-content/uploads/2026/11/official_logo.png',
    'https://brainyogaacademy.com/wp-content/uploads/2026/07/Frame-262-1-1024x180.png',
    'https://damandeeps107-eng.github.io/brain-yoga-academy/official_logo.png'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = resp.read()
            print(f"URL: {u}")
            print(f"  Status: {resp.status} | Length: {len(data)} bytes | Content-Type: {resp.headers.get('content-type')}")
    except Exception as e:
        print(f"URL: {u} -> ERROR: {e}")
