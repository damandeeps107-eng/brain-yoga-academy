# Apply authentic Children Brain Yoga brand color architecture to all sections
import os
import re

files = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html'
]

def update_page_colors(content):
    # 1. Update Section 2 (Everyday Challenges) cards to Ice Blue (#D2F0FF) matching kids.html
    # Replace the card classes inside Section 2
    challenges_pattern = r'(<section id="challenges"[^>]*>)(.*?)(</section>)'
    def challenges_replacer(m):
        sec_open = m.group(1)
        body = m.group(2)
        sec_close = m.group(3)
        # Update cards from bg-slate-50 to bg-brandTealIce/40 hover:bg-brandTealIce/70 border border-brandTeal/20
        body = body.replace('bg-slate-50 border border-slate-200 hover:border-brandTeal', 'bg-[#D2F0FF]/50 border border-[#007984]/20 hover:border-[#007984] hover:bg-[#D2F0FF]/80')
        return f"{sec_open}{body}{sec_close}"
    content = re.sub(challenges_pattern, challenges_replacer, content, flags=re.DOTALL)

    # 2. Update Section 5 (Our Practices) to Rich Teal Blue (#007984) background matching kids.html
    practices_pattern = r'<section id="practices"[^>]*>.*?</section>'
    new_practices = """    <!-- ========================================================================= -->
    <!-- SECTION 5: OUR PRACTICES — Background: Brand Primary Teal (#007984)       -->
    <!-- Matching Children Page's Vibrant Teal Section                             -->
    <!-- ========================================================================= -->
    <section id="practices" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#007984] text-white border-b border-teal-900/30">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-16">
                <div class="inline-flex items-center gap-2 bg-white/15 px-4 py-1.5 rounded-full border border-white/25 text-xs font-bold uppercase tracking-wider text-white mb-3">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span>Curriculum & Techniques</span>
                </div>
                <h2 class="main-heading !text-white">
                    Our Practices
                </h2>
                <p class="sub-heading !text-teal-100">
                    Simple, repeatable mind-wellness practices designed for desk workers, busy professionals, and leaders.
                </p>
            </div>

            <!-- 8 Full Practice Cards with Clean Unobstructed Photos -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                
                <!-- 1. Brain Gym and Brain Coordination -->
                <div class="by-card flex flex-col justify-between bg-white text-slate-800 shadow-xl hover:shadow-2xl transition-all">
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
                <div class="by-card flex flex-col justify-between bg-white text-slate-800 shadow-xl hover:shadow-2xl transition-all">
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
                <div class="by-card flex flex-col justify-between bg-white text-slate-800 shadow-xl hover:shadow-2xl transition-all">
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
                <div class="by-card flex flex-col justify-between bg-white text-slate-800 shadow-xl hover:shadow-2xl transition-all">
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
                <div class="by-card flex flex-col justify-between bg-white text-slate-800 shadow-xl hover:shadow-2xl transition-all">
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
                <div class="by-card flex flex-col justify-between bg-white text-slate-800 shadow-xl hover:shadow-2xl transition-all">
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
                <div class="by-card flex flex-col justify-between bg-white text-slate-800 shadow-xl hover:shadow-2xl transition-all">
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
                <div class="by-card flex flex-col justify-between bg-white text-slate-800 shadow-xl hover:shadow-2xl transition-all">
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

    # 3. Update Section 7 (How Does the Program Work?) to Soft Ice Blue (#EAF7FD)
    content = content.replace(
        '<section id="how-it-works" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">',
        '<section id="how-it-works" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#EAF7FD] border-b border-sky-100">'
    )

    # 4. Update Section 8 (Corporate Workshops) to Rich Warm Orange Gradient matching kids.html
    corporate_pattern = r'<section id="corporate"[^>]*>.*?</section>'
    new_corporate = """    <!-- ========================================================================= -->
    <!-- SECTION 8: CORPORATE WORKSHOPS — Background: Warm Orange Gradient         -->
    <!-- Matching Children Page's #FD8742 / #D36005 Vibrant Accent Section         -->
    <!-- ========================================================================= -->
    <section id="corporate" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-gradient-to-br from-[#FD8742] via-[#F4A261] to-[#D36005] text-white border-b border-orange-700/20 shadow-inner">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="inline-flex items-center gap-2 bg-white/20 px-4 py-1.5 rounded-full border border-white/30 text-xs font-bold uppercase tracking-wider text-white mb-3">
                    <span class="w-2 h-2 rounded-full bg-white"></span>
                    <span>Corporate Brain Yoga Workshops</span>
                </div>
                <h2 class="main-heading !text-white">
                    Bring Brain Yoga to Your Workplace
                </h2>
                <p class="sub-heading !text-orange-100">
                    Bring Brain Yoga to your startup, IT team, business network, or organization. Our interactive workshops combine engaging brain-training activities with practical techniques that employees can incorporate into their daily lives.
                </p>
            </div>

            <!-- 4 Formats: Crisp White Cards on Orange Background -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                
                <div class="p-6 rounded-2xl bg-white text-slate-800 shadow-xl hover:translate-y-[-4px] transition-transform">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Express Break</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">30 to 45-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Introductory session designed for team all-hands, energizer breaks, or wellness kickoffs.
                    </p>
                </div>

                <div class="p-6 rounded-2xl bg-white text-slate-800 shadow-xl border-2 border-brandTeal hover:translate-y-[-4px] transition-transform relative">
                    <span class="absolute -top-3 right-4 text-[10px] font-bold uppercase tracking-wider bg-brandTeal text-white px-2.5 py-0.5 rounded-full">Popular</span>
                    <div class="text-xs font-bold text-brandOrange uppercase tracking-wider mb-2">Interactive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">60 to 90-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Interactive workshop with live practice, breathing, tapping, and desk-friendly resets.
                    </p>
                </div>

                <div class="p-6 rounded-2xl bg-white text-slate-800 shadow-xl hover:translate-y-[-4px] transition-transform">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Intensive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Half-Day Workshop</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        In-depth training for leadership offsites, retreats, and high-performance teams.
                    </p>
                </div>

                <div class="p-6 rounded-2xl bg-white text-slate-800 shadow-xl hover:translate-y-[-4px] transition-transform">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Sustained</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Multi-Session Program</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Weekly or monthly structured wellness journey for long-term stress resilience.
                    </p>
                </div>

            </div>

            <!-- Topics Cloud (Glass White) -->
            <div class="p-6 sm:p-8 rounded-2xl bg-white/15 backdrop-blur-xs border border-white/25 mb-10">
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

            <!-- Corporate CTAs -->
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
                <p class="text-xs text-orange-100">
                    Customized proposals delivered within 24 hours. Online and in-person delivery available.
                </p>
            </div>

        </div>
    </section>"""
    content = re.sub(corporate_pattern, new_corporate, content, flags=re.DOTALL)

    return content

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_c = update_page_colors(c)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Successfully applied Children Page brand color theme to: {filepath}")
