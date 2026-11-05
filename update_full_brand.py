import re

targets = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html',
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Replace logo block with official brand logo
    old_logo_pattern = r'<a href="busy-minds\.html" class="flex items-center gap-3 group">.*?</a>'
    new_logo_block = """<a href="busy-minds.html" class="flex items-center gap-3 group">
                <img src="official_logo.png" alt="Brain Yoga Academy" class="h-10 sm:h-12 w-auto object-contain">
                <span class="hidden sm:inline-block text-[11px] font-black uppercase tracking-wider text-[#007984] bg-[#E6F7F8] px-2.5 py-1 rounded-md border border-[#007984]/20">
                    For Busy Minds
                </span>
            </a>"""
    html = re.sub(old_logo_pattern, new_logo_block, html, flags=re.DOTALL)

    # 2. Update footer logo as well
    old_footer_logo = r'<div>\s*<span class="text-lg font-black text-white tracking-tight">\s*Brain Yoga<span class="text-orangeBrand">\.</span>\s*</span>'
    new_footer_logo = """<div>
                    <img src="official_logo.png" alt="Brain Yoga Academy" class="h-9 w-auto brightness-0 invert opacity-95 mb-2">"""
    html = re.sub(old_footer_logo, new_footer_logo, html)

    # 3. Ensure the exact Teal #007984 and Orange #FD8742 are set everywhere
    html = html.replace('#0F6E8C', '#007984')
    html = html.replace('#0B6573', '#085C65')
    html = html.replace('#F58220', '#FD8742')
    html = html.replace('#E06D0C', '#D36005')

    # 4. Make section backgrounds distinctly alternate between White and Warm Peach #FFF3EB
    html = html.replace('bg-peachBgAlt', 'bg-[#FFEADB]')
    html = html.replace('bg-peachBg', 'bg-[#FFF3EB]')

    with open(t, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Refined branding in {t}")

print("All targets branded with official logo and exact colors!")
