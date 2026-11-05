import urllib.request, ssl

ctx = ssl._create_unverified_context()

urls_to_test = [
    'https://brainyogaacademy.com/brain-yoga-for-busy-minds/',
    'https://brainyogaacademy.com/?page_id=1242'
]

for url in urls_to_test:
    print(f"\n--- Testing Anonymous Public Access to: {url} ---")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            print("Status Code:", resp.status)
            print("Final URL:", resp.geturl())
            html = resp.read().decode('utf-8')
            print(f"Content Length: {len(html)} bytes")
            print("Has 'Deadlines. Pressure.':", 'Deadlines. Pressure.' in html)
            print("Has 'Rajendra Boddu':", 'Rajendra Boddu' in html)
            print("Has '8 Practical':", 'Our Practices' in html or '8 Practical' in html)
            print("Has Floating WhatsApp:", 'by-floating-wa' in html)
    except Exception as e:
        print("Error accessing URL:", e)
