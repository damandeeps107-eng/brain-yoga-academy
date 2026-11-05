import os

files = [
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html"
]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace trainer image with the reliable 100% visible solid RGB portrait
    content = content.replace(
        '<img src="trainer_rajendra_real.webp" alt="Rajendra Boddu" class="w-full h-full object-cover object-top" loading="lazy" decoding="async">',
        '<img src="trainer_rajendra_portrait.jpg" alt="Rajendra Boddu" class="w-full h-full object-cover object-top" loading="eager" decoding="async">'
    )
    # Also catch any variations
    content = content.replace("trainer_rajendra_real.webp", "trainer_rajendra_portrait.jpg")
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Updated {fpath} with trainer_rajendra_portrait.jpg")
