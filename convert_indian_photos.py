import os
import glob
from PIL import Image

BRAIN_DIR = "/Users/user/.gemini/antigravity/brain/bb086ab2-813b-4f49-93e8-89022ca4e399"
DEST_DIR = "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing"
SUBDIR = os.path.join(DEST_DIR, "brain-yoga-for-busy-minds")

TARGETS = {
    "practice_braingym.webp": "practice_indian_braingym",
    "practice_ambidextrous.webp": "practice_indian_ambidextrous",
    "practice_pranayama.webp": "practice_indian_pranayama",
    "practice_mindfulness.webp": "practice_indian_mindfulness",
    "practice_visualization.webp": "practice_indian_visualization",
    "practice_eft.webp": "practice_indian_eft",
    "practice_yoganidra.webp": "practice_indian_yoganidra",
    "practice_awareness.webp": "practice_indian_awareness",
    "workshop_corporate_team.webp": "workshop_indian_team",
    "workshop_corporate_chair.webp": "workshop_indian_chair"
}

def process_images():
    for out_name, prefix in TARGETS.items():
        pattern = os.path.join(BRAIN_DIR, f"{prefix}*.jpg")
        matches = sorted(glob.glob(pattern))
        if not matches:
            print(f"[WAITING] No match found for {prefix}")
            continue
        latest_file = matches[-1]
        print(f"Processing {latest_file} -> {out_name}...")
        
        with Image.open(latest_file) as img:
            img = img.convert("RGB")
            # Resize appropriately, maintain good aspect ratio
            w, h = img.size
            target_w = 900
            target_h = int((h / w) * target_w)
            resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
            
            dest_path1 = os.path.join(DEST_DIR, out_name)
            resized.save(dest_path1, "WEBP", quality=88)
            print(f" Saved: {dest_path1}")
            
            if os.path.exists(SUBDIR):
                dest_path2 = os.path.join(SUBDIR, out_name)
                resized.save(dest_path2, "WEBP", quality=88)
                print(f" Saved: {dest_path2}")

if __name__ == "__main__":
    process_images()
