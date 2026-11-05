#!/usr/bin/env python3
"""Insert bottom flickering bar after </footer> in busy-minds.html"""

HTML_PATH = "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

BOTTOM_BAR_HTML = """
    <!-- ========================================================================= -->
    <!-- BOTTOM FLICKERING BAR: BRAIN YOGA FOR CHILDREN LINK                      -->
    <!-- ========================================================================= -->
    <div class="by-bottom-flicker-bar" aria-label="Children Program Link Bottom">
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

# Check if HTML div already present (look for the aria-label specifically)
if 'aria-label="Children Program Link Bottom"' in content:
    print("⚠️  Bottom bar already present in HTML — skipping")
else:
    footer_close_idx = content.rfind("</footer>")
    if footer_close_idx == -1:
        print("ERROR: </footer> not found!")
        exit(1)
    insert_at = footer_close_idx + len("</footer>")
    content = content[:insert_at] + BOTTOM_BAR_HTML + content[insert_at:]
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Bottom flickering bar inserted after </footer> at char {insert_at}")
    print(f"   File size: {len(content)} chars")
