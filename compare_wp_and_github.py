import urllib.request, ssl

ctx = ssl._create_unverified_context()

req = urllib.request.Request('https://brainyogaacademy.com/brain-yoga-for-busy-minds/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    wp_html = resp.read().decode('utf-8')

print("WP Page Length:", len(wp_html))

# Let's inspect sections present in wp_html
print("Contains Tailwind CSS CDN:", 'tailwindcss' in wp_html)
print("Contains Lucide Icons CDN:", 'lucide' in wp_html)
print("Contains by-card classes:", 'by-card' in wp_html)
print("Contains Astra Theme Header:", 'ast-theme-transparent-header' in wp_html or 'ast-container' in wp_html)
print("Contains Page Template:", 'elementor_header_footer' in wp_html or 'elementor-template-full-width' in wp_html)
