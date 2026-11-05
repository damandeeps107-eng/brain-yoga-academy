import urllib.request, urllib.parse, http.cookiejar, ssl, json, re, uuid

def get_id():
    return uuid.uuid4().hex[:7]

# Load media map
with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/wp_media_map.json', 'r') as f:
    media_map = json.load(f)

def get_img(key):
    item = media_map.get(key, {})
    return {
        "url": item.get("url", ""),
        "id": item.get("id", 0)
    }

# Build Elementor Elements
elements = []

# Global CSS / Custom Helper Styles
global_css_widget = {
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
# =========================================================================
# SECTION 1: HERO SECTION
# =========================================================================
hero_section = {
    "id": "hero_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#FFE8DA",
        "padding": {"unit": "px", "top": "70", "right": "20", "bottom": "70", "left": "20"},
        "flex_direction": "row",
        "flex_wrap": "wrap",
        "justify_content": "space-between",
        "align_items": "center"
    },
    "elements": [
        global_css_widget,
        # Left Column (Copy)
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "width": {"unit": "%", "size": 58},
                "width_mobile": {"unit": "%", "size": 100},
                "flex_direction": "column",
                "gap": {"unit": "px", "size": 18}
            },
            "elements": [
                {
                    "id": get_id(),
                    "elType": "widget",
                    "widgetType": "html",
                    "settings": {
                        "html": '<div style="display:flex; flex-wrap:wrap; gap:8px; align-items:center;">'
                                '<span style="background:#D2F0FF; color:#007984; border:1px solid rgba(0,121,132,0.25); padding:4px 12px; border-radius:9999px; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.08em;">Mind-Wellness For Adults</span>'
                                '<span style="background:#FFFFFF; color:#D36005; border:1px solid rgba(253,135,66,0.3); padding:4px 12px; border-radius:9999px; font-size:12px; font-weight:700;">"Body at home. Mind still at the office."</span>'
                                '</div>'
                    }
                },
                {
                    "id": get_id(),
                    "elType": "widget",
                    "widgetType": "heading",
                    "settings": {
                        "title": "Deadlines. Pressure. Responsibilities.<br><span style='color: #007984;'>Is Your Mind Getting a Break?</span>",
                        "header_size": "h1",
                        "title_color": "#1F1F1F",
                        "typography_font_family": "Poppins",
                        "typography_font_weight": "800",
                        "typography_font_size": {"unit": "px", "size": 42},
                        "typography_line_height": {"unit": "em", "size": 1.2}
                    }
                },
                {
                    "id": get_id(),
                    "elType": "widget",
                    "widgetType": "text-editor",
                    "settings": {
                        "editor": "<p style='font-size: 17px; line-height: 1.6; color: #334155;'><strong>Brain Yoga for Busy Minds</strong> is a practical mind-wellness program for working professionals, entrepreneurs, and corporate teams who want to pause, reset, and respond to work pressures with clarity and focus.</p>",
                        "text_color": "#334155"
                    }
                },
                {
                    "id": get_id(),
                    "elType": "container",
                    "isInner": True,
                    "settings": {
                        "flex_direction": "row",
                        "flex_wrap": "wrap",
                        "gap": {"unit": "px", "size": 14}
                    },
                    "elements": [
                        {
                            "id": get_id(),
                            "elType": "widget",
                            "widgetType": "button",
                            "settings": {
                                "text": "Book a FREE Introductory Session",
                                "link": {"url": "https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20I%20would%20like%20to%20book%20a%20FREE%20Introductory%20Session."},
                                "background_color": "#FD8742",
                                "button_text_color": "#FFFFFF",
                                "typography_font_family": "Poppins",
                                "typography_font_weight": "600",
                                "border_radius": {"unit": "px", "top": 10, "right": 10, "bottom": 10, "left": 10},
                                "button_padding": {"unit": "px", "top": 14, "right": 24, "bottom": 14, "left": 24}
                            }
                        },
                        {
                            "id": get_id(),
                            "elType": "widget",
                            "widgetType": "button",
                            "settings": {
                                "text": "Enquire Corporate Workshops",
                                "link": {"url": "https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20we%20are%20interested%20in%20corporate%20workshops%20for%20our%20team."},
                                "background_color": "#FFFFFF",
                                "button_text_color": "#007984",
                                "typography_font_family": "Poppins",
                                "typography_font_weight": "600",
                                "border_border": "solid",
                                "border_width": {"unit": "px", "top": 2, "right": 2, "bottom": 2, "left": 2},
                                "border_color": "#007984",
                                "border_radius": {"unit": "px", "top": 10, "right": 10, "bottom": 10, "left": 10},
                                "button_padding": {"unit": "px", "top": 12, "right": 22, "bottom": 12, "left": 22}
                            }
                        }
                    ]
                },
                {
                    "id": get_id(),
                    "elType": "widget",
                    "widgetType": "icon-list",
                    "settings": {
                        "icon_list": [
                            {"text": "Hands-on sessions", "selected_icon": {"value": "fas fa-check", "library": "fa-solid"}},
                            {"text": "Online & In-Person", "selected_icon": {"value": "fas fa-laptop", "library": "fa-solid"}},
                            {"text": "Corporate & Individual", "selected_icon": {"value": "fas fa-briefcase", "library": "fa-solid"}}
                        ],
                        "view": "inline",
                        "icon_color": "#007984",
                        "text_color": "#475569"
                    }
                }
            ]
        },
        # Right Column (Trainer Card)
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "width": {"unit": "%", "size": 38},
                "width_mobile": {"unit": "%", "size": 100},
                "background_background": "classic",
                "background_color": "#FFFFFF",
                "border_radius": {"unit": "px", "top": 16, "right": 16, "bottom": 16, "left": 16},
                "box_shadow_box_shadow": {"horizontal": 0, "vertical": 12, "blur": 30, "spread": -4, "color": "rgba(15,37,55,0.1)"},
                "padding": {"unit": "px", "top": 0, "right": 0, "bottom": 0, "left": 0},
                "overflow": "hidden"
            },
            "elements": [
                {
                    "id": get_id(),
                    "elType": "widget",
                    "widgetType": "image",
                    "settings": {
                        "image": get_img('rajendra_14_new.webp'),
                        "image_size": "full"
                    }
                },
                {
                    "id": get_id(),
                    "elType": "container",
                    "isInner": True,
                    "settings": {
                        "padding": {"unit": "px", "top": 16, "right": 20, "bottom": 16, "left": 20},
                        "flex_direction": "row",
                        "justify_content": "space-between",
                        "align_items": "center"
                    },
                    "elements": [
                        {
                            "id": get_id(),
                            "elType": "container",
                            "isInner": True,
                            "settings": {"flex_direction": "column"},
                            "elements": [
                                {
                                    "id": get_id(),
                                    "elType": "widget",
                                    "widgetType": "heading",
                                    "settings": {
                                        "title": "Rajendra Boddu",
                                        "header_size": "h3",
                                        "typography_font_size": {"unit": "px", "size": 18},
                                        "typography_font_weight": "700"
                                    }
                                },
                                {
                                    "id": get_id(),
                                    "elType": "widget",
                                    "widgetType": "heading",
                                    "settings": {
                                        "title": "15 Yrs IT Veteran & Certified Yoga Therapist",
                                        "header_size": "p",
                                        "typography_font_size": {"unit": "px", "size": 12},
                                        "title_color": "#64748B"
                                    }
                                }
                            ]
                        },
                        {
                            "id": get_id(),
                            "elType": "widget",
                            "widgetType": "button",
                            "settings": {
                                "text": "Intro Video",
                                "link": {"url": "https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20please%20share%20the%20introductory%20video."},
                                "background_color": "#D2F0FF",
                                "button_text_color": "#007984",
                                "typography_font_size": {"unit": "px", "size": 12},
                                "border_radius": {"unit": "px", "top": 8, "right": 8, "bottom": 8, "left": 8}
                            }
                        }
                    ]
                }
            ]
        }
    ]
}

