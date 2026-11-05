import subprocess
from PIL import Image

widths = [1440, 1280, 1024, 768, 390]
for w in widths:
    h = 800 if w > 500 else 844
    cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot=/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/test_{w}.png",
        "file:///Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    im = Image.open(f"/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/test_{w}.png")
    # Crop top 150px
    im.crop((0, 0, im.width, 140)).save(f"/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/crop_{w}.png")
    print(f"Captured {w}px header")
