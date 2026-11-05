import re

CSS_ANIMATIONS = '''
        /* ========================================================================= */
        /* SILKY SMOOTH ANIMATIONS & MICRO-INTERACTIONS                              */
        /* ========================================================================= */

        /* Hero Entrance Keyframes */
        @keyframes heroFadeDown {
            from {
                opacity: 0;
                transform: translate3d(0, -22px, 0);
            }
            to {
                opacity: 1;
                transform: translate3d(0, 0, 0);
            }
        }

        @keyframes heroFadeUp {
            from {
                opacity: 0;
                transform: translate3d(0, 32px, 0);
            }
            to {
                opacity: 1;
                transform: translate3d(0, 0, 0);
            }
        }

        @keyframes heroCardIn {
            from {
                opacity: 0;
                transform: translate3d(36px, 18px, 0) scale(0.96);
            }
            to {
                opacity: 1;
                transform: translate3d(0, 0, 0) scale(1);
            }
        }

        @keyframes floatSubtle {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-6px);
            }
        }

        /* Hero Staggered Animation Classes */
        .anim-hero-eyebrow {
            animation: heroFadeDown 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.05s both;
        }
        .anim-hero-title {
            animation: heroFadeUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.18s both;
        }
        .anim-hero-sub {
            animation: heroFadeUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.32s both;
        }
        .anim-hero-cta {
            animation: heroFadeUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.46s both;
        }
        .anim-hero-badges {
            animation: heroFadeUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.60s both;
        }
        .anim-hero-card {
            animation: heroCardIn 0.95s cubic-bezier(0.16, 1, 0.3, 1) 0.25s both;
        }

        /* Subtle Gentle Card Float */
        .hero-float-subtle {
            animation: floatSubtle 6s ease-in-out 1.2s infinite;
        }

        /* Scroll-Triggered Reveal Animations */
        .reveal-on-scroll {
            opacity: 0;
            transform: translate3d(0, 30px, 0);
            transition: opacity 0.75s cubic-bezier(0.16, 1, 0.3, 1), transform 0.75s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: opacity, transform;
        }
        .reveal-on-scroll.is-revealed {
            opacity: 1;
            transform: translate3d(0, 0, 0);
        }

        /* Grid Stagger Cascades */
        .stagger-grid > * {
            opacity: 0;
            transform: translate3d(0, 32px, 0);
            transition: opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
            will-change: opacity, transform;
        }
        .stagger-grid.is-revealed > *:nth-child(1) { transition-delay: 0.04s; }
        .stagger-grid.is-revealed > *:nth-child(2) { transition-delay: 0.10s; }
        .stagger-grid.is-revealed > *:nth-child(3) { transition-delay: 0.16s; }
        .stagger-grid.is-revealed > *:nth-child(4) { transition-delay: 0.22s; }
        .stagger-grid.is-revealed > *:nth-child(5) { transition-delay: 0.28s; }
        .stagger-grid.is-revealed > *:nth-child(6) { transition-delay: 0.34s; }
        .stagger-grid.is-revealed > *:nth-child(7) { transition-delay: 0.40s; }
        .stagger-grid.is-revealed > *:nth-child(8) { transition-delay: 0.46s; }
        .stagger-grid.is-revealed > *:nth-child(9) { transition-delay: 0.52s; }
        .stagger-grid.is-revealed > *:nth-child(10) { transition-delay: 0.58s; }

        .stagger-grid.is-revealed > * {
            opacity: 1;
            transform: translate3d(0, 0, 0);
        }

        /* Silky Smooth Card Transitions & Hover Dynamics */
        .by-card {
            transition: transform 0.32s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.32s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s ease;
        }
        .by-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 16px 36px -4px rgba(0, 121, 132, 0.14);
            border-color: #007984;
        }

        /* Image Micro-Zoom inside cards */
        .by-card-zoom img {
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .by-card-zoom:hover img {
            transform: scale(1.04);
        }

        /* Interactive Button Micro-Press States */
        .by-btn-primary {
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease, box-shadow 0.2s ease;
        }
        .by-btn-primary:active {
            transform: scale(0.97) translateY(0);
        }
        .by-btn-secondary {
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease, border-color 0.2s ease;
        }
        .by-btn-secondary:active {
            transform: scale(0.97);
        }

        /* Safe fallback for users who prefer reduced motion */
        @media (prefers-reduced-motion: reduce) {
            *, ::before, ::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
                scroll-behavior: auto !important;
            }
            .reveal-on-scroll, .stagger-grid > * {
                opacity: 1 !important;
                transform: none !important;
            }
        }
'''

