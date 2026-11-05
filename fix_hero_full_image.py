import re

files = [
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html",
    "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html"
]

target_old = '''                <!-- Right Visual Column (5 cols) -->
                <!-- Strictly NO TEXT ON TOP OF IMAGE: Clean portrait, unified bottom bar! -->
                <div class="lg:col-span-5">
                    <div class="by-card">
                        <!-- Clean, unobstructed portrait photo -->
                        <div class="relative h-60 sm:h-72 lg:h-[370px] w-full bg-slate-100 overflow-hidden">
                            <img src="rajendra_hero_new.webp" alt="Rajendra Boddu - Brain Yoga Trainer" class="w-full h-full object-cover object-top" loading="eager" fetchpriority="high">
                        </div>'''

replacement_new = '''                <!-- Right Visual Column (5 cols) -->
                <!-- Strictly NO TEXT ON TOP OF IMAGE: Clean portrait, unified bottom bar! -->
                <div class="lg:col-span-5 flex flex-col justify-center">
                    <div class="by-card max-w-sm sm:max-w-md mx-auto w-full overflow-hidden shadow-lg border border-slate-200/80 bg-white">
                        <!-- Clean, unobstructed full portrait photo (100% visible, no half cut) -->
                        <div class="relative w-full bg-slate-100 overflow-hidden">
                            <img src="rajendra_hero_new.webp" alt="Rajendra Boddu - Brain Yoga Trainer" class="w-full h-auto block object-cover" loading="eager" fetchpriority="high">
                        </div>'''

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if target_old in content:
        content = content.replace(target_old, replacement_new)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {fpath} successfully.")
    else:
        print(f"Target not found in {fpath}, checking fallback...")
        # fallback regex if whitespace differs
        pattern = r'<div class="relative h-60 sm:h-72 lg:h-\[370px\] w-full bg-slate-100 overflow-hidden">\s*<img src="rajendra_hero_new\.webp"[^>]+>\s*</div>'
        sub_repl = '''<div class="relative w-full bg-slate-100 overflow-hidden">
                            <img src="rajendra_hero_new.webp" alt="Rajendra Boddu - Brain Yoga Trainer" class="w-full h-auto block object-cover" loading="eager" fetchpriority="high">
                        </div>'''
        new_content, count = re.subn(pattern, sub_repl, content)
        if count > 0:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Regex updated {fpath} with {count} matches.")
        else:
            print(f"Failed to update {fpath}.")
