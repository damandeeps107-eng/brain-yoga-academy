import re

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS in <style>
old_css_pattern = r'/\* Bulletproof Header & Logo Constraints.*?\*/\s*header \{.*?\}(?:\s*header img.*?\})?(?:\s*footer img.*?\})?'
new_css = """/* Bulletproof Header & Logo Constraints across all devices */
        header {
            position: sticky !important;
            top: 0 !important;
            z-index: 99999 !important;
            background-color: rgba(255, 255, 255, 0.98) !important;
            backdrop-filter: blur(8px) !important;
            border-bottom: 1px solid #E2E8F0 !important;
            width: 100% !important;
            max-width: 100vw !important;
        }
        .by-brand-logo {
            height: 36px !important;
            max-height: 36px !important;
            width: auto !important;
            max-width: 205px !important;
            object-fit: contain !important;
            display: block !important;
        }
        @media (max-width: 640px) {
            .by-brand-logo {
                height: 28px !important;
                max-height: 28px !important;
                max-width: 155px !important;
            }
        }
        footer img, footer a img {
            height: 42px !important;
            max-height: 42px !important;
            width: auto !important;
            max-width: 230px !important;
            object-fit: contain !important;
            display: inline-block !important;
        }"""

html = re.sub(r'/\* Bulletproof Header & Logo Constraints.*?footer img, footer a img \{[^}]*\}', new_css, html, flags=re.DOTALL)

