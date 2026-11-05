# Strict Children Page Brand Color Theme:
# Only Teal Blue (#007984), Sunny Orange (#F4A261 / #FD8742), Ice Blue (#D2F0FF / #E6F7F8), and Pure White (#FFFFFF).
# ZERO peach, ZERO dark brown!

import os
import re

files = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html'
]

def apply_strict_theme(content):
    # 1. Update top notification banner (from peach to soft teal/white)
    content = re.sub(
        r'<aside aria-label="Program Announcement" class="[^"]*">',
        '<aside aria-label="Program Announcement" class="bg-[#E6F7F8] border-b border-[#007984]/20 py-2 px-4 text-center text-xs font-medium text-slate-800">',
        content
    )

    # 2. Section 1: Hero (clean light background, no peach)
    content = re.sub(
        r'<section id="hero" class="relative bg-brandPeachBg pt-6 pb-12 sm:pt-10 sm:pb-16 lg:pt-16 lg:pb-24 border-b border-slate-200">',
        '<section id="hero" class="relative bg-gradient-to-b from-[#F8FCFD] to-white pt-6 pb-12 sm:pt-10 sm:pb-16 lg:pt-16 lg:pb-24 border-b border-slate-200">',
        content
    )

    # 3. Section 3: Shift in Perspective (Barking Dog) (clean white background, no peach)
    content = re.sub(
        r'<section id="shift" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">',
        '<section id="shift" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FAFCFD] border-b border-slate-200">',
        content
    )

    # 4. Section 4: What is Brain Yoga (4-Pillar Graphic container from peach to soft Ice Blue / Teal tint)
    content = content.replace('bg-brandPeachBg border border-slate-200', 'bg-[#E6F7F8]/80 border border-[#007984]/20')

    # 5. Section 7: How Does the Program Work? (Strictly NO peach, clean soft ice blue)
    content = re.sub(
        r'<section id="how-it-works" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[^"]* border-b [^"]*">',
        '<section id="how-it-works" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#EAF7FD] border-b border-sky-100">',
        content
    )
    # Inside Section 7, replace any bg-brandPeachLight with bg-orange-50 or bg-white
    how_pattern = r'(<section id="how-it-works"[^>]*>)(.*?)(</section>)'
    def how_replacer(m):
        open_tag = m.group(1)
        body = m.group(2)
        close_tag = m.group(3)
        body = body.replace('bg-brandPeachLight text-brandOrangeDark', 'bg-orange-50 text-brandOrange border border-brandOrange/25')
        body = body.replace('bg-brandPeachLight', 'bg-white border border-brandOrange/20')
        return f"{open_tag}{body}{close_tag}"
    content = re.sub(how_pattern, how_replacer, content, flags=re.DOTALL)

    # 6. Section 8: Corporate Workshops (Bright, sunny, inviting Orange from kids.html: #F4A261 to #FD8742, NO dark brown!)
    corporate_pattern = r'<section id="corporate"[^>]*>.*?</section>'
    new_corporate = """    <!-- ========================================================================= -->
    <!-- SECTION 8: CORPORATE WORKSHOPS — Bright Sunny Orange (#F4A261 ➔ #FD8742)  -->
    <!-- Matching Children Page's Vibrant, Cheerful Orange (NOT dark brown!)       -->
    <!-- ========================================================================= -->
    <section id="corporate" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-gradient-to-r from-[#F4A261] via-[#FD8742] to-[#F4A261] text-white border-b border-orange-400 shadow-md">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="inline-flex items-center gap-2 bg-white/25 px-4 py-1.5 rounded-full border border-white/40 text-xs font-bold uppercase tracking-wider text-white mb-3 shadow-xs">
                    <span class="w-2 h-2 rounded-full bg-white"></span>
                    <span>Corporate Brain Yoga Workshops</span>
                </div>
                <h2 class="main-heading !text-white">
                    Bring Brain Yoga to Your Workplace
                </h2>
                <p class="sub-heading !text-white/95 font-medium">
                    Bring Brain Yoga to your startup, IT team, business network, or organization. Our interactive workshops combine engaging brain-training activities with practical techniques that employees can incorporate into their daily lives.
                </p>
            </div>

            <!-- 4 Formats: Crisp White Cards on Sunny Orange Background -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                
                <div class="p-6 rounded-2xl bg-white text-slate-800 shadow-lg hover:shadow-2xl hover:translate-y-[-4px] transition-all">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Express Break</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">30 to 45-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Introductory session designed for team all-hands, energizer breaks, or wellness kickoffs.
                    </p>
                </div>

                <div class="p-6 rounded-2xl bg-white text-slate-800 shadow-lg border-2 border-brandTeal hover:shadow-2xl hover:translate-y-[-4px] transition-all relative">
                    <span class="absolute -top-3 right-4 text-[10px] font-bold uppercase tracking-wider bg-brandTeal text-white px-2.5 py-0.5 rounded-full shadow-xs">Popular</span>
                    <div class="text-xs font-bold text-brandOrange uppercase tracking-wider mb-2">Interactive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">60 to 90-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Interactive workshop with live practice, breathing, tapping, and desk-friendly resets.
                    </p>
                </div>

                <div class="p-6 rounded-2xl bg-white text-slate-800 shadow-lg hover:shadow-2xl hover:translate-y-[-4px] transition-all">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Intensive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Half-Day Workshop</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        In-depth training for leadership offsites, retreats, and high-performance teams.
                    </p>
                </div>

                <div class="p-6 rounded-2xl bg-white text-slate-800 shadow-lg hover:shadow-2xl hover:translate-y-[-4px] transition-all">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Sustained</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Multi-Session Program</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Weekly or monthly structured wellness journey for long-term stress resilience.
                    </p>
                </div>

            </div>

            <!-- Topics Cloud (Pure White with Crisp Badges) -->
            <div class="p-6 sm:p-8 rounded-2xl bg-white/20 backdrop-blur-xs border border-white/35 mb-10">
                <h4 class="text-sm font-bold text-white uppercase tracking-wider mb-4 text-center">
                    Workshop Topics May Include:
                </h4>
                <div class="flex flex-wrap justify-center gap-2.5 sm:gap-3">
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-sm">Focus and Attention</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-sm">Stress Awareness</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-sm">Emotional Balance</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-sm">Mindful Work Habits</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-sm">Desk-Friendly Movement</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-sm">Digital Detox Micro-Habits</span>
                </div>
            </div>

            <!-- Corporate Action CTAs -->
            <div class="text-center space-y-4">
                <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                    <button onclick="openModal('corporateModal')" class="by-btn-primary !bg-white !text-brandOrangeDark hover:!bg-orange-50 !shadow-xl font-bold">
                        <i data-lucide="file-text" class="w-4 h-4"></i>
                        <span>Request a Corporate Proposal</span>
                    </button>
                    <a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20we%20want%20to%20schedule%20a%2015-minute%20discussion%20about%20a%20Corporate%20Brain%20Yoga%20Workshop." target="_blank" class="by-btn-teal !bg-[#007984] hover:!bg-[#085C65] !shadow-xl">
                        <i data-lucide="message-square" class="w-4 h-4"></i>
                        <span>Schedule a 15-Minute Discussion</span>
                    </a>
                </div>
                <p class="text-xs text-white/90">
                    Customized proposals delivered within 24 hours. Online and in-person delivery available.
                </p>
            </div>

        </div>
    </section>"""
    content = re.sub(corporate_pattern, new_corporate, content, flags=re.DOTALL)

    # 7. Section 9: Trainer (clean white background, no peach)
    content = re.sub(
        r'<section id="trainer" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">',
        '<section id="trainer" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-white border-b border-slate-200">',
        content
    )

    # 8. Section 11: FAQ (clean white background, no peach)
    content = re.sub(
        r'<section id="faq" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">',
        '<section id="faq" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FAFCFD] border-b border-slate-200">',
        content
    )

    return content

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_c = apply_strict_theme(c)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Successfully applied strict Children brand theme to: {filepath}")
