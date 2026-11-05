import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
req = urllib.request.Request('https://brainyogaacademy.com/brain-yoga-for-busy-minds/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)'})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read().decode('utf-8')

print("Status:", resp.status)
print("Page length:", len(html))
print("Has Tailwind CDN:", 'cdn.tailwindcss.com' in html)
print("Has Lucide Icons CDN:", 'unpkg.com/lucide' in html)
print("Has uncropped hero image (14_new.webp):", 'https://brainyogaacademy.com/wp-content/uploads/2026/11/rajendra_14_new.webp' in html)
print("Has trainer portrait:", 'https://brainyogaacademy.com/wp-content/uploads/2026/11/trainer_rajendra_portrait.jpg' in html)
print("Has barking dog:", 'https://brainyogaacademy.com/wp-content/uploads/2026/11/barking_dog_new.webp' in html)
print("Has practice photos:", 'https://brainyogaacademy.com/wp-content/uploads/2026/11/practice_braingym.webp' in html)
print("Has corporate photos:", 'https://brainyogaacademy.com/wp-content/uploads/2026/11/workshop_corporate_team.webp' in html)
print("Has booking modal:", 'id="individualModal"' in html)
print("Has corporate modal:", 'id="corporateModal"' in html)
print("Has floating WhatsApp:", 'wa.me/918331929240' in html)
print("Astra header present (should be False for Canvas):", 'ast-theme-transparent-header' in html)
