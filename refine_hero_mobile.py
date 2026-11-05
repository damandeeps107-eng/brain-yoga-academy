# Script to refine Hero section for mobile responsiveness and eliminate overcrowding
import os

files = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html'
]

refined_hero_html = """    <!-- ========================================================================= -->
    <!-- SECTION 1: HERO (Top of page) — Background: Warm Peach #FFF3EB            -->
    <!-- Mobile-Refined & Uncluttered: Balanced Spacing, No Overcrowding            -->
    <!-- ========================================================================= -->
    <section id="hero" class="relative bg-brandPeachBg pt-6 pb-12 sm:pt-10 sm:pb-16 lg:pt-16 lg:pb-24 border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-center">
                
                <!-- Left Content Column (7 cols) -->
                <div class="lg:col-span-7 space-y-4 sm:space-y-6 text-left">
                    
                    <!-- Eyebrow & Client Hook (Streamlined, punchy, no mobile clutter) -->
                    <div class="flex flex-wrap items-center gap-2">
                        <div class="inline-flex items-center gap-1.5 bg-brandTealLight px-3 py-1 rounded-full border border-brandTeal/20 text-[11px] font-bold uppercase tracking-wider text-brandTeal">
                            <span class="w-1.5 h-1.5 rounded-full bg-brandTeal"></span>
                            <span>Mind-Wellness For Adults</span>
                        </div>
                        <div class="inline-flex items-center gap-2 bg-white px-3 py-1 rounded-full border border-brandOrange/30 shadow-xs text-xs sm:text-sm font-bold text-brandOrangeDark">
                            <span class="w-2 h-2 rounded-full bg-brandOrange animate-pulse"></span>
                            <span>"Body at home. Mind still at the office."</span>
                        </div>
                    </div>

                    <!-- Main Headline (Crisp, bold, perfectly responsive) -->
                    <h1 class="font-heading text-2xl sm:text-4xl lg:text-5xl font-extrabold text-brandDark tracking-tight leading-[1.25]">
                        Your Work Is Demanding. <br class="hidden sm:inline">
                        <span style="color: #007984;">Your Mind Needs Care Too.</span>
                    </h1>

                    <!-- Subheading (Exact wording from Rajendra Boddu's Document) -->
                    <p class="text-sm sm:text-base md:text-lg text-slate-700 leading-relaxed font-normal max-w-2xl">
                        Develop calmness, focus, and emotional balance through practical Brain Yoga techniques designed for everyday work and life.
                    </p>

                    <!-- Paragraph description (Visible on tablet/desktop, streamlined on mobile) -->
                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-2xl hidden sm:block">
                        <strong>Brain Yoga for Busy Minds</strong> is a practical mind-wellness program for working professionals, entrepreneurs, and adults who want to pause, reset, and respond to life's challenges with greater awareness.
                    </p>

                    <!-- CTAs (Prominent on mobile, side-by-side on desktop) -->
                    <div class="pt-1 flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
                        <button onclick="openModal('individualModal')" class="by-btn-primary !w-full sm:!w-auto !py-3 !text-sm">
                            <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                            <span>Book a FREE Introductory Session</span>
                        </button>
                        
                        <button onclick="openModal('corporateModal')" class="by-btn-secondary !w-full sm:!w-auto !py-2.5 sm:!py-3 !text-xs sm:!text-sm">
                            <i data-lucide="building-2" class="w-4 h-4"></i>
                            <span>Enquire Corporate Workshops</span>
                        </button>
                    </div>

                    <!-- Trust Tags (Single-line micro strip) -->
                    <div class="pt-1 flex flex-wrap items-center gap-x-4 gap-y-2 text-xs font-semibold text-slate-600">
                        <div class="flex items-center gap-1.5">
                            <i data-lucide="check" class="w-3.5 h-3.5 text-brandTeal"></i>
                            <span>Hands-on sessions</span>
                        </div>
                        <div class="flex items-center gap-1.5">
                            <i data-lucide="monitor" class="w-3.5 h-3.5 text-brandTeal"></i>
                            <span>Online & In-Person</span>
                        </div>
                        <div class="flex items-center gap-1.5">
                            <i data-lucide="briefcase" class="w-3.5 h-3.5 text-brandOrange"></i>
                            <span>Corporate & Individual</span>
                        </div>
                    </div>
                </div>

                <!-- Right Visual Column (5 cols) -->
                <!-- Strictly NO TEXT ON TOP OF IMAGE: Clean portrait, unified bottom bar! -->
                <div class="lg:col-span-5">
                    <div class="by-card">
                        <!-- Clean, unobstructed portrait photo -->
                        <div class="relative h-60 sm:h-72 lg:h-[370px] w-full bg-slate-100 overflow-hidden">
                            <img src="rajindra_boddu_portrait.jpg" alt="Rajendra Boddu - Brain Yoga Trainer" class="w-full h-full object-cover object-top" loading="eager" fetchpriority="high">
                        </div>

                        <!-- Single Sleek Footer Bar Below Photo -->
                        <div class="p-4 sm:p-5 bg-white border-t border-slate-100 flex items-center justify-between gap-3">
                            <div class="min-w-0">
                                <div class="flex items-center gap-2">
                                    <h3 class="text-base sm:text-lg font-bold text-brandDark truncate">Rajendra Boddu</h3>
                                    <span class="text-[9px] font-bold uppercase tracking-wider text-brandOrange bg-brandPeachLight px-2 py-0.5 rounded border border-brandOrange/20 whitespace-nowrap">Lead Trainer</span>
                                </div>
                                <p class="text-xs text-slate-500 truncate mt-0.5">15 Yrs IT Veteran & Certified Yoga Therapist</p>
                            </div>
                            
                            <!-- Compact 2-Min Demo Video Button -->
                            <button onclick="openVideoModal()" class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-brandTealLight hover:bg-brandTeal hover:text-white text-brandTeal text-xs font-bold border border-brandTeal/20 transition-all shadow-xs flex-shrink-0" aria-label="Watch 2-minute introductory video">
                                <i data-lucide="play" class="w-3.5 h-3.5 fill-current text-brandOrange"></i>
                                <span>2-Min Demo</span>
                            </button>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

import re

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the Hero section
    pattern = r'<section id="hero".*?</section>'
    new_content, count = re.subn(pattern, refined_hero_html, content, flags=re.DOTALL)
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully refined hero in: {filepath}")
    else:
        print(f"Hero section pattern not matched in: {filepath}")