elements.append(hero_section)

# =========================================================================
# SECTION 2: EVERYDAY CHALLENGES
# =========================================================================
triggers_data = [
    ("Constant Distraction", "Struggling to stay focused while working or studying?"),
    ("Screen Fatigue & Brain Fog", "Hours of screen time leaving you drained and unproductive?"),
    ("Restless Sleep", "Tired in the morning, body exhausted, mind buzzing with tasks?"),
    ("High Workplace Stress", "Deadlines, demands, and pressure taking a toll on well-being?"),
    ("Overthinking Loop", "Replaying conversations, anticipating problems, mind racing?"),
    ("Lack of Work-Life Boundary", "Body at home, mind still answering office emails?"),
    ("Desk Stiffness & Fatigue", "Sitting for hours causing chronic physical tension?"),
    ("Emotional Reactivity", "Snapping at colleagues or family due to built-up pressure?"),
    ("Quick Fixes Don't Last", "Coffee and scrolling give brief escape, not real mental rest.")
]

trigger_cards = []
for title, desc in triggers_data:
    trigger_cards.append({
        "id": get_id(),
        "elType": "container",
        "isInner": True,
        "settings": {
            "width": {"unit": "%", "size": 31},
            "width_tablet": {"unit": "%", "size": 48},
            "width_mobile": {"unit": "%", "size": 100},
            "background_background": "classic",
            "background_color": "#D2F0FF",
            "border_radius": {"unit": "px", "top": 12, "right": 12, "bottom": 12, "left": 12},
            "padding": {"unit": "px", "top": 20, "right": 20, "bottom": 20, "left": 20},
            "flex_direction": "column",
            "gap": {"unit": "px", "size": 8}
        },
        "elements": [
            {
                "id": get_id(),
                "elType": "widget",
                "widgetType": "heading",
                "settings": {
                    "title": title,
                    "header_size": "h4",
                    "typography_font_size": {"unit": "px", "size": 16},
                    "typography_font_weight": "700",
                    "title_color": "#1F1F1F"
                }
            },
            {
                "id": get_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f"<p style='font-size: 13px; color: #334155; margin:0;'>{desc}</p>"
                }
            }
        ]
    })

