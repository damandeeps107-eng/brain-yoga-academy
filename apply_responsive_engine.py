import json, re

input_script = '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/build_elementor_native_page.py'
with open(input_script, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace global_css_widget html definition with enhanced mobile-responsive and floating WhatsApp widget
old_css_start = code.find('global_css_widget = {')
old_css_end = code.find('# =========================================================================\n# SECTION 1: HERO SECTION', old_css_start)

enhanced_css_widget = '''global_css_widget = {
    "id": get_id(),
    "elType": "widget",
    "widgetType": "html",
    "settings": {
        "html": """<style>
/* Brain Yoga Brand Standards & Speed Optimizations */
:root {
    --by-teal: #007984;
    --by-teal-dark: #005a63;
    --by-orange: #FD8742;
    --by-orange-dark: #D36005;
    --by-peach: #FFE8DA;
    --by-ice-blue: #D2F0FF;
    --by-dark: #1F1F1F;
}

/* Fluid Resets & Overflow Protection */
*, *::before, *::after {
    box-sizing: border-box !important;
}
html, body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
    scroll-behavior: smooth !important;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* 60fps GPU-Accelerated Interactions */
.by-card-hover {
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    will-change: transform, box-shadow;
    transform: translateZ(0);
}
.by-card-hover:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 16px 32px -4px rgba(0, 121, 132, 0.15) !important;
}
.by-img-zoom img {
    transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1) !important;
    will-change: transform;
}
.by-img-zoom:hover img {
    transform: scale(1.03) !important;
}

/* Image fluid scaling & aspect ratio protection */
.elementor-widget-image img, img {
    max-width: 100% !important;
    height: auto !important;
    display: block;
}

/* Tablet & Mobile Breakpoints */
@media (max-width: 1024px) {
    .e-con-boxed {
        padding-left: 20px !important;
        padding-right: 20px !important;
    }
}

@media (max-width: 768px) {
    /* Section vertical padding on mobile */
    .elementor-section, .e-con {
        padding-left: 16px !important;
        padding-right: 16px !important;
    }
    #hero_section, #challenges_section, #perspective_section, 
    #philosophy_section, #practices_section, #corporate_section, 
    #trainer_section, #testimonials_section, #faq_section {
        padding-top: 45px !important;
        padding-bottom: 45px !important;
    }

    /* Stack 2-column sections cleanly on mobile */
    #hero_section, #trainer_section {
        flex-direction: column !important;
    }
    #hero_section > .e-con, #trainer_section > .e-con {
        width: 100% !important;
        max-width: 100% !important;
    }

    /* Mobile typography scaling */
    h1.elementor-heading-title, #hero_section h1 {
        font-size: 28px !important;
        line-height: 1.25 !important;
    }
    h2.elementor-heading-title {
        font-size: 24px !important;
        line-height: 1.3 !important;
    }
    h3.elementor-heading-title {
        font-size: 19px !important;
        line-height: 1.35 !important;
    }

    /* Touch-friendly full-width buttons on mobile */
    .elementor-widget-button {
        width: 100% !important;
    }
    .elementor-widget-button .elementor-button {
        width: 100% !important;
        min-height: 48px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        font-size: 15px !important;
        padding: 12px 18px !important;
    }
}

@media (max-width: 480px) {
    #hero_section h1 {
        font-size: 25px !important;
    }
    h2.elementor-heading-title {
        font-size: 22px !important;
    }
    p, .elementor-widget-text-editor p {
        font-size: 14.5px !important;
        line-height: 1.6 !important;
    }
}

/* Floating WhatsApp Quick Action Button */
.by-floating-wa {
    position: fixed;
    bottom: 22px;
    right: 20px;
    z-index: 999999;
    background: #25D366;
    color: #FFFFFF !important;
    border-radius: 50px;
    padding: 12px 20px;
    display: inline-flex;
    align-items: center;
    gap: 9px;
    font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 14px;
    font-weight: 700;
    box-shadow: 0 10px 25px rgba(37,211,102,0.45);
    text-decoration: none !important;
    animation: waFloatPulse 3s infinite ease-in-out;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.by-floating-wa:hover {
    transform: translateY(-3px) scale(1.03);
    box-shadow: 0 14px 30px rgba(37,211,102,0.6);
    color: #FFFFFF !important;
}
@keyframes waFloatPulse {
    0%, 100% { transform: scale(1); box-shadow: 0 10px 25px rgba(37,211,102,0.45); }
    50% { transform: scale(1.04); box-shadow: 0 14px 28px rgba(37,211,102,0.65); }
}
@media (max-width: 480px) {
    .by-floating-wa {
        bottom: 16px;
        right: 16px;
        padding: 10px 16px;
        font-size: 13px;
    }
}
</style>

<!-- Floating WhatsApp Quick Connect Button -->
<a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20I%20would%20like%20to%20enquire%20about%20Brain%20Yoga%20for%20Busy%20Minds." target="_blank" rel="noopener noreferrer" class="by-floating-wa" aria-label="Enquire on WhatsApp">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
    <span>Chat on WhatsApp</span>
</a>"""
    }
}
'''

code = code[:old_css_start] + enhanced_css_widget + code[old_css_end:]

# Now let's add the recursive responsive transformer before json.dump
save_marker = "elements.append(footer_section)"
transformer_code = '''elements.append(footer_section)

# =========================================================================
# RECURSIVE RESPONSIVE TRANSFORMER (MOBILE & TABLET ENGINE)
# =========================================================================
def apply_responsive_settings(el, is_root=False):
    settings = el.setdefault('settings', {})
    elType = el.get('elType', '')
    widgetType = el.get('widgetType', '')

    # 1. Root Section Settings
    if is_root:
        settings.setdefault('padding_mobile', {'unit': 'px', 'top': '45', 'right': '16', 'bottom': '45', 'left': '16'})
        settings.setdefault('padding_tablet', {'unit': 'px', 'top': '55', 'right': '20', 'bottom': '55', 'left': '20'})
        if settings.get('flex_direction') == 'row':
            settings['flex_direction_mobile'] = 'column'
            settings['flex_direction_tablet'] = 'column'

    # 2. Heading Typography Responsive Scaling
    if widgetType == 'heading':
        header_size = settings.get('header_size', 'h2')
        font_size = settings.get('typography_font_size', {})
        if isinstance(font_size, dict):
            size = font_size.get('size', 0)
            if header_size == 'h1' or size >= 36:
                settings['typography_font_size_mobile'] = {'unit': 'px', 'size': 28}
                settings['typography_font_size_tablet'] = {'unit': 'px', 'size': 36}
            elif header_size == 'h2' or (28 <= size < 36):
                settings['typography_font_size_mobile'] = {'unit': 'px', 'size': 24}
                settings['typography_font_size_tablet'] = {'unit': 'px', 'size': 28}
            elif header_size in ['h3', 'h4'] or (16 <= size < 28):
                settings['typography_font_size_mobile'] = {'unit': 'px', 'size': max(16, size - 2)}

    # 3. Inner Container Widths, Gaps & Stacking
    if elType == 'container' and not is_root:
        width = settings.get('width', {})
        if isinstance(width, dict):
            size = width.get('size', 100)
            if size <= 50:
                settings['width_mobile'] = {'unit': '%', 'size': 100}
                if size <= 35:
                    settings['width_tablet'] = {'unit': '%', 'size': 48}
                else:
                    settings['width_tablet'] = {'unit': '%', 'size': 100}

        # Check for multiple buttons inside a container (Hero CTA row)
        children = el.get('elements', [])
        button_count = sum(1 for c in children if c.get('widgetType') == 'button')
        if button_count >= 2:
            settings['flex_direction_mobile'] = 'column'
            settings['gap_mobile'] = {'unit': 'px', 'size': 12}
            settings['width_mobile'] = {'unit': '%', 'size': 100}

    for child in el.get('elements', []):
        apply_responsive_settings(child, is_root=False)

for sec in elements:
    apply_responsive_settings(sec, is_root=True)
'''

code = code.replace(save_marker, transformer_code)

with open(input_script, 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully upgraded build_elementor_native_page.py with responsive engine!")