JS_OBSERVER = '''
        // =========================================================================
        // SILKY SMOOTH SCROLL REVEAL OBSERVER (Native IntersectionObserver)
        // =========================================================================
        (function() {
            if ('IntersectionObserver' in window) {
                const observerOptions = {
                    root: null,
                    rootMargin: '0px 0px -40px 0px',
                    threshold: 0.08
                };

                const revealObserver = new IntersectionObserver((entries, observer) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('is-revealed');
                            observer.unobserve(entry.target);
                        }
                    });
                }, observerOptions);

                // Observe all elements targeted for reveal
                document.querySelectorAll('.reveal-on-scroll, .stagger-grid').forEach(el => {
                    revealObserver.observe(el);
                });
            } else {
                // Graceful fallback for legacy browsers: reveal everything immediately
                document.querySelectorAll('.reveal-on-scroll, .stagger-grid').forEach(el => {
                    el.classList.add('is-revealed');
                });
            }
        })();
'''

def enhance_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject CSS Animations into <style> if not already present
    if '/* SILKY SMOOTH ANIMATIONS & MICRO-INTERACTIONS' not in html:
        html = html.replace('</style>', CSS_ANIMATIONS + '\n    </style>', 1)
        print(f"[{filepath}] Injected CSS animations")

    # 2. Add Hero animation classes
    # Eyebrow wrapper
    html = re.sub(
        r'<div class="flex flex-wrap items-center gap-2">(\s*<div class="inline-flex items-center gap-1\.5 bg-brandTealLight)',
        r'<div class="anim-hero-eyebrow flex flex-wrap items-center gap-2">\1',
        html
    )

    # Headline
    html = html.replace(
        '<h1 class="font-heading text-2xl sm:text-4xl lg:text-5xl font-extrabold text-brandDark tracking-tight leading-[1.25]">',
        '<h1 class="anim-hero-title font-heading text-2xl sm:text-4xl lg:text-5xl font-extrabold text-brandDark tracking-tight leading-[1.25]">'
    )

    # Subheading & description
    html = re.sub(
        r'(<p class="text-sm sm:text-base md:text-lg text-slate-700 leading-relaxed font-normal max-w-2xl">)',
        r'<div class="anim-hero-sub space-y-3">\1',
        html
    )
    # Close the div before CTAs
    html = re.sub(
        r'(</p>\s*)(<!-- CTAs)',
        r'\1</div>\n\n                    \2',
        html
    )

    # CTAs
    html = html.replace(
        '<div class="pt-1 flex flex-col sm:flex-row items-stretch sm:items-center gap-3">',
        '<div class="anim-hero-cta pt-1 flex flex-col sm:flex-row items-stretch sm:items-center gap-3">'
    )

    # Trust badges
    html = html.replace(
        '<div class="pt-1 flex flex-wrap items-center gap-x-4 gap-y-2 text-xs font-semibold text-slate-600">',
        '<div class="anim-hero-badges pt-1 flex flex-wrap items-center gap-x-4 gap-y-2 text-xs font-semibold text-slate-600">'
    )

    # Hero Card (Right column)
    html = html.replace(
        '<div class="by-card max-w-sm sm:max-w-md mx-auto w-full overflow-hidden shadow-lg border border-slate-200/80 bg-white">',
        '<div class="anim-hero-card hero-float-subtle by-card max-w-sm sm:max-w-md mx-auto w-full overflow-hidden shadow-lg border border-slate-200/80 bg-white">'
    )

    # 3. Add scroll reveal and stagger classes to sections and grids
    # Everyday Challenges (#challenges)
    html = html.replace(
        '<div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">',
        '<div class="reveal-on-scroll text-center max-w-3xl mx-auto mb-12 sm:mb-16">'
    )
    html = html.replace(
        '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">',
        '<div class="stagger-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">'
    )

    # Shift / Mindset (#mindset)
    html = html.replace(
        '<div class="text-center max-w-3xl mx-auto mb-10 sm:mb-14">',
        '<div class="reveal-on-scroll text-center max-w-3xl mx-auto mb-10 sm:mb-14">'
    )
    html = html.replace(
        '<div class="by-card mb-10 overflow-hidden">',
        '<div class="reveal-on-scroll by-card mb-10 overflow-hidden">'
    )
    html = html.replace(
        '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch">',
        '<div class="stagger-grid grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch">'
    )

    # Core Philosophy (#philosophy)
    html = html.replace(
        '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">',
        '<div class="stagger-grid grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">'
    )

    # Practices (#practices)
    # Give cards by-card-zoom class for smooth image zoom on hover
    html = html.replace(
        'by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70',
        'by-card by-card-zoom flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70'
    )

    # How It Works (#how-it-works)
    html = html.replace(
        '<div class="grid grid-cols-1 md:grid-cols-3 gap-8">',
        '<div class="stagger-grid grid grid-cols-1 md:grid-cols-3 gap-8">'
    )

    # Corporate Workshops (#corporate)
    html = html.replace(
        '<div class="grid grid-cols-1 lg:grid-cols-2 gap-8">',
        '<div class="stagger-grid grid grid-cols-1 lg:grid-cols-2 gap-8">'
    )

    # Benefits (#benefits)
    html = html.replace(
        '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">',
        '<div class="stagger-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
    )

    # Testimonials (#testimonials)
    html = html.replace(
        '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">',
        '<div class="stagger-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
    )

    # Trainer Profile (#trainer)
    html = html.replace(
        '<div class="lg:col-span-5 flex flex-col items-center">',
        '<div class="reveal-on-scroll lg:col-span-5 flex flex-col items-center">'
    )
    html = html.replace(
        '<div class="lg:col-span-7 space-y-6">',
        '<div class="reveal-on-scroll lg:col-span-7 space-y-6">'
    )

    # FAQ (#faq)
    html = html.replace(
        '<div class="max-w-3xl mx-auto space-y-4">',
        '<div class="reveal-on-scroll max-w-3xl mx-auto space-y-4">'
    )

    # Contact / Final CTA (#contact)
    html = html.replace(
        '<div class="by-card bg-white p-8 sm:p-12 border border-orange-200/80 shadow-xl max-w-4xl mx-auto text-center relative overflow-hidden">',
        '<div class="reveal-on-scroll by-card bg-white p-8 sm:p-12 border border-orange-200/80 shadow-xl max-w-4xl mx-auto text-center relative overflow-hidden">'
    )

    # 4. Inject JS Observer script before </script> at the bottom
    if '// SILKY SMOOTH SCROLL REVEAL OBSERVER' not in html:
        # inject inside the main script tag
        html = html.replace('// WhatsApp Form Handlers', JS_OBSERVER + '\n        // WhatsApp Form Handlers')
        print(f"[{filepath}] Injected JS scroll reveal observer")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[{filepath}] Saved successfully!")

if __name__ == '__main__':
    files = [
        "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html",
        "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html",
        "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html",
        "/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html"
    ]
    for fp in files:
        enhance_html(fp)