challenges_section = {
    "id": "challenges_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {"unit": "px", "top": "70", "right": "20", "bottom": "70", "left": "20"},
        "flex_direction": "column",
        "align_items": "center"
    },
    "elements": [
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "THE DAILY REALITY",
                "header_size": "h6",
                "align": "center",
                "title_color": "#007984",
                "typography_font_size": {"unit": "px", "size": 12},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "Everyday Challenges for Busy Minds",
                "header_size": "h2",
                "align": "center",
                "title_color": "#1F1F1F",
                "typography_font_size": {"unit": "px", "size": 32},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
                "editor": "<p style='text-align: center; color: #475569; font-size: 15px; max-width: 650px;'>Your work is important. But what about your mental well-being?</p>"
            }
        },
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "flex_direction": "row",
                "flex_wrap": "wrap",
                "justify_content": "center",
                "gap": {"unit": "px", "size": 16},
                "margin": {"unit": "px", "top": 30, "right": 0, "bottom": 0, "left": 0}
            },
            "elements": trigger_cards
        }
    ]
}
elements.append(challenges_section)

# =========================================================================
# SECTION 3: SIMPLE SHIFT IN PERSPECTIVE (BARKING DOG)
# =========================================================================
perspective_section = {
    "id": "perspective_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#FFE8DA",
        "padding": {"unit": "px", "top": "70", "right": "20", "bottom": "70", "left": "20"},
        "flex_direction": "column",
        "align_items": "center"
    },
    "elements": [
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "A SIMPLE SHIFT IN PERSPECTIVE",
                "header_size": "h6",
                "align": "center",
                "title_color": "#D36005",
                "typography_font_size": {"unit": "px", "size": 12},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "10 People. 1 Barking Dog.",
                "header_size": "h2",
                "align": "center",
                "title_color": "#1F1F1F",
                "typography_font_size": {"unit": "px", "size": 32},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
                "editor": "<p style='text-align: center; color: #475569; font-size: 15px; max-width: 650px;'>One external trigger. Ten completely different internal reactions. The situation is identical—the response is created inside the mind.</p>"
            }
        },
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "width": {"unit": "%", "size": 95},
                "background_background": "classic",
                "background_color": "#FFFFFF",
                "border_radius": {"unit": "px", "top": 16, "right": 16, "bottom": 16, "left": 16},
                "overflow": "hidden",
                "box_shadow_box_shadow": {"horizontal": 0, "vertical": 8, "blur": 24, "spread": 0, "color": "rgba(15,37,55,0.08)"},
                "margin": {"unit": "px", "top": 24, "right": 0, "bottom": 24, "left": 0}
            },
            "elements": [
                {
                    "id": get_id(),
                    "elType": "widget",
                    "widgetType": "image",
                    "settings": {
                        "image": get_img('barking_dog_new.webp'),
                        "image_size": "full"
                    }
                }
            ]
        }
    ]
}
elements.append(perspective_section)

