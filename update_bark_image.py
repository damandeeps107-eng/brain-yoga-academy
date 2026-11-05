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
    
    content = content.replace("barking_dog_real_faces.webp", "barking_dog_new.webp")
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Updated {fpath} with barking_dog_new.webp")
