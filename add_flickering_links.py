#!/usr/bin/env python3
"""
Add flickering links to busy-minds.html:
- TOP: Update existing aside bar to have flickering animation
- BOTTOM: Add a new flickering bar just before </footer>
"""

import re

HTML_PATH = "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

print(f"File loaded: {len(content)} chars")

# ─────────────────────────────────────────────────────────────
# STEP 1: Add flickering CSS into <style> block (before </style>)
# ─────────────────────────────────────────────────────────────
FLICKER_CSS = """
        /* =========================================================
           FLICKERING LINK ANIMATION — Gentle Glow Pulse
           Sir's requirement: "clearly visible, attractive, gently
           flickering to catch attention without being too distracting"
        ========================================================= */
        @keyframes gentleFlicker {
            0%,  100% {
                opacity: 1;
                box-shadow: 0 0 6px rgba(253, 135, 66, 0.4), 0 0 12px rgba(253, 135, 66, 0.2);
                text-shadow: 0 0 8px rgba(255, 232, 218, 0.6);
            }
            50% {
                opacity: 0.72;
                box-shadow: 0 0 16px rgba(253, 135, 66, 0.9), 0 0 32px rgba(253, 135, 66, 0.5), 0 0 48px rgba(253, 135, 66, 0.2);
                text-shadow: 0 0 14px rgba(255, 255, 255, 0.9);
            }
        }
        .by-flicker-link {
            animation: gentleFlicker 2.6s ease-in-out infinite;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            border-radius: 20px;
            padding: 2px 10px 2px 8px;
            border: 1px solid rgba(253, 135, 66, 0.55);
            background: rgba(253, 135, 66, 0.12);
            font-weight: 700;
            color: #FFE8DA;
            text-decoration: none;
            transition: color 0.2s ease;
            white-space: nowrap;
        }
        .by-flicker-link:hover {
            color: #ffffff;
            animation-play-state: paused;
            box-shadow: 0 0 20px rgba(253, 135, 66, 1);
        }
        .by-bottom-flicker-bar {
            background: linear-gradient(135deg, #085C65 0%, #007984 60%, #0a8f9b 100%);
            padding: 16px 16px;
            text-align: center;
        }
"""

# Check if already added
if "gentleFlicker" in content:
    print("⚠️  Flicker CSS already present — skipping CSS injection")
else:
    # Find the closing </style> in the head (first occurrence before </head>)
    head_end = content.find("</head>")
    style_close = content.rfind("</style>", 0, head_end)
    if style_close == -1:
        print("ERROR: </style> not found before </head>")
        exit(1)
    content = content[:style_close] + FLICKER_CSS + "\n    </style>" + content[style_close + len("</style>"):]
    print("✅ Flicker CSS injected into <style> block")

# ─────────────────────────────────────────────────────────────
# STEP 2: Replace the existing top <aside> bar with flickering version
# ─────────────────────────────────────────────────────────────
NEW_TOP_BAR = """    <!-- ========================================================================= -->
    <!-- TOP FLICKERING BAR: BRAIN YOGA FOR CHILDREN LINK                         -->
    <!-- ========================================================================= -->
    <aside aria-label="Program Announcement" class="bg-[#007984] py-2.5 px-3 sm:px-4 text-center text-xs font-semibold text-white shadow-sm">
        <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 sm:gap-3 flex-wrap text-center leading-tight">
            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold uppercase bg-brandOrange text-white whitespace-nowrap tracking-wide">
                &#x1F9D2; Child Wellness
            </span>
            <span class="text-[11px] sm:text-xs opacity-90">Looking for memory &amp; focus training for kids?</span>
            <a href="https://brainyogaacademy.com/"
               class="by-flicker-link text-[11px] sm:text-xs"
               target="_self" rel="noopener">
                <span>&#x2728; Brain Yoga for Children</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
        </div>
    </aside>"""

# Find and replace the existing aside block
aside_pattern = re.compile(
    r'[ \t]*<!--\s*=+\s*-->\s*\n\s*<!--[^\n]*TOP ANNOUNCEMENT BAR[^\n]*-->\s*\n\s*<!--\s*=+\s*-->\s*\n\s*<aside[^>]*aria-label="Program Announcement"[^>]*>.*?</aside>',
    re.DOTALL
)
match = aside_pattern.search(content)
if match:
    content = content[:match.start()] + NEW_TOP_BAR + content[match.end():]
    print("✅ Top announcement bar replaced with flickering version")
else:
    print("⚠️  Could not find existing aside block via regex — trying simple search")
    # Try a simpler approach: find the aside by its unique aria-label
    aside_start = content.find('<aside aria-label="Program Announcement"')
    if aside_start == -1:
        print("ERROR: aside bar not found!")
        exit(1)
    aside_end = content.find("</aside>", aside_start) + len("</aside>")
    # Also grab the comment lines before it
    comment_start = content.rfind("<!-- =====", 0, aside_start)
    if comment_start != -1:
        # Go back to include the full comment block (find actual line start)
        line_start = content.rfind("\n", 0, comment_start) + 1
        content = content[:line_start] + NEW_TOP_BAR + content[aside_end:]
        print("✅ Top bar replaced via simple search")
    else:
        content = content[:aside_start] + NEW_TOP_BAR + content[aside_end:]
        print("✅ Top bar replaced (no preceding comment)")

# ─────────────────────────────────────────────────────────────
# STEP 3: Add BOTTOM flickering bar just AFTER </footer>
# ─────────────────────────────────────────────────────────────
BOTTOM_BAR = """
    <!-- ========================================================================= -->
    <!-- BOTTOM FLICKERING BAR: BRAIN YOGA FOR CHILDREN LINK                      -->
    <!-- ========================================================================= -->
    <div class="by-bottom-flicker-bar" aria-label="Children Program Link">
        <div style="max-width:900px;margin:0 auto;display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;">
            <span style="font-family:Inter,sans-serif;font-size:12px;font-weight:600;color:rgba(255,255,255,0.88);letter-spacing:0.01em;">
                &#x1F4A1; Also explore our Children's program &mdash;
            </span>
            <a href="https://brainyogaacademy.com/"
               class="by-flicker-link"
               target="_self" rel="noopener"
               style="font-size:13px;">
                <span>&#x2728; Brain Yoga for Children</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
            <span style="font-family:Inter,sans-serif;font-size:11px;color:rgba(255,255,255,0.6);">Memory &middot; Focus &middot; Concentration for Kids</span>
        </div>
    </div>
"""

if "by-bottom-flicker-bar" in content:
    print("⚠️  Bottom flicker bar already present — skipping")
else:
    footer_close_idx = content.rfind("</footer>")
    if footer_close_idx == -1:
        print("ERROR: </footer> not found!")
        exit(1)
    insert_at = footer_close_idx + len("</footer>")
    content = content[:insert_at] + BOTTOM_BAR + content[insert_at:]
    print("✅ Bottom flickering bar added after </footer>")

# ─────────────────────────────────────────────────────────────
# STEP 4: Write back the file
# ─────────────────────────────────────────────────────────────
with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n✅ ALL DONE! File saved: {HTML_PATH}")
print(f"   Total file size: {len(content)} chars")
