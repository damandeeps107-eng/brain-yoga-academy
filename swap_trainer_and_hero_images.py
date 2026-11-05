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
    
    # 1. Hero: Use 14.png (rajendra_14_new.webp)
    content = content.replace("rajendra_hero_new.webp", "rajendra_14_new.webp")
    
    # 2. Trainer section: Restore original trainer photo (trainer_rajendra_real.webp)
    content = content.replace("rajendra_trainer_new_square.webp", "trainer_rajendra_real.webp")
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Updated {fpath} successfully.")
