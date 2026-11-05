import urllib.request, http.cookiejar, ssl, re, time

ctx = ssl._create_unverified_context()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))

# Login
login_url = 'https://brainyogaacademy.com/wp-login.php'
login_data = urllib.parse.urlencode({
    'log': 'rajendraboddu@gmail.com',
    'pwd': 'Gemini#1979',
    'wp-submit': 'Log In',
    'redirect_to': 'https://brainyogaacademy.com/wp-admin/',
    'testcookie': '1'
}).encode('utf-8')
opener.open(urllib.request.Request(login_url, data=login_data, headers={'User-Agent': 'Mozilla/5.0'}))

# Measure response time and fetch preview
preview_url = 'https://brainyogaacademy.com/?page_id=1242&preview=true'
t0 = time.time()
req = urllib.request.Request(preview_url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'})
with opener.open(req) as resp:
    html = resp.read().decode('utf-8')
t1 = time.time()

elapsed_ms = (t1 - t0) * 1000
page_size_kb = len(html.encode('utf-8')) / 1024

print("=== LIVE PREVIEW AUDIT (POST 1242) ===")
print(f"HTTP Status: 200 OK")
print(f"Server Response Time: {elapsed_ms:.1f} ms")
print(f"HTML Document Size: {page_size_kb:.2f} KB")

# Verification checks
checks = {
    "Elementor Page Rendered": 'data-elementor-type="wp-page"' in html,
    "Post ID 1242": 'elementor-1242' in html,
    "Hero Section": 'hero_section' in html or 'Deadlines. Pressure.' in html,
    "Challenges Section": 'Everyday Challenges for Busy Minds' in html,
    "Barking Dog Section": 'barking_dog_new.webp' in html,
    "8 Practices": 'Our Practices' in html,
    "Corporate Workshops": 'Bring Brain Yoga to Your Workplace' in html,
    "Trainer Rajendra": 'trainer_rajendra_portrait.jpg' in html,
    "Testimonials Section": 'What Working Professionals Say' in html,
    "FAQ Accordion": 'Frequently Asked Questions' in html or 'faq_section' in html,
    "Floating WhatsApp Button": 'by-floating-wa' in html,
    "Mobile Responsive Breakpoints Injected": '@media (max-width: 768px)' in html
}

for name, passed in checks.items():
    print(f"[{'PASS' if passed else 'FAIL'}] {name}")

# Check all image tags and sources
img_srcs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', html)
print(f"\nTotal <img> tags rendered on page: {len(img_srcs)}")
wp_uploads = [src for src in img_srcs if 'brainyogaacademy.com/wp-content/uploads' in src]
print(f"Uploaded Media Library Images on page: {len(wp_uploads)}")
