import os

HTML_FILES = [
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html"
]

REPLACEMENTS = [
    ("custom_fit15.webp", "practice_braingym.webp"),
    ("custom_stretching_fun.webp", "practice_ambidextrous.webp"),
    ("custom_chair_yoga.webp", "practice_pranayama.webp"),
    ("mindfulness_peace.jpg", "practice_mindfulness.webp"),
    ("custom_sound_bath.webp", "practice_visualization.webp"),
    ("custom_laughter_yoga.webp", "practice_eft.webp"),
    ("custom_ergo_posture.webp", "practice_yoganidra.webp"),
    ("executive_focus.jpg", "practice_awareness.webp"),
    ("workshop_team.jpg", "workshop_corporate_team.webp"),
    ("workshop_interactive.jpg", "workshop_corporate_chair.webp")
]

for file_path in HTML_FILES:
    if not os.path.exists(file_path):
        print(f"Skipping {file_path} (not found)")
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    count = 0
    for old_val, new_val in REPLACEMENTS:
        if old_val in content:
            content = content.replace(old_val, new_val)
            count += 1
            print(f"[{os.path.basename(file_path)}] Replaced {old_val} -> {new_val}")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {file_path} with {count} replacements.\n")
