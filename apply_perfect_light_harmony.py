# Apply Perfect Light Harmony:
# Every section background is Light Teal Blue (#E6F7F8), Light Orange (#FFE8DA), or Pure White (#FFFFFF).
# ZERO dark orange, ZERO dark teal, ZERO dark heavy backgrounds!
# All headings dark & crisp (#1F1F1F) with Teal (#007984) and Orange (#FD8742) highlights.

import os
import re

files = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html'
]

def transform_page(content):
    # 1. Top Banner: Light Teal
    content = re.sub(
        r'<aside aria-label="Program Announcement" class="[^"]*">',
        '<aside aria-label="Program Announcement" class="bg-[#E6F7F8] border-b border-[#007984]/20 py-2 px-4 text-center text-xs font-medium text-slate-800">',
        content
    )

    # 2. Section 1 (Hero): Light Orange (#FFE8DA)
    content = re.sub(
        r'<section id="hero" class="[^"]*">',
        '<section id="hero" class="relative bg-[#FFE8DA] pt-6 pb-12 sm:pt-10 sm:pb-16 lg:pt-16 lg:pb-24 border-b border-orange-200/60">',
        content
    )

    # 3. Section 2 (Challenges): Clean White (#FFFFFF) with Light Teal Cards (#E6F7F8)
    # Ensure section background is bg-white
    content = re.sub(
        r'<section id="challenges" class="[^"]*">',
        '<section id="challenges" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-white border-b border-slate-200">',
        content
    )
    # Ensure cards in Section 2 use Light Teal Blue
    challenges_pattern = r'(<section id="challenges"[^>]*>)(.*?)(</section>)'
    def challenges_replacer(m):
        open_tag = m.group(1)
        body = m.group(2)
        close_tag = m.group(3)
        body = re.sub(r'class="p-5 rounded-xl [^"]*"', 'class="p-5 rounded-xl bg-[#E6F7F8] border border-[#007984]/20 hover:border-[#007984] hover:bg-[#DDF7F8] transition-colors flex items-start gap-4"', body)
        # for the md:col-span-2 card:
        body = body.replace('class="p-5 rounded-xl bg-[#E6F7F8] border border-[#007984]/20 hover:border-[#007984] hover:bg-[#DDF7F8] transition-colors flex items-start gap-4" class="md:col-span-2', 'class="md:col-span-2 p-5 rounded-xl bg-[#E6F7F8] border border-[#007984]/20 hover:border-[#007984] hover:bg-[#DDF7F8] transition-colors flex items-start gap-4"')
        return f"{open_tag}{body}{close_tag}"
    content = re.sub(challenges_pattern, challenges_replacer, content, flags=re.DOTALL)

    # 4. Section 3 (Shift / Barking Dog): Light Orange (#FFE8DA)
    content = re.sub(
        r'<section id="shift" class="[^"]*">',
        '<section id="shift" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FFE8DA] border-b border-orange-200/60">',
        content
    )

    # 5. Section 4 (What is Brain Yoga): Clean White (#FFFFFF) with 4-pillar in Light Teal (#E6F7F8)
    content = re.sub(
        r'<section id="about" class="[^"]*">',
        '<section id="about" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-white border-b border-slate-200">',
        content
    )

    # 6. Section 5 (Our Practices): Light Teal Blue (#E6F7F8) with Clean White Cards
    practices_pattern = r'<section id="practices"[^>]*>.*?</section>'
    new_practices = """    <!-- ========================================================================= -->
    <!-- SECTION 5: OUR PRACTICES — Background: Light Teal Blue (#E6F7F8)          -->
    <!-- Light, soothing background with 8 pure white practice cards               -->
    <!-- ========================================================================= -->
    <section id="practices" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#E6F7F8] border-b border-teal-200/70">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-16">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>Curriculum & Techniques</span>
                </div>
                <h2 class="main-heading">
                    Our <span style="color: #007984;">Practices</span>
                </h2>
                <p class="sub-heading">
                    Simple, repeatable mind-wellness practices designed for desk workers, busy professionals, and leaders.
                </p>
            </div>

            <!-- 8 Full Practice Cards with Clean Unobstructed Photos -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                
                <!-- 1. Brain Gym and Brain Coordination -->
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_fit15.webp" alt="Brain Gym and Brain Coordination" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-0.5 rounded mb-2">
                                Attention & Alertness
                            </span>
                            <h3 class="text-base font-bold text-brandDark mb-2">
                                Brain Gym and Brain Coordination
                            </h3>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                Simple movements and coordination exercises that encourage attention, alertness, and a break from habitual patterns.
                            </p>
                        </div>
                    </div>
                    <div class="px-6 pb-5 pt-0">
                        <span class="text-xs font-semibold text-brandTeal hover:text-brandOrange inline-flex items-center gap-1 transition-colors">
                            Step-by-step Guided →
                        </span>
                    </div>
                </div>

                <!-- 2. Ambidextrous and Neurobic Activities -->
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_stretching_fun.webp" alt="Ambidextrous and Neurobic Activities" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-brandPeachLight px-2.5 py-0.5 rounded mb-2">
                                Neuroplasticity
                            </span>
                            <h3 class="text-base font-bold text-brandDark mb-2">
                                Ambidextrous & Neurobic Activities
                            </h3>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                Use both hands and challenge familiar routines through engaging brain-training activities.
                            </p>
                        </div>
                    </div>
                    <div class="px-6 pb-5 pt-0">
                        <span class="text-xs font-semibold text-brandTeal hover:text-brandOrange inline-flex items-center gap-1 transition-colors">
                            Step-by-step Guided →
                        </span>
                    </div>
                </div>

                <!-- 3. Breathing and Pranayama -->
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_chair_yoga.webp" alt="Breathing and Pranayama" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-0.5 rounded mb-2">
                                Nervous System Reset
                            </span>
                            <h3 class="text-base font-bold text-brandDark mb-2">
                                Breathing and Pranayama
                            </h3>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                Simple breathing practices to support relaxation and present-moment awareness.
                            </p>
                        </div>
                    </div>
                    <div class="px-6 pb-5 pt-0">
                        <span class="text-xs font-semibold text-brandTeal hover:text-brandOrange inline-flex items-center gap-1 transition-colors">
                            Step-by-step Guided →
                        </span>
                    </div>
                </div>

                <!-- 4. Mindfulness and Inner Stillness -->
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="mindfulness_peace.jpg" alt="Mindfulness and Inner Stillness" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-brandPeachLight px-2.5 py-0.5 rounded mb-2">
                                Mental Stillness
                            </span>
                            <h3 class="text-base font-bold text-brandDark mb-2">
                                Mindfulness & Inner Stillness
                            </h3>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                Learn to observe thoughts, sensations, and emotions without immediately reacting to them.
                            </p>
                        </div>
                    </div>
                    <div class="px-6 pb-5 pt-0">
                        <span class="text-xs font-semibold text-brandTeal hover:text-brandOrange inline-flex items-center gap-1 transition-colors">
                            Step-by-step Guided →
                        </span>
                    </div>
                </div>

                <!-- 5. Meditation and Creative Visualization -->
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_sound_bath.webp" alt="Meditation and Creative Visualization" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-0.5 rounded mb-2">
                                Focused Attention
                            </span>
                            <h3 class="text-base font-bold text-brandDark mb-2">
                                Meditation & Visualization
                            </h3>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                Guided practices to settle attention, clarify intentions, and mentally rehearse constructive actions.
                            </p>
                        </div>
                    </div>
                    <div class="px-6 pb-5 pt-0">
                        <span class="text-xs font-semibold text-brandTeal hover:text-brandOrange inline-flex items-center gap-1 transition-colors">
                            Step-by-step Guided →
                        </span>
                    </div>
                </div>

                <!-- 6. Emotional Awareness and EFT -->
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_laughter_yoga.webp" alt="Emotional Awareness and EFT" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-brandPeachLight px-2.5 py-0.5 rounded mb-2">
                                Emotional Balance
                            </span>
                            <h3 class="text-base font-bold text-brandDark mb-2">
                                Emotional Awareness & EFT
                            </h3>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                A guided tapping-based self-awareness practice to help participants notice and work with uncomfortable feelings.
                            </p>
                        </div>
                    </div>
                    <div class="px-6 pb-5 pt-0">
                        <span class="text-xs font-semibold text-brandTeal hover:text-brandOrange inline-flex items-center gap-1 transition-colors">
                            Step-by-step Guided →
                        </span>
                    </div>
                </div>

                <!-- 7. Yoga Nidra and Desk Relaxation -->
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_ergo_posture.webp" alt="Yoga Nidra and Desk Relaxation" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-0.5 rounded mb-2">
                                Chair & Workplace
                            </span>
                            <h3 class="text-base font-bold text-brandDark mb-2">
                                Yoga Nidra & Desk Relaxation
                            </h3>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                Guided relaxation and body-awareness practices that can be adapted to a chair or workplace.
                            </p>
                        </div>
                    </div>
                    <div class="px-6 pb-5 pt-0">
                        <span class="text-xs font-semibold text-brandTeal hover:text-brandOrange inline-flex items-center gap-1 transition-colors">
                            Step-by-step Guided →
                        </span>
                    </div>
                </div>

                <!-- 8. Everyday Awareness Techniques -->
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="executive_focus.jpg" alt="Everyday Awareness Techniques" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-brandPeachLight px-2.5 py-0.5 rounded mb-2">
                                Daily Presence
                            </span>
                            <h3 class="text-base font-bold text-brandDark mb-2">
                                Everyday Awareness Techniques
                            </h3>
                            <p class="text-xs text-slate-600 leading-relaxed">
                                Practice mindful pauses during meetings, communication, mobile phone usage, transitions, and challenging situations.
                            </p>
                        </div>
                    </div>
                    <div class="px-6 pb-5 pt-0">
                        <span class="text-xs font-semibold text-brandTeal hover:text-brandOrange inline-flex items-center gap-1 transition-colors">
                            Step-by-step Guided →
                        </span>
                    </div>
                </div>

            </div>

        </div>
    </section>"""
    content = re.sub(practices_pattern, new_practices, content, flags=re.DOTALL)

    # 7. Section 6 (Benefits): Clean White (#FFFFFF)
    content = re.sub(
        r'<section id="benefits" class="[^"]*">',
        '<section id="benefits" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-white border-b border-slate-200">',
        content
    )

    # 8. Section 7 (How It Works): Light Teal Blue (#E6F7F8)
    content = re.sub(
        r'<section id="how-it-works" class="[^"]*">',
        '<section id="how-it-works" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#E6F7F8] border-b border-teal-200/70">',
        content
    )

    # 9. Section 8 (Corporate Workshops): Light Orange (#FFE8DA) — NOT dark orange!
    corporate_pattern = r'<section id="corporate"[^>]*>.*?</section>'
    new_corporate = """    <!-- ========================================================================= -->
    <!-- SECTION 8: CORPORATE WORKSHOPS — Background: Light Orange (#FFE8DA)       -->
    <!-- Matching Children Page's Soft Warm Orange (NOT dark orange!)              -->
    <!-- ========================================================================= -->
    <section id="corporate" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FFE8DA] border-b border-orange-200/60">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow-orange">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span>Corporate Brain Yoga Workshops</span>
                </div>
                <h2 class="main-heading">
                    Bring Brain Yoga to <span style="color: #FD8742;">Your Workplace</span>
                </h2>
                <p class="sub-heading">
                    Bring Brain Yoga to your startup, IT team, business network, or organization. Our interactive workshops combine engaging brain-training activities with practical techniques that employees can incorporate into their daily lives.
                </p>
            </div>

            <!-- 4 Formats: Crisp White Cards on Light Orange Background -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                
                <div class="by-card p-6 bg-white text-slate-800 shadow-sm hover:shadow-xl transition-all">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Express Break</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">30 to 45-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Introductory session designed for team all-hands, energizer breaks, or wellness kickoffs.
                    </p>
                </div>

                <div class="by-card p-6 bg-white text-slate-800 shadow-sm border-2 border-brandTeal hover:shadow-xl transition-all relative">
                    <span class="absolute -top-3 right-4 text-[10px] font-bold uppercase tracking-wider bg-brandTeal text-white px-2.5 py-0.5 rounded-full shadow-xs">Popular</span>
                    <div class="text-xs font-bold text-brandOrange uppercase tracking-wider mb-2">Interactive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">60 to 90-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Interactive workshop with live practice, breathing, tapping, and desk-friendly resets.
                    </p>
                </div>

                <div class="by-card p-6 bg-white text-slate-800 shadow-sm hover:shadow-xl transition-all">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Intensive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Half-Day Workshop</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        In-depth training for leadership offsites, retreats, and high-performance teams.
                    </p>
                </div>

                <div class="by-card p-6 bg-white text-slate-800 shadow-sm hover:shadow-xl transition-all">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Sustained</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Multi-Session Program</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Weekly or monthly structured wellness journey for long-term stress resilience.
                    </p>
                </div>

            </div>

            <!-- Topics Cloud (Clean White Cards) -->
            <div class="p-6 sm:p-8 rounded-2xl bg-white border border-orange-200/80 mb-10 shadow-sm">
                <h4 class="text-sm font-bold text-brandDark uppercase tracking-wider mb-4 text-center">
                    Workshop Topics May Include:
                </h4>
                <div class="flex flex-wrap justify-center gap-2.5 sm:gap-3">
                    <span class="bg-[#FFE8DA] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-orange-200/80">Focus and Attention</span>
                    <span class="bg-[#FFE8DA] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-orange-200/80">Stress Awareness</span>
                    <span class="bg-[#FFE8DA] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-orange-200/80">Emotional Balance</span>
                    <span class="bg-[#FFE8DA] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-orange-200/80">Mindful Work Habits</span>
                    <span class="bg-[#FFE8DA] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-orange-200/80">Desk-Friendly Movement</span>
                    <span class="bg-[#FFE8DA] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-orange-200/80">Digital Detox Micro-Habits</span>
                </div>
            </div>

            <!-- Corporate Action CTAs -->
            <div class="text-center space-y-4">
                <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                    <button onclick="openModal('corporateModal')" class="by-btn-primary">
                        <i data-lucide="file-text" class="w-4 h-4"></i>
                        <span>Request a Corporate Proposal</span>
                    </button>
                    <a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20we%20want%20to%20schedule%20a%2015-minute%20discussion%20about%20a%20Corporate%20Brain%20Yoga%20Workshop." target="_blank" class="by-btn-secondary">
                        <i data-lucide="message-square" class="w-4 h-4"></i>
                        <span>Schedule a 15-Minute Discussion</span>
                    </a>
                </div>
                <p class="text-xs text-slate-600">
                    Customized proposals delivered within 24 hours. Online and in-person delivery available.
                </p>
            </div>

        </div>
    </section>"""
    content = re.sub(corporate_pattern, new_corporate, content, flags=re.DOTALL)

    # 10. Section 9 (Trainer): Clean White (#FFFFFF)
    content = re.sub(
        r'<section id="trainer" class="[^"]*">',
        '<section id="trainer" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-white border-b border-slate-200">',
        content
    )

    # 11. Section 10 (Testimonials): Light Orange (#FFE8DA)
    content = re.sub(
        r'<section id="testimonials" class="[^"]*">',
        '<section id="testimonials" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FFE8DA] border-b border-orange-200/60">',
        content
    )

    # 12. Section 11 (FAQ): Clean White (#FFFFFF)
    content = re.sub(
        r'<section id="faq" class="[^"]*">',
        '<section id="faq" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-white border-b border-slate-200">',
        content
    )

    # 13. Section 12 (CTA): Light Teal Blue (#E6F7F8) with Clean White Card
    cta_pattern = r'<section id="cta"[^>]*>.*?</section>'
    new_cta = """    <!-- ========================================================================= -->
    <!-- SECTION 12: FINAL CALL TO ACTION — Background: Light Teal Blue (#E6F7F8)  -->
    <!-- ========================================================================= -->
    <section id="cta" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#E6F7F8] border-b border-teal-200/70">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="by-card p-8 sm:p-14 text-center bg-white shadow-xl border border-teal-200 space-y-6">
                
                <div class="inline-flex items-center gap-2 bg-[#E6F7F8] px-4 py-1.5 rounded-full border border-[#007984]/30">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span class="text-xs font-bold uppercase tracking-widest text-[#007984]">Begin Your Practice</span>
                </div>

                <h2 class="main-heading">
                    Give Your Mind a <span style="color: #007984;">Practical Pause.</span>
                </h2>

                <p class="sub-heading">
                    Explore how Brain Yoga for Busy Minds can support your personal wellness or become part of your team's wellness initiative.
                </p>

                <div class="pt-4 flex flex-col sm:flex-row items-center justify-center gap-4">
                    <button onclick="openModal('individualModal')" class="by-btn-primary">
                        <i data-lucide="calendar" class="w-5 h-5"></i>
                        <span>Book a FREE Introductory Session</span>
                    </button>

                    <a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20I%20am%20interested%20in%20Brain%20Yoga%20for%20Busy%20Minds.%20Please%20share%20details." target="_blank" class="inline-flex items-center justify-center gap-2 px-7 py-3.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm shadow-md transition-all">
                        <i data-lucide="message-circle" class="w-5 h-5"></i>
                        <span>Enquire on WhatsApp</span>
                    </a>

                    <button onclick="openModal('corporateModal')" class="by-btn-secondary">
                        <i data-lucide="building-2" class="w-5 h-5"></i>
                        <span>Request a Corporate Workshop</span>
                    </button>
                </div>

                <p class="text-xs text-slate-500 pt-2">
                    Direct WhatsApp Contact: <a href="https://wa.me/918331929240" class="underline font-bold text-brandTeal">+91 83319 29240</a>
                </p>
            </div>
        </div>
    </section>"""
    content = re.sub(cta_pattern, new_cta, content, flags=re.DOTALL)

    return content

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_c = transform_page(c)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Successfully applied perfect light harmony to: {filepath}")