# =========================================================================
# SECTION 4: THE CORE PHILOSOPHY
# =========================================================================
philosophy_section = {
    "id": "philosophy_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {"unit": "px", "top": "70", "right": "20", "bottom": "70", "left": "20"},
        "flex_direction": "column",
        "align_items": "center"
    },
    "elements": [
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "THE 4-PILLAR MIND-RESET ARC",
                "header_size": "h6",
                "align": "center",
                "title_color": "#007984",
                "typography_font_size": {"unit": "px", "size": 12},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "Not Just Relaxation. A Practical Way to Train Your Mind.",
                "header_size": "h2",
                "align": "center",
                "title_color": "#1F1F1F",
                "typography_font_size": {"unit": "px", "size": 30},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "flex_direction": "row",
                "flex_wrap": "wrap",
                "justify_content": "center",
                "gap": {"unit": "px", "size": 18},
                "margin": {"unit": "px", "top": 30, "right": 0, "bottom": 0, "left": 0}
            },
            "elements": [
                {
                    "id": get_id(),
                    "elType": "container",
                    "isInner": True,
                    "settings": {
                        "width": {"unit": "%", "size": 23},
                        "width_tablet": {"unit": "%", "size": 48},
                        "width_mobile": {"unit": "%", "size": 100},
                        "background_background": "classic",
                        "background_color": "#D2F0FF",
                        "border_radius": {"unit": "px", "top": 12, "right": 12, "bottom": 12, "left": 12},
                        "padding": {"unit": "px", "top": 24, "right": 20, "bottom": 24, "left": 20}
                    },
                    "elements": [
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Step 01", "header_size": "span", "title_color": "#007984", "typography_font_size": {"unit": "px", "size": 12}, "typography_font_weight": "700"}},
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Pause & Settle", "header_size": "h4", "typography_font_size": {"unit": "px", "size": 18}, "typography_font_weight": "700"}},
                        {"id": get_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p style='font-size:13px; color:#475569;'>Disengage from urgent momentum and bring physical awareness to the present moment.</p>"}}
                    ]
                },
                {
                    "id": get_id(),
                    "elType": "container",
                    "isInner": True,
                    "settings": {
                        "width": {"unit": "%", "size": 23},
                        "width_tablet": {"unit": "%", "size": 48},
                        "width_mobile": {"unit": "%", "size": 100},
                        "background_background": "classic",
                        "background_color": "#D2F0FF",
                        "border_radius": {"unit": "px", "top": 12, "right": 12, "bottom": 12, "left": 12},
                        "padding": {"unit": "px", "top": 24, "right": 20, "bottom": 24, "left": 20}
                    },
                    "elements": [
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Step 02", "header_size": "span", "title_color": "#007984", "typography_font_size": {"unit": "px", "size": 12}, "typography_font_weight": "700"}},
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Release & Reset", "header_size": "h4", "typography_font_size": {"unit": "px", "size": 18}, "typography_font_weight": "700"}},
                        {"id": get_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p style='font-size:13px; color:#475569;'>Discharge accumulated neurological stress through breathwork and bilateral movement.</p>"}}
                    ]
                },
                {
                    "id": get_id(),
                    "elType": "container",
                    "isInner": True,
                    "settings": {
                        "width": {"unit": "%", "size": 23},
                        "width_tablet": {"unit": "%", "size": 48},
                        "width_mobile": {"unit": "%", "size": 100},
                        "background_background": "classic",
                        "background_color": "#D2F0FF",
                        "border_radius": {"unit": "px", "top": 12, "right": 12, "bottom": 12, "left": 12},
                        "padding": {"unit": "px", "top": 24, "right": 20, "bottom": 24, "left": 20}
                    },
                    "elements": [
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Step 03", "header_size": "span", "title_color": "#007984", "typography_font_size": {"unit": "px", "size": 12}, "typography_font_weight": "700"}},
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Strengthen & Focus", "header_size": "h4", "typography_font_size": {"unit": "px", "size": 18}, "typography_font_weight": "700"}},
                        {"id": get_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p style='font-size:13px; color:#475569;'>Neurobic coordination exercises that build dual-hemisphere brain connectivity.</p>"}}
                    ]
                },
                {
                    "id": get_id(),
                    "elType": "container",
                    "isInner": True,
                    "settings": {
                        "width": {"unit": "%", "size": 23},
                        "width_tablet": {"unit": "%", "size": 48},
                        "width_mobile": {"unit": "%", "size": 100},
                        "background_background": "classic",
                        "background_color": "#D2F0FF",
                        "border_radius": {"unit": "px", "top": 12, "right": 12, "bottom": 12, "left": 12},
                        "padding": {"unit": "px", "top": 24, "right": 20, "bottom": 24, "left": 20}
                    },
                    "elements": [
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Step 04", "header_size": "span", "title_color": "#007984", "typography_font_size": {"unit": "px", "size": 12}, "typography_font_weight": "700"}},
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Integrate into Life", "header_size": "h4", "typography_font_size": {"unit": "px", "size": 18}, "typography_font_weight": "700"}},
                        {"id": get_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p style='font-size:13px; color:#475569;'>Apply micro-practices during demanding meetings, emails, and transitions.</p>"}}
                    ]
                }
            ]
        }
    ]
}
elements.append(philosophy_section)

# =========================================================================
# SECTION 5: OUR PRACTICES (8 TECHNIQUES WITH INDIAN PROFESSIONALS)
# =========================================================================
practices_data = [
    ("practice_braingym.webp", "Brain Gym & Coordination", "Attention & Alertness", "Bilateral hand and finger drills that activate neural connections between brain hemispheres."),
    ("practice_ambidextrous.webp", "Ambidextrous & Neurobics", "Cognitive Flexibility", "Dual-hand writing and motor drills that stimulate neuroplasticity and mental agility."),
    ("practice_pranayama.webp", "Breathing & Pranayama", "Nervous System Reset", "Rhythmic breath control techniques that balance sympathetic and parasympathetic systems."),
    ("practice_mindfulness.webp", "Mindfulness & Stillness", "Emotional Regulation", "Conscious observational awareness that allows you to respond thoughtfully instead of reacting."),
    ("practice_visualization.webp", "Creative Visualization", "Goal & Stress Resilience", "Guided mental imagery exercises that reinforce cognitive calm, focus, and clear vision."),
    ("practice_eft.webp", "Emotional Awareness & EFT", "Rapid Stress Relief", "Gentle acupressure tapping on meridian points to dissolve anxiety and mental blockage."),
    ("practice_yoganidra.webp", "Yoga Nidra & Relaxation", "Deep Cognitive Rest", "Systematic guided desk-friendly micro-relaxation that resets mental fatigue in 15 minutes."),
    ("practice_awareness.webp", "Everyday Awareness", "Habitual Mindset", "Micro-pauses and mindful checking habits that protect your mental space throughout work.")
]

practice_cards = []
for img_key, title, tag, desc in practices_data:
    practice_cards.append({
        "id": get_id(),
        "elType": "container",
        "isInner": True,
        "settings": {
            "width": {"unit": "%", "size": 23},
            "width_tablet": {"unit": "%", "size": 48},
            "width_mobile": {"unit": "%", "size": 100},
            "background_background": "classic",
            "background_color": "#FFFFFF",
            "border_radius": {"unit": "px", "top": 14, "right": 14, "bottom": 14, "left": 14},
            "box_shadow_box_shadow": {"horizontal": 0, "vertical": 6, "blur": 18, "spread": 0, "color": "rgba(15,37,55,0.06)"},
            "overflow": "hidden"
        },
        "elements": [
            {
                "id": get_id(),
                "elType": "widget",
                "widgetType": "image",
                "settings": {
                    "image": get_img(img_key),
                    "image_size": "full"
                }
            },
            {
                "id": get_id(),
                "elType": "container",
                "isInner": True,
                "settings": {
                    "padding": {"unit": "px", "top": 16, "right": 16, "bottom": 20, "left": 16},
                    "flex_direction": "column",
                    "gap": {"unit": "px", "size": 6}
                },
                "elements": [
                    {
                        "id": get_id(),
                        "elType": "widget",
                        "widgetType": "html",
                        "settings": {
                            "html": f'<span style="display:inline-block; font-size:10px; font-weight:700; text-transform:uppercase; color:#007984; background:#E8F7F9; padding:2px 8px; border-radius:4px; border:1px solid rgba(0,121,132,0.2);">{tag}</span>'
                        }
                    },
                    {
                        "id": get_id(),
                        "elType": "widget",
                        "widgetType": "heading",
                        "settings": {
                            "title": title,
                            "header_size": "h4",
                            "typography_font_size": {"unit": "px", "size": 16},
                            "typography_font_weight": "700",
                            "title_color": "#1F1F1F"
                        }
                    },
                    {
                        "id": get_id(),
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {
                            "editor": f"<p style='font-size:12px; color:#64748B; line-height:1.5; margin:0;'>{desc}</p>"
                        }
                    }
                ]
            }
        ]
    })

practices_section = {
    "id": "practices_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#FFE8DA",
        "padding": {"unit": "px", "top": "70", "right": "20", "bottom": "70", "left": "20"},
        "flex_direction": "column",
        "align_items": "center"
    },
    "elements": [
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "CURRICULUM & TECHNIQUES",
                "header_size": "h6",
                "align": "center",
                "title_color": "#D36005",
                "typography_font_size": {"unit": "px", "size": 12},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "Our Practices",
                "header_size": "h2",
                "align": "center",
                "title_color": "#1F1F1F",
                "typography_font_size": {"unit": "px", "size": 32},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
                "editor": "<p style='text-align: center; color: #475569; font-size: 15px; max-width: 650px;'>Simple, repeatable mind-wellness practices designed for desk workers, busy professionals, and leaders.</p>"
            }
        },
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "flex_direction": "row",
                "flex_wrap": "wrap",
                "justify_content": "center",
                "gap": {"unit": "px", "size": 18},
                "margin": {"unit": "px", "top": 30, "right": 0, "bottom": 0, "left": 0}
            },
            "elements": practice_cards
        }
    ]
}
elements.append(practices_section)