# 2. Update Top Announcement Bar and Header HTML
old_header_pattern = r'<!-- ===+ -->\s*<!-- TOP ANNOUNCEMENT BAR.*?<!-- ===+ -->\s*<!-- SECTION 1: HERO'
new_header_html = """<!-- ========================================================================= -->
    <!-- TOP ANNOUNCEMENT BAR: BRAIN YOGA FOR CHILDREN LINK                        -->
    <!-- ========================================================================= -->
    <aside aria-label="Program Announcement" class="bg-[#007984] py-2 px-3 sm:px-4 text-center text-xs font-semibold text-white shadow-xs">
        <div class="max-w-7xl mx-auto flex items-center justify-center gap-1.5 sm:gap-2 flex-wrap text-center leading-tight">
            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold uppercase bg-brandOrange text-white whitespace-nowrap">
                Child Wellness
            </span>
            <span class="text-[11px] sm:text-xs">Looking for our proven memory & concentration training for kids?</span>
            <a href="https://brainyogaacademy.com/" class="inline-flex items-center gap-1 font-bold text-[#FFE8DA] hover:text-white hover:underline transition-colors whitespace-nowrap text-[11px] sm:text-xs">
                <span>Visit Brain Yoga For Children</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </a>
        </div>
    </aside>

    <!-- ========================================================================= -->
    <!-- TOP STICKY NAVBAR (Bulletproof Responsive: Desktop, Laptop, Tablet, Mobile)-->
    <!-- ========================================================================= -->
    <header class="sticky top-0 z-50 w-full bg-white/98 backdrop-blur-md border-b border-slate-200 shadow-xs transition-all">
        <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8 h-16 lg:h-20 flex items-center justify-between gap-2 sm:gap-4">
            
            <!-- Official Brand Logo -->
            <a href="https://brainyogaacademy.com/brain-yoga-for-busy-minds/" class="flex items-center gap-2 sm:gap-2.5 flex-shrink-0 no-underline" style="display: flex !important; align-items: center !important; text-decoration: none !important;">
                <img decoding="async" src="https://brainyogaacademy.com/wp-content/uploads/2026/11/official_logo.png" alt="Brain Yoga Academy" class="by-brand-logo" style="height: 36px !important; width: auto !important; max-width: 205px !important; object-fit: contain !important; display: block !important;">
                <span class="hidden sm:inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2 py-0.5 rounded-md border border-brandTeal/20 whitespace-nowrap">
                    For Busy Minds
                </span>
            </a>

            <!-- Desktop Navigation Links (Responsive xl:flex with clean spacing) -->
            <nav class="hidden xl:flex items-center gap-2.5 2xl:gap-5 text-xs 2xl:text-sm font-semibold text-slate-700 whitespace-nowrap">
                <a href="#challenges" class="hover:text-brandTeal transition-colors">Everyday Challenges</a>
                <a href="#shift" class="hover:text-brandTeal transition-colors">Shift in Perspective</a>
                <a href="#about" class="hover:text-brandTeal transition-colors">About</a>
                <a href="#practices" class="hover:text-brandTeal transition-colors">Our Practices</a>
                <a href="#benefits" class="hover:text-brandTeal transition-colors">Gains</a>
                <a href="#corporate" class="hover:text-brandTeal transition-colors text-brandTeal font-bold">Corporate</a>
                <a href="#trainer" class="hover:text-brandTeal transition-colors">Trainer</a>
                <a href="#testimonials" class="hover:text-brandTeal transition-colors">Testimonials</a>
                <a href="#faq" class="hover:text-brandTeal transition-colors">FAQ</a>
            </nav>

            <!-- Header Action CTAs -->
            <div class="flex items-center gap-1.5 sm:gap-3 flex-shrink-0">
                <a href="https://brainyogaacademy.com/" class="hidden 2xl:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-brandPeachLight hover:bg-brandPeachBg text-brandOrangeDark text-xs font-bold border border-brandOrange/20 transition-all">
                    <span>Kids Yoga</span>
                    <i data-lucide="arrow-up-right" class="w-3.5 h-3.5"></i>
                </a>

                <button onclick="openModal('individualModal')" class="by-btn-primary !py-2 !px-2.5 sm:!px-4 !text-xs sm:!text-sm flex items-center gap-1.5 whitespace-nowrap">
                    <i data-lucide="calendar" class="w-3.5 h-3.5 sm:w-4 sm:h-4"></i>
                    <span class="hidden sm:inline">Book FREE Session</span>
                    <span class="sm:hidden">Book Free</span>
                </button>

                <!-- Mobile & Tablet Hamburger Button (Visible on < 1280px) -->
                <button type="button" id="mobileMenuToggle" aria-label="Toggle navigation menu" class="xl:hidden w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 flex items-center justify-center transition-all flex-shrink-0">
                    <i data-lucide="menu" id="menuIcon" class="w-4 h-4 sm:w-5 sm:h-5"></i>
                </button>
            </div>
        </div>

        <!-- Mobile & Tablet Drawer Menu (Full Scrollable, Clean) -->
        <div id="mobileDrawerMenu" class="hidden xl:hidden border-t border-slate-200 bg-white px-5 py-5 space-y-3 shadow-2xl max-h-[80vh] overflow-y-auto">
            <nav class="flex flex-col space-y-2 text-sm font-semibold text-slate-800">
                <a href="#challenges" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Everyday Challenges <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#shift" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Shift in Perspective <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#about" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">About Program <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#practices" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Our Practices <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#benefits" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">What Regular Practice Can Build <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#how-it-works" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">How the Program Works <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#corporate" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between text-brandTeal font-bold">Corporate Workshops <i data-lucide="chevron-right" class="w-4 h-4 text-brandTeal"></i></a>
                <a href="#trainer" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Meet Trainer (Rajendra Boddu) <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#testimonials" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Testimonials <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#faq" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">FAQs <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="https://brainyogaacademy.com/" class="mobile-nav-link py-2 text-brandOrangeDark font-bold flex items-center justify-between">Brain Yoga For Children →</a>
            </nav>
            <div class="pt-3 flex flex-col gap-2.5">
                <button onclick="openModal('individualModal'); closeMobileMenu();" class="w-full py-3 rounded-lg bg-brandOrange hover:bg-brandOrangeDark text-white font-bold text-center text-sm shadow-md">
                    Book a FREE Introductory Session
                </button>
                <button onclick="openModal('corporateModal'); closeMobileMenu();" class="w-full py-3 rounded-lg bg-brandTeal hover:bg-brandTealDark text-white font-bold text-center text-sm shadow-md">
                    Enquire About Corporate Workshops
                </button>
            </div>
        </div>
    </header>

    <!-- ========================================================================= -->
    <!-- SECTION 1: HERO"""

html = re.sub(old_header_pattern, new_header_html, html, flags=re.DOTALL)

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated busy-minds.html, brain-yoga-for-busy-minds.html, and index.html!")
