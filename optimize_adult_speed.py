#!/usr/bin/env python3
"""
Speed optimization for busy-minds.html:
1. Remove anti-cache meta tags that make Safari reload everything from scratch.
2. Add resource hints (preconnect, dns-prefetch, prefetch).
3. Set fetchpriority="high" on hero/logo images.
4. Set loading="lazy" decoding="async" on all below-the-fold images.
"""
import re

FILE = "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove anti-cache meta tags
old_meta = """    <!-- Cache Buster Meta Tags for Safari & Mobile Browsers -->
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">"""

new_meta = """    <!-- Performance & Browser Cache Hints -->
    <meta http-equiv="Cache-Control" content="public, max-age=604800, stale-while-revalidate=86400">
    <link rel="preconnect" href="https://brainyogaacademy.com">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="dns-prefetch" href="https://cdn.tailwindcss.com">
    <link rel="dns-prefetch" href="https://unpkg.com">
    <link rel="prefetch" href="https://brainyogaacademy.com/">"""

if old_meta in content:
    content = content.replace(old_meta, new_meta)
    print("✅ Replaced anti-cache meta with performance cache & preconnect hints")
else:
    # Try regex
    content = re.sub(
        r'<!-- Cache Buster Meta Tags.*?<meta http-equiv="Expires" content="0">',
        new_meta.strip(),
        content,
        flags=re.DOTALL
    )
    print("✅ Cleaned anti-cache meta via regex")

# 2. Hero logo: add fetchpriority="high" decoding="async"
content = re.sub(
    r'<img decoding="async" src="https://brainyogaacademy.com/wp-content/uploads/2026/11/official_logo.png" alt="Brain Yoga Academy" class="by-brand-logo"',
    r'<img fetchpriority="high" decoding="async" src="https://brainyogaacademy.com/wp-content/uploads/2026/11/official_logo.png" alt="Brain Yoga Academy" class="by-brand-logo"',
    content
)

# 3. Hero image: add fetchpriority="high" decoding="async"
content = re.sub(
    r'<img src="rajendra_14_new.webp" alt="Rajendra Boddu - Brain Yoga Trainer" class="w-full h-auto block max-w-full rounded-2xl shadow-xl border border-slate-100">',
    r'<img fetchpriority="high" decoding="async" src="rajendra_14_new.webp" alt="Rajendra Boddu - Brain Yoga Trainer" class="w-full h-auto block max-w-full rounded-2xl shadow-xl border border-slate-100">',
    content
)

# 4. Barking dog: add loading="lazy" decoding="async"
content = re.sub(
    r'<img src="barking_dog_new.webp" alt="10 People and 1 Barking Dog - Mindset Metaphor" class="w-full h-auto',
    r'<img loading="lazy" decoding="async" src="barking_dog_new.webp" alt="10 People and 1 Barking Dog - Mindset Metaphor" class="w-full h-auto',
    content
)

# 5. Practice images (ensure all have loading="lazy" decoding="async")
practice_files = [
    "practice_braingym.webp", "practice_ambidextrous.webp", "practice_pranayama.webp",
    "practice_mindfulness.webp", "practice_visualization.webp", "practice_eft.webp",
    "practice_yoganidra.webp", "practice_awareness.webp"
]
for p in practice_files:
    content = re.sub(
        rf'<img(?![^>]*loading=[\"\']lazy[\"\']) src="{p}"',
        f'<img loading="lazy" decoding="async" src="{p}"',
        content
    )

# 6. Workshop images
for w in ["workshop_corporate_team.webp", "workshop_corporate_chair.webp", "trainer_rajendra_portrait.jpg"]:
    content = re.sub(
        rf'<img(?![^>]*loading=[\"\']lazy[\"\']) src="{w}"',
        f'<img loading="lazy" decoding="async" src="{w}"',
        content
    )

# 7. Add instant hover-preloader script before </body>
instant_nav_script = """
    <!-- Instant Page Preloader for Lightning-Fast Navigation -->
    <script>
    (function() {
        var preloaded = false;
        function prefetchKids() {
            if (preloaded) return;
            preloaded = true;
            var l = document.createElement('link');
            l.rel = 'prefetch';
            l.href = 'https://brainyogaacademy.com/';
            document.head.appendChild(l);
        }
        // Prefetch when user hovers or touches children links
        document.querySelectorAll('a[href="https://brainyogaacademy.com/"]').forEach(function(a) {
            a.addEventListener('mouseenter', prefetchKids, {once: true, passive: true});
            a.addEventListener('touchstart', prefetchKids, {once: true, passive: true});
        });
        // Idle prefetch after 1.5s
        if ('requestIdleCallback' in window) {
            requestIdleCallback(prefetchKids);
        } else {
            setTimeout(prefetchKids, 1500);
        }
    })();
    </script>
</body>"""

if "Instant Page Preloader" not in content:
    content = content.replace("</body>", instant_nav_script)
    print("✅ Added instant hover preloader script")

with open(FILE, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Saved optimized busy-minds.html ({len(content)} chars)")
