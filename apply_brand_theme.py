import re

targets = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html',
]

for t in targets:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Tailwind config with exact colors from kids.html (post-1111.css)
    # Primary Teal: #007984
    # Deep Teal: #0B6573
    # Ice Blue: #D2F0FF
    # Primary Orange: #FD8742 & #F4A261
    # Dark Orange: #D36005
    # Peach Background: #FFF0E6 & #FFE8DA
    # Dark text: #1F1F1F & #111827
    
    content = content.replace("tealBrand: '#0F6E8C'", "tealBrand: '#007984'")
    content = content.replace("tealDark: '#0B6573'", "tealDark: '#085C65'")
    content = content.replace("tealLight: '#E8F5F8'", "tealLight: '#E6F7F8'")
    content = content.replace("tealIce: '#DDF7FF'", "tealIce: '#D2F0FF'")
    content = content.replace("orangeBrand: '#F58220'", "orangeBrand: '#FD8742'")
    content = content.replace("orangeDark: '#E06D0C'", "orangeDark: '#D36005'")
    content = content.replace("orangeLight: '#FFF4EC'", "orangeLight: '#FFE8DA'")
    content = content.replace("peachBg: '#FFF8F3'", "peachBg: '#FFF3EB'")
    content = content.replace("peachBgAlt: '#FFF6EE'", "peachBgAlt: '#FFEADB'")
    content = content.replace("navyBrand: '#0F2537'", "navyBrand: '#1A2E35'")
    
    # Also replace raw hex codes in CSS
    content = content.replace('#0F6E8C', '#007984')
    content = content.replace('#F58220', '#FD8742')
    content = content.replace('#0F2537', '#1A2E35')
    content = content.replace('#FFF8F3', '#FFF3EB')
    content = content.replace('#FFF6EE', '#FFEADB')
    content = content.replace('#DDF7FF', '#D2F0FF')
    content = content.replace('#FFF4EC', '#FFE8DA')
    content = content.replace('#E06D0C', '#D36005')

    # Update button border radius from rounded-full to rounded-xl (10px - 12px) matching kids.html
    # In kids.html, Elementor buttons have: border-radius: 10px 10px 10px 10px;
    content = re.sub(r'rounded-full\s+(font-bold|font-black|shimmer-btn|text-white)', r'rounded-xl \1', content)

    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Applied exact brand palette to {t}")

print("Brand consistency update completed successfully!")