# =========================================================================
# SECTION 7: CORPORATE WORKSHOPS & BENEFITS (SIGNATURE TEAL #007984)
# =========================================================================
corporate_section = {
    "id": "corporate_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#007984",
        "padding": {"unit": "px", "top": "70", "right": "20", "bottom": "70", "left": "20"},
        "flex_direction": "column",
        "align_items": "center"
    },
    "elements": [
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "CORPORATE WELLNESS PROGRAMS",
                "header_size": "h6",
                "align": "center",
                "title_color": "#FFE8DA",
                "typography_font_size": {"unit": "px", "size": 12},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "Bring Brain Yoga to Your Workplace",
                "header_size": "h2",
                "align": "center",
                "title_color": "#FFFFFF",
                "typography_font_size": {"unit": "px", "size": 32},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
                "editor": "<p style='text-align: center; color: #D2F0FF; font-size: 15px; max-width: 650px;'>Empower your teams with actionable tools to reduce burnout, elevate concentration, and boost collective morale.</p>"
            }
        },
        # Two Workshop Photo Cards
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "flex_direction": "row",
                "flex_wrap": "wrap",
                "justify_content": "center",
                "gap": {"unit": "px", "size": 24},
                "margin": {"unit": "px", "top": 30, "right": 0, "bottom": 30, "left": 0}
            },
            "elements": [
                {
                    "id": get_id(),
                    "elType": "container",
                    "isInner": True,
                    "settings": {
                        "width": {"unit": "%", "size": 48},
                        "width_mobile": {"unit": "%", "size": 100},
                        "background_background": "classic",
                        "background_color": "#FFFFFF",
                        "border_radius": {"unit": "px", "top": 14, "right": 14, "bottom": 14, "left": 14},
                        "overflow": "hidden"
                    },
                    "elements": [
                        {"id": get_id(), "elType": "widget", "widgetType": "image", "settings": {"image": get_img('workshop_corporate_team.webp'), "image_size": "full"}},
                        {
                            "id": get_id(),
                            "elType": "container",
                            "isInner": True,
                            "settings": {"padding": {"unit": "px", "top": 20, "right": 20, "bottom": 20, "left": 20}},
                            "elements": [
                                {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Interactive Hands-on Exercises", "header_size": "h4", "typography_font_size": {"unit": "px", "size": 18}, "typography_font_weight": "700"}},
                                {"id": get_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p style='font-size:13px; color:#475569;'>Energizing team breaks that improve focus, reduce screen fatigue, and boost group dynamics.</p>"}}
                            ]
                        }
                    ]
                },
                {
                    "id": get_id(),
                    "elType": "container",
                    "isInner": True,
                    "settings": {
                        "width": {"unit": "%", "size": 48},
                        "width_mobile": {"unit": "%", "size": 100},
                        "background_background": "classic",
                        "background_color": "#FFFFFF",
                        "border_radius": {"unit": "px", "top": 14, "right": 14, "bottom": 14, "left": 14},
                        "overflow": "hidden"
                    },
                    "elements": [
                        {"id": get_id(), "elType": "widget", "widgetType": "image", "settings": {"image": get_img('workshop_corporate_chair.webp'), "image_size": "full"}},
                        {
                            "id": get_id(),
                            "elType": "container",
                            "isInner": True,
                            "settings": {"padding": {"unit": "px", "top": 20, "right": 20, "bottom": 20, "left": 20}},
                            "elements": [
                                {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Chair & Desk Ergonomic Reset", "header_size": "h4", "typography_font_size": {"unit": "px", "size": 18}, "typography_font_weight": "700"}},
                                {"id": get_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p style='font-size:13px; color:#475569;'>Zero gym wear or mats needed. Every drill is performed seated at desk workstations.</p>"}}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
elements.append(corporate_section)

# =========================================================================
# SECTION 9: TRAINER PROFILE
# =========================================================================
trainer_section = {
    "id": "trainer_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#FFE8DA",
        "padding": {"unit": "px", "top": "70", "right": "20", "bottom": "70", "left": "20"},
        "flex_direction": "row",
        "flex_wrap": "wrap",
        "justify_content": "space-between",
        "align_items": "center"
    },
    "elements": [
        # Photo
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "width": {"unit": "%", "size": 38},
                "width_mobile": {"unit": "%", "size": 100},
                "background_background": "classic",
                "background_color": "#FFFFFF",
                "border_radius": {"unit": "px", "top": 16, "right": 16, "bottom": 16, "left": 16},
                "box_shadow_box_shadow": {"horizontal": 0, "vertical": 10, "blur": 26, "spread": 0, "color": "rgba(15,37,55,0.08)"},
                "overflow": "hidden"
            },
            "elements": [
                {
                    "id": get_id(),
                    "elType": "widget",
                    "widgetType": "image",
                    "settings": {
                        "image": get_img('trainer_rajendra_portrait.jpg'),
                        "image_size": "full"
                    }
                },
                {
                    "id": get_id(),
                    "elType": "container",
                    "isInner": True,
                    "settings": {"padding": {"unit": "px", "top": 16, "right": 16, "bottom": 16, "left": 16}, "align_items": "center"},
                    "elements": [
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Rajendra Boddu", "header_size": "h3", "align": "center", "typography_font_size": {"unit": "px", "size": 20}, "typography_font_weight": "700"}},
                        {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "Founder & Lead Brain Yoga Facilitator", "header_size": "p", "align": "center", "title_color": "#007984", "typography_font_size": {"unit": "px", "size": 13}}}
                    ]
                }
            ]
        },
        # Bio
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "width": {"unit": "%", "size": 58},
                "width_mobile": {"unit": "%", "size": 100},
                "flex_direction": "column",
                "gap": {"unit": "px", "size": 14}
            },
            "elements": [
                {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "MEET YOUR TRAINER", "header_size": "h6", "title_color": "#D36005", "typography_font_size": {"unit": "px", "size": 12}, "typography_font_weight": "700"}},
                {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": "From 15 Years in the IT Industry to Mind-Wellness Facilitator", "header_size": "h2", "title_color": "#1F1F1F", "typography_font_size": {"unit": "px", "size": 28}, "typography_font_weight": "700"}},
                {"id": get_id(), "elType": "widget", "widgetType": "text-editor", "settings": {"editor": "<p style='font-size:14px; line-height:1.65; color:#334155;'>Rajendra Boddu spent over 15 years in demanding IT corporate environments. Having experienced firsthand the pressures, back-to-back delivery deadlines, and cognitive exhaustion that professionals navigate daily, he transitioned to mind-wellness and yoga therapy.</p><p style='font-size:14px; line-height:1.65; color:#334155;'>He synthesized classical breathwork, neurobic science, bilateral coordination, and mindfulness into <strong>Brain Yoga</strong>—a zero-friction methodology tailored for working adults.</p>"}},
                {
                    "id": get_id(),
                    "elType": "widget",
                    "widgetType": "button",
                    "settings": {
                        "text": "Connect with Rajendra on WhatsApp",
                        "link": {"url": "https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20I%20would%20like%20to%20connect%20with%20you%20regarding%20Brain%20Yoga."},
                        "background_color": "#FD8742",
                        "button_text_color": "#FFFFFF",
                        "typography_font_weight": "600",
                        "border_radius": {"unit": "px", "top": 10, "right": 10, "bottom": 10, "left": 10}
                    }
                }
            ]
        }
    ]
}
elements.append(trainer_section)

# =========================================================================
# SECTION 10: TESTIMONIALS (SIGNATURE TEAL)
# =========================================================================
testimonials_data = [
    ("testimonial_uma.jpg", "Uma Maheswari", "IT Project Manager, Hyderabad", "With tight sprint deadlines, brain fog used to set in by 3 PM. These 5-minute Brain Gym coordination drills give me instant mental clarity without caffeine."),
    ("testimonial_aryan.jpg", "Aryan Verma", "Senior Software Engineer, Bengaluru", "The breathing and eye relaxation techniques made a visible difference in my focus and reduced my evening screen fatigue drastically."),
    ("testimonial_kavitha.jpg", "Kavitha", "HR Business Partner, Hyderabad", "We hosted a corporate workshop for 85 team members. The feedback was overwhelmingly positive—practical, zero athletic demands, and highly engaging."),
    ("testimonial_sravani.jpg", "Sravani", "Chartered Accountant, Hyderabad", "Tax season used to trigger intense neck stiffness and shallow breathing. The desk pranayama exercises are a game-changer."),
    ("testimonial_vinay.jpg", "Vinay Kumar", "Startup Founder, Hyderabad", "The barking dog mindset framework helped me pause during investor negotiations instead of impulsively reacting. Life-changing perspective."),
    ("testimonial_kiran.jpg", "Kiran Reddy", "Operations Lead, Cyberabad", "Simple, repeatable, and science-backed. Rajendra's IT background means he actually understands corporate pressure.")
]

testimonial_cards = []
for img_key, name, role, quote in testimonials_data:
    testimonial_cards.append({
        "id": get_id(),
        "elType": "container",
        "isInner": True,
        "settings": {
            "width": {"unit": "%", "size": 31},
            "width_tablet": {"unit": "%", "size": 48},
            "width_mobile": {"unit": "%", "size": 100},
            "background_background": "classic",
            "background_color": "#FFFFFF",
            "border_radius": {"unit": "px", "top": 14, "right": 14, "bottom": 14, "left": 14},
            "padding": {"unit": "px", "top": 20, "right": 20, "bottom": 20, "left": 20},
            "flex_direction": "column",
            "justify_content": "space-between",
            "gap": {"unit": "px", "size": 14}
        },
        "elements": [
            {
                "id": get_id(),
                "elType": "widget",
                "widgetType": "text-editor",
                "settings": {
                    "editor": f"<p style='font-size:13px; font-style:italic; color:#334155; line-height:1.6;'>\"{quote}\"</p>"
                }
            },
            {
                "id": get_id(),
                "elType": "container",
                "isInner": True,
                "settings": {
                    "flex_direction": "row",
                    "align_items": "center",
                    "gap": {"unit": "px", "size": 12},
                    "border_border": "solid",
                    "border_width": {"unit": "px", "top": 1, "right": 0, "bottom": 0, "left": 0},
                    "border_color": "#F1F5F9",
                    "padding": {"unit": "px", "top": 12, "right": 0, "bottom": 0, "left": 0}
                },
                "elements": [
                    {
                        "id": get_id(),
                        "elType": "widget",
                        "widgetType": "image",
                        "settings": {
                            "image": get_img(img_key),
                            "image_size": "thumbnail",
                            "width": {"unit": "px", "size": 44},
                            "height": {"unit": "px", "size": 44},
                            "border_radius": {"unit": "px", "top": 999, "right": 999, "bottom": 999, "left": 999}
                        }
                    },
                    {
                        "id": get_id(),
                        "elType": "container",
                        "isInner": True,
                        "settings": {"flex_direction": "column"},
                        "elements": [
                            {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": name, "header_size": "h4", "typography_font_size": {"unit": "px", "size": 14}, "typography_font_weight": "700", "title_color": "#1F1F1F"}},
                            {"id": get_id(), "elType": "widget", "widgetType": "heading", "settings": {"title": role, "header_size": "p", "typography_font_size": {"unit": "px", "size": 11}, "title_color": "#64748B"}}
                        ]
                    }
                ]
            }
        ]
    })

testimonials_section = {
    "id": "testimonials_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#007984",
        "padding": {"unit": "px", "top": "70", "right": "20", "bottom": "70", "left": "20"},
        "flex_direction": "column",
        "align_items": "center"
    },
    "elements": [
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "EXPERIENCES",
                "header_size": "h6",
                "align": "center",
                "title_color": "#FFE8DA",
                "typography_font_size": {"unit": "px", "size": 12},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "What Working Professionals Say",
                "header_size": "h2",
                "align": "center",
                "title_color": "#FFFFFF",
                "typography_font_size": {"unit": "px", "size": 32},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "flex_direction": "row",
                "flex_wrap": "wrap",
                "justify_content": "center",
                "gap": {"unit": "px", "size": 18},
                "margin": {"unit": "px", "top": 30, "right": 0, "bottom": 0, "left": 0}
            },
            "elements": testimonial_cards
        }
    ]
}
elements.append(testimonials_section)

# =========================================================================
# SECTION 11: FAQS (ACCORDION WIDGET)
# =========================================================================
faq_tabs = [
    {
        "_id": get_id(),
        "tab_title": "Do I need any prior yoga experience or physical flexibility?",
        "tab_content": "No prior experience or flexibility is required! Brain Yoga focuses on gentle bilateral coordination drills, neurobic finger movements, eye relaxation, and desk-friendly breathwork that anyone can perform while comfortably seated."
    },
    {
        "_id": get_id(),
        "tab_title": "Do we need yoga mats or athletic gym clothes?",
        "tab_content": "No! Brain Yoga for Busy Minds requires zero gym wear or mats. All neurobic movements, eye exercises, and breathwork are performed while comfortably seated on an office chair in regular formal or casual work clothes."
    },
    {
        "_id": get_id(),
        "tab_title": "How much time do these practices take on a busy workday?",
        "tab_content": "Each individual technique takes just 3 to 5 minutes. You can practice them during natural workday transitions—between meetings, before opening an email sprint, or when taking a quick break."
    },
    {
        "_id": get_id(),
        "tab_title": "Can sessions be organized for our remote/hybrid corporate team?",
        "tab_content": "Yes, absolutely! We host live, highly engaging virtual workshops via Zoom or Microsoft Teams with cameras on, interactive polls, and real-time guidance. In-person corporate campus workshops are also available across Hyderabad and other cities."
    },
    {
        "_id": get_id(),
        "tab_title": "How is Brain Yoga different from regular meditation apps?",
        "tab_content": "Meditation apps often ask an already exhausted mind to sit in silent concentration. Brain Yoga uses bilateral movement, neurobics, and EFT tapping to actively engage the nervous system first, making mental calm natural and effortless."
    },
    {
        "_id": get_id(),
        "tab_title": "How soon can our company schedule a corporate session?",
        "tab_content": "We can typically schedule corporate workshops with 3 to 5 business days advance notice to customize the curriculum around your team's specific pain points and timings."
    }
]

faq_section = {
    "id": "faq_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "padding": {"unit": "px", "top": "70", "right": "20", "bottom": "70", "left": "20"},
        "flex_direction": "column",
        "align_items": "center"
    },
    "elements": [
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "QUESTIONS & CLARIFICATIONS",
                "header_size": "h6",
                "align": "center",
                "title_color": "#007984",
                "typography_font_size": {"unit": "px", "size": 12},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "Frequently Asked Questions",
                "header_size": "h2",
                "align": "center",
                "title_color": "#1F1F1F",
                "typography_font_size": {"unit": "px", "size": 32},
                "typography_font_weight": "700"
            }
        },
        {
            "id": get_id(),
            "elType": "container",
            "isInner": True,
            "settings": {
                "width": {"unit": "%", "size": 75},
                "width_mobile": {"unit": "%", "size": 100},
                "margin": {"unit": "px", "top": 24, "right": 0, "bottom": 0, "left": 0}
            },
            "elements": [
                {
                    "id": get_id(),
                    "elType": "widget",
                    "widgetType": "accordion",
                    "settings": {
                        "tabs": faq_tabs,
                        "title_color": "#1F1F1F",
                        "tab_active_color": "#007984",
                        "title_background": "#F8FAFC",
                        "content_background_color": "#FFFFFF"
                    }
                }
            ]
        }
    ]
}
elements.append(faq_section)

# =========================================================================
# SECTION 12: FINAL CTA & FOOTER
# =========================================================================
footer_section = {
    "id": "footer_section",
    "elType": "container",
    "isInner": False,
    "settings": {
        "content_width": "boxed",
        "background_background": "classic",
        "background_color": "#FFFFFF",
        "border_border": "solid",
        "border_width": {"unit": "px", "top": 1, "right": 0, "bottom": 0, "left": 0},
        "border_color": "#E2E8F0",
        "padding": {"unit": "px", "top": "50", "right": "20", "bottom": "30", "left": "20"},
        "flex_direction": "column",
        "align_items": "center",
        "gap": {"unit": "px", "size": 16}
    },
    "elements": [
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "image",
            "settings": {
                "image": get_img('official_logo.png'),
                "image_size": "medium",
                "width": {"unit": "px", "size": 180}
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "text-editor",
            "settings": {
                "editor": "<p style='text-align:center; color:#64748B; font-size:13px; max-width:500px;'>Brain Yoga Academy, Hyderabad, India.<br>WhatsApp: +91 83319 29240 | Email: rajendraboddu@gmail.com</p>"
            }
        },
        {
            "id": get_id(),
            "elType": "widget",
            "widgetType": "heading",
            "settings": {
                "title": "© 2026 Brain Yoga Academy. All Rights Reserved.",
                "header_size": "p",
                "align": "center",
                "title_color": "#94A3B8",
                "typography_font_size": {"unit": "px", "size": 12}
            }
        }
    ]
}
elements.append(footer_section)

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


# Save JSON file
out_path = '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain_yoga_elementor_native_template.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({
        "version": "0.4",
        "title": "Brain Yoga for Busy Minds - Elementor Native Template",
        "type": "page",
        "content": elements
    }, f, indent=2)

print(f"Generated {out_path} with {len(elements)} root sections/containers!")
