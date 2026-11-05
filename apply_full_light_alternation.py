import re

files = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html'
]

def update_sections(html):
    # 1. Top banner: Light Teal
    html = re.sub(
        r'<aside aria-label="Program Announcement" class="[^"]*">',
        '<aside aria-label="Program Announcement" class="bg-[#E6F7F8] border-b border-[#007984]/20 py-2 px-4 text-center text-xs font-medium text-slate-800">',
        html
    )

    # 2. Section 1 (Hero): Light Orange (#FFE8DA)
    html = re.sub(
        r'<section id="hero" class="[^"]*">',
        '<section id="hero" class="relative bg-[#FFE8DA] pt-6 pb-12 sm:pt-10 sm:pb-16 lg:pt-16 lg:pb-24 border-b border-orange-200/60">',
        html
    )

    # 3. Section 2 (Challenges): Light Teal Blue (#E6F7F8) with Crisp White Cards
    challenges_pattern = r'<section id="challenges"[^>]*>.*?</section>'
    new_challenges = """    <!-- ========================================================================= -->
    <!-- SECTION 2: EVERYDAY CHALLENGES — Background: Light Teal Blue (#E6F7F8)    -->
    <!-- Soft light teal background with 9 crisp white trigger cards               -->
    <!-- ========================================================================= -->
    <section id="challenges" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#E6F7F8] border-b border-teal-200/70">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>Everyday Reality Check</span>
                </div>
                <h2 class="main-heading">
                    Does This Sound Familiar? <span style="color: #007984;">You're Not Alone.</span>
                </h2>
                <p class="sub-heading">
                    Your work is important. But what about your mental well-being?
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-orange-100 text-brandOrange flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="compass" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Constant Distraction</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">Struggling to stay focused while working or studying?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-teal-100 text-brandTeal flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="smartphone" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Compulsive Phone Checking</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">Reaching for your phone repeatedly without realizing it?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-orange-100 text-brandOrange flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="battery-low" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Energy Crash by Afternoon</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">Starting your day motivated, but running on empty by mid-afternoon?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-teal-100 text-brandTeal flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="zap" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Frequent Irritation</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">Getting easily irritated, stressed, or emotionally drained by small interruptions?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-orange-100 text-brandOrange flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Overthinking at Bedtime</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">Replaying conversations, tasks, and worries long after the workday is done?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-teal-100 text-brandTeal flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="monitor" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Digital Brain Fog</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">Back-to-back meetings, chats, and tabs leaving your mind buzzing and scattered?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-orange-100 text-brandOrange flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="repeat" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Routine Resistance</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">Knowing you should pause or stretch, but trapped in the cycle of "one more task"?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-teal-100 text-brandTeal flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="coffee" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Restless Rest</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">Even on weekends, your mind stays locked in work mode and emergency readiness?</p>
                    </div>
                </div>

                <div class="md:col-span-2 p-5 rounded-xl bg-white border border-[#007984]/20 hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange text-white flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Capable, But Constantly Operating at Mental Capacity</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">You handle your responsibilities well — but beneath the surface, your nervous system is in a state of unending overdrive.</p>
                    </div>
                </div>
            </div>

            <div class="mt-12 text-center">
                <p class="text-xs text-slate-600 max-w-xl mx-auto">
                    These are not personal shortcomings. They are the natural response of an overloaded nervous system navigating constant digital stimulation.
                </p>
            </div>

        </div>
    </section>"""
    html = re.sub(challenges_pattern, new_challenges, html, flags=re.DOTALL)

    # 4. Section 3 (Shift): Light Orange (#FFE8DA)
    html = re.sub(
        r'<section id="shift" class="[^"]*">',
        '<section id="shift" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FFE8DA] border-b border-orange-200/60">',
        html
    )

    # 5. Section 4 (What is Brain Yoga / About): Light Teal Blue (#E6F7F8)
    about_pattern = r'<section id="about"[^>]*>.*?</section>'
    new_about = """    <!-- ========================================================================= -->
    <!-- SECTION 4: WHAT IS BRAIN YOGA — Background: Light Teal Blue (#E6F7F8)      -->
    <!-- ========================================================================= -->
    <section id="about" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#E6F7F8] border-b border-teal-200/70">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>The Core Philosophy</span>
                </div>
                <h2 class="main-heading">
                    What Is <span style="color: #007984;">Brain Yoga for Busy Minds?</span>
                </h2>
                <p class="sub-heading font-medium text-slate-700">
                    "Brain Yoga for Busy Minds combines simple brain-training activities, mindful movements, breathing techniques, and meditation to help you become more aware of your thoughts, emotions, and everyday responses."
                </p>
            </div>

            <!-- 4-Pillar Graphic Architecture (White Container on Light Teal) -->
            <div class="mb-14 p-8 rounded-2xl bg-white border border-[#007984]/20 shadow-sm">
                <div class="text-center mb-8">
                    <span class="text-[11px] font-bold uppercase tracking-wider text-brandOrange bg-[#FFE8DA] px-3 py-1 rounded-md border border-brandOrange/20 shadow-xs">
                        The 4-Pillar Mind-Reset Arc
                    </span>
                    <h3 class="text-lg font-bold text-brandDark mt-2">A Complete, Practical Loop for Mental Clarity</h3>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="p-6 rounded-xl bg-[#E6F7F8] border border-[#007984]/20 text-center hover:shadow-md transition-all">
                        <div class="w-12 h-12 mx-auto rounded-xl bg-white text-brandTeal flex items-center justify-center font-bold text-base mb-3 shadow-xs border border-[#007984]/20">01</div>
                        <h4 class="font-bold text-brandDark text-sm mb-1.5">Brain-Training Activities</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">Break habitual mental autopilot and stimulate neuroplastic pathways.</p>
                    </div>

                    <div class="p-6 rounded-xl bg-[#FFE8DA] border border-orange-200/80 text-center hover:shadow-md transition-all">
                        <div class="w-12 h-12 mx-auto rounded-xl bg-white text-brandOrange flex items-center justify-center font-bold text-base mb-3 shadow-xs border border-orange-200">02</div>
                        <h4 class="font-bold text-brandDark text-sm mb-1.5">Mindful Movements</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">Release physical stiffness and ground attention back into the body.</p>
                    </div>

                    <div class="p-6 rounded-xl bg-[#E6F7F8] border border-[#007984]/20 text-center hover:shadow-md transition-all">
                        <div class="w-12 h-12 mx-auto rounded-xl bg-white text-brandTeal flex items-center justify-center font-bold text-base mb-3 shadow-xs border border-[#007984]/20">03</div>
                        <h4 class="font-bold text-brandDark text-sm mb-1.5">Breathing Practices</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">Downshift the sympathetic nervous system and soothe stress spikes.</p>
                    </div>

                    <div class="p-6 rounded-xl bg-[#FFE8DA] border border-orange-200/80 text-center hover:shadow-md transition-all">
                        <div class="w-12 h-12 mx-auto rounded-xl bg-white text-brandOrange flex items-center justify-center font-bold text-base mb-3 shadow-xs border border-orange-200">04</div>
                        <h4 class="font-bold text-brandDark text-sm mb-1.5">Inner Stillness & Meditation</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">Cultivate unshakeable focus and non-reactive cognitive spaciousness.</p>
                    </div>
                </div>
            </div>

            <!-- 3 Mind-Body Connection Pillars -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="by-card p-6 bg-white border border-[#007984]/20 shadow-xs">
                    <div class="w-10 h-10 rounded-lg bg-[#E6F7F8] text-brandTeal flex items-center justify-center mb-4">
                        <i data-lucide="brain" class="w-5 h-5"></i>
                    </div>
                    <h3 class="text-base font-bold text-brandDark mb-2">Notice Thoughts Early</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Recognize spiraling thoughts before they hijack your focus, conversations, or evening rest.
                    </p>
                </div>

                <div class="by-card p-6 bg-white border border-[#007984]/20 shadow-xs">
                    <div class="w-10 h-10 rounded-lg bg-[#FFE8DA] text-brandOrange flex items-center justify-center mb-4">
                        <i data-lucide="heart-pulse" class="w-5 h-5"></i>
                    </div>
                    <h3 class="text-base font-bold text-brandDark mb-2">Soothe Emotional Surges</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Build an internal buffer against urgency, deadline panic, and workplace friction.
                    </p>
                </div>

                <div class="by-card p-6 bg-white border border-[#007984]/20 shadow-xs">
                    <div class="w-10 h-10 rounded-lg bg-[#E6F7F8] text-brandTeal flex items-center justify-center mb-4">
                        <i data-lucide="activity" class="w-5 h-5"></i>
                    </div>
                    <h3 class="text-base font-bold text-brandDark mb-2">Desk-Friendly & Practical</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Zero special equipment or workout clothes needed. Every micro-reset fits seamlessly into office life.
                    </p>
                </div>
            </div>

        </div>
    </section>"""
    html = re.sub(about_pattern, new_about, html, flags=re.DOTALL)

    # 6. Section 5 (Our Practices): Light Orange (#FFE8DA)
    practices_pattern = r'<section id="practices"[^>]*>.*?</section>'
    new_practices = """    <!-- ========================================================================= -->
    <!-- SECTION 5: OUR PRACTICES — Background: Light Orange (#FFE8DA)              -->
    <!-- Soft light orange background with 8 pure white practice cards              -->
    <!-- ========================================================================= -->
    <section id="practices" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FFE8DA] border-b border-orange-200/60">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-16">
                <div class="section-eyebrow-orange">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span>Curriculum & Techniques</span>
                </div>
                <h2 class="main-heading">
                    Our <span style="color: #FD8742;">Practices</span>
                </h2>
                <p class="sub-heading">
                    Simple, repeatable mind-wellness practices designed for desk workers, busy professionals, and leaders.
                </p>
            </div>

            <!-- 8 Full Practice Cards with Clean Unobstructed Photos -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                
                <!-- 1. Brain Gym and Brain Coordination -->
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_fit15.webp" alt="Brain Gym and Brain Coordination" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-teal-50 px-2.5 py-0.5 rounded mb-2 border border-teal-200/60">
                                Attention & Alertness
                            </span>
                            <h3 class="text-base font-bold text-brandDark mb-2">
                                Brain Gym & Brain Coordination
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
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_stretching_fun.webp" alt="Ambidextrous and Neurobic Activities" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-orange-50 px-2.5 py-0.5 rounded mb-2 border border-orange-200/60">
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
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_chair_yoga.webp" alt="Breathing and Pranayama" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-teal-50 px-2.5 py-0.5 rounded mb-2 border border-teal-200/60">
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
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="mindfulness_peace.jpg" alt="Mindfulness and Inner Stillness" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-orange-50 px-2.5 py-0.5 rounded mb-2 border border-orange-200/60">
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
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_sound_bath.webp" alt="Meditation and Creative Visualization" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-teal-50 px-2.5 py-0.5 rounded mb-2 border border-teal-200/60">
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
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_laughter_yoga.webp" alt="Emotional Awareness and EFT" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-orange-50 px-2.5 py-0.5 rounded mb-2 border border-orange-200/60">
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
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_ergo_posture.webp" alt="Yoga Nidra and Desk Relaxation" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-teal-50 px-2.5 py-0.5 rounded mb-2 border border-teal-200/60">
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
                <div class="by-card flex flex-col justify-between bg-white shadow-sm hover:shadow-xl transition-all border border-orange-200/70">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="executive_focus.jpg" alt="Everyday Awareness Techniques" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-orange-50 px-2.5 py-0.5 rounded mb-2 border border-orange-200/60">
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
    html = re.sub(practices_pattern, new_practices, html, flags=re.DOTALL)

    # 7. Section 6 (Benefits / What Regular Practice Can Build): Light Teal Blue (#E6F7F8)
    benefits_pattern = r'<section id="benefits"[^>]*>.*?</section>'
    new_benefits = """    <!-- ========================================================================= -->
    <!-- SECTION 6: BENEFITS — Background: Light Teal Blue (#E6F7F8)                -->
    <!-- ========================================================================= -->
    <section id="benefits" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#E6F7F8] border-b border-teal-200/70">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>Sustainable Benefits</span>
                </div>
                <h2 class="main-heading">
                    What Regular Practice <span style="color: #007984;">Can Build</span>
                </h2>
                <p class="sub-heading">
                    Participants may gradually develop:
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 flex items-center gap-4 shadow-xs hover:border-[#007984] transition-colors">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Greater awareness of stress triggers and habitual reactions.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 flex items-center gap-4 shadow-xs hover:border-[#007984] transition-colors">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Improved ability to pause before reacting in challenging situations.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 flex items-center gap-4 shadow-xs hover:border-[#007984] transition-colors">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Practical tools to reset attention and reduce mental fatigue during work.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 flex items-center gap-4 shadow-xs hover:border-[#007984] transition-colors">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Simple techniques to support emotional balance and calm.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 flex items-center gap-4 shadow-xs hover:border-[#007984] transition-colors">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Mindful work habits that protect focus and personal well-being.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white border border-[#007984]/20 flex items-center gap-4 shadow-xs hover:border-[#007984] transition-colors">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Healthier boundaries with screens, notifications, and workplace urgency.
                    </p>
                </div>
            </div>

            <!-- Neuroplasticity Box -->
            <div class="mt-8 p-6 rounded-2xl bg-white border border-[#007984]/20 shadow-xs flex items-center gap-4">
                <div class="w-10 h-10 rounded-full bg-[#E6F7F8] text-brandTeal flex items-center justify-center flex-shrink-0 border border-[#007984]/20">
                    <i data-lucide="sparkles" class="w-5 h-5"></i>
                </div>
                <div>
                    <h4 class="text-sm font-bold text-brandDark">Rooted in Neuroplasticity & Habit Formation</h4>
                    <p class="text-xs text-slate-600 mt-0.5">Brain Yoga trains your brain to break automatic stress responses and replace them with deliberate, conscious choices.</p>
                </div>
            </div>

        </div>
    </section>"""
    html = re.sub(benefits_pattern, new_benefits, html, flags=re.DOTALL)

    # 8. Section 7 (How Does the Program Work?): Light Orange (#FFE8DA) — NO PEACH!
    how_pattern = r'<section id="how-it-works"[^>]*>.*?</section>'
    new_how = """    <!-- ========================================================================= -->
    <!-- SECTION 7: HOW DOES THE PROGRAM WORK — Background: Light Orange (#FFE8DA)  -->
    <!-- ========================================================================= -->
    <section id="how-it-works" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FFE8DA] border-b border-orange-200/60">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-12">
                <div class="section-eyebrow-orange">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span>Flexible Delivery</span>
                </div>
                <h2 class="main-heading">
                    How Does the <span style="color: #FD8742;">Program Work?</span>
                </h2>
                <p class="sub-heading">
                    Practical sessions designed for real life, with flexible formats for individuals and corporate teams.
                </p>

                <!-- Program Chips from document -->
                <div class="mt-4 flex flex-wrap justify-center gap-3 text-xs font-semibold text-slate-700">
                    <span class="bg-white px-3.5 py-1.5 rounded-lg border border-orange-200/80 shadow-xs">
                        📍 Format: Live guided sessions, online or in person
                    </span>
                    <span class="bg-white px-3.5 py-1.5 rounded-lg border border-orange-200/80 shadow-xs">
                        👥 Designed for: Adults, working professionals, entrepreneurs & teams
                    </span>
                </div>
            </div>

            <!-- Corporate Session Showcase Cards - Clean Unobstructed Photos! -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
                <div class="by-card bg-white border border-orange-200/80 overflow-hidden shadow-sm hover:shadow-xl transition-all">
                    <div class="aspect-[16/10] w-full overflow-hidden bg-slate-100">
                        <img src="workshop_team.jpg" alt="Corporate Brain Yoga Workshop" class="w-full h-full object-cover" loading="lazy" decoding="async">
                    </div>
                    <div class="p-6 bg-white">
                        <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-teal-50 px-2.5 py-0.5 rounded mb-2 border border-teal-200/60">
                            Team Wellness In Action
                        </span>
                        <h4 class="text-base sm:text-lg font-bold text-brandDark">Interactive Hands-on Exercises</h4>
                        <p class="text-xs text-slate-600 mt-1 leading-relaxed">Energizing breaks that improve focus, reduce fatigue, and boost team morale.</p>
                    </div>
                </div>

                <div class="by-card bg-white border border-orange-200/80 overflow-hidden shadow-sm hover:shadow-xl transition-all">
                    <div class="aspect-[16/10] w-full overflow-hidden bg-slate-100">
                        <img src="workshop_interactive.jpg" alt="Brain Gym and Desk Stretching" class="w-full h-full object-cover" loading="lazy" decoding="async">
                    </div>
                    <div class="p-6 bg-white">
                        <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-orange-50 px-2.5 py-0.5 rounded mb-2 border border-orange-200/60">
                            Desk-Friendly Adaptability
                        </span>
                        <h4 class="text-base sm:text-lg font-bold text-brandDark">Chair & Ergonomic Mind-Breaks</h4>
                        <p class="text-xs text-slate-600 mt-1 leading-relaxed">No special clothing or gym required — perfectly suited for office environments.</p>
                    </div>
                </div>
            </div>

            <!-- Available Formats Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
                
                <div class="by-card p-6 text-center bg-white border border-orange-200/80 shadow-xs hover:shadow-md transition-all">
                    <div class="w-12 h-12 rounded-lg bg-orange-50 text-brandOrange border border-brandOrange/25 mx-auto flex items-center justify-center mb-3">
                        <i data-lucide="sun" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-brandDark text-base mb-1">Introductory Session</h4>
                    <p class="text-xs text-slate-500">Perfect to experience the core methods firsthand</p>
                </div>

                <div class="by-card p-6 text-center bg-white border border-orange-200/80 shadow-xs hover:shadow-md transition-all">
                    <div class="w-12 h-12 rounded-lg bg-teal-50 text-brandTeal border border-teal-200/60 mx-auto flex items-center justify-center mb-3">
                        <i data-lucide="target" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-brandDark text-base mb-1">Focused Workshop</h4>
                    <p class="text-xs text-slate-500">Deep-dive on focus, screen habits, or stress</p>
                </div>

                <div class="by-card p-6 text-center bg-white border border-orange-200/80 shadow-xs hover:shadow-md transition-all">
                    <div class="w-12 h-12 rounded-lg bg-orange-50 text-brandOrange border border-brandOrange/25 mx-auto flex items-center justify-center mb-3">
                        <i data-lucide="layers" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-brandDark text-base mb-1">Multi-Session Program</h4>
                    <p class="text-xs text-slate-500">Progressive habit-building over consecutive weeks</p>
                </div>

                <div class="by-card p-6 text-center bg-white border border-orange-200/80 shadow-xs hover:shadow-md transition-all">
                    <div class="w-12 h-12 rounded-lg bg-teal-50 text-brandTeal border border-teal-200/60 mx-auto flex items-center justify-center mb-3">
                        <i data-lucide="building-2" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-brandDark text-base mb-1">Customized Corporate</h4>
                    <p class="text-xs text-slate-500">Tailored to your organization size and schedule</p>
                </div>

            </div>

            <!-- Action Button -->
            <div class="by-card p-8 text-center max-w-2xl mx-auto bg-white border border-orange-200/80 shadow-sm">
                <p class="text-sm sm:text-base font-semibold text-slate-800 mb-6">
                    Participants also learn simple activities that they can practice independently at home or during work breaks.
                </p>
                <button onclick="openModal('corporateModal')" class="by-btn-primary">
                    <i data-lucide="users" class="w-4 h-4"></i>
                    <span>Discuss a Program for Your Team</span>
                </button>
            </div>

        </div>
    </section>"""
    html = re.sub(how_pattern, new_how, html, flags=re.DOTALL)

    # 9. Section 8 (Corporate Workshops): Light Teal Blue (#E6F7F8) — NOT DARK ORANGE!
    corporate_pattern = r'<section id="corporate"[^>]*>.*?</section>'
    new_corporate = """    <!-- ========================================================================= -->
    <!-- SECTION 8: CORPORATE WORKSHOPS — Background: Light Teal Blue (#E6F7F8)     -->
    <!-- Soft light teal background (NO dark orange!) with crisp white cards        -->
    <!-- ========================================================================= -->
    <section id="corporate" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#E6F7F8] border-b border-teal-200/70">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>Corporate Brain Yoga Workshops</span>
                </div>
                <h2 class="main-heading">
                    Bring Brain Yoga to <span style="color: #007984;">Your Workplace</span>
                </h2>
                <p class="sub-heading">
                    Bring Brain Yoga to your startup, IT team, business network, or organization. Our interactive workshops combine engaging brain-training activities with practical techniques that employees can incorporate into their daily lives.
                </p>
            </div>

            <!-- 4 Formats: Crisp White Cards on Light Teal Blue Background -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                
                <div class="by-card p-6 bg-white text-slate-800 shadow-sm hover:shadow-xl transition-all border border-[#007984]/20">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Express Break</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">30 to 45-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Introductory session designed for team all-hands, energizer breaks, or wellness kickoffs.
                    </p>
                </div>

                <div class="by-card p-6 bg-white text-slate-800 shadow-sm border-2 border-brandTeal hover:shadow-xl transition-all relative">
                    <span class="absolute -top-3 right-4 text-[10px] font-bold uppercase tracking-wider bg-brandOrange text-white px-2.5 py-0.5 rounded-full shadow-xs">Popular</span>
                    <div class="text-xs font-bold text-brandOrange uppercase tracking-wider mb-2">Interactive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">60 to 90-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Interactive workshop with live practice, breathing, tapping, and desk-friendly resets.
                    </p>
                </div>

                <div class="by-card p-6 bg-white text-slate-800 shadow-sm hover:shadow-xl transition-all border border-[#007984]/20">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Intensive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Half-Day Workshop</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        In-depth training for leadership offsites, retreats, and high-performance teams.
                    </p>
                </div>

                <div class="by-card p-6 bg-white text-slate-800 shadow-sm hover:shadow-xl transition-all border border-[#007984]/20">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Sustained</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Multi-Session Program</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Weekly or monthly structured wellness journey for long-term stress resilience.
                    </p>
                </div>

            </div>

            <!-- Topics Cloud (Clean White Cards) -->
            <div class="p-6 sm:p-8 rounded-2xl bg-white border border-[#007984]/20 mb-10 shadow-sm">
                <h4 class="text-sm font-bold text-brandDark uppercase tracking-wider mb-4 text-center">
                    Workshop Topics May Include:
                </h4>
                <div class="flex flex-wrap justify-center gap-2.5 sm:gap-3">
                    <span class="bg-[#E6F7F8] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-[#007984]/20">Focus and Attention</span>
                    <span class="bg-[#E6F7F8] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-[#007984]/20">Stress Awareness</span>
                    <span class="bg-[#E6F7F8] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-[#007984]/20">Emotional Balance</span>
                    <span class="bg-[#E6F7F8] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-[#007984]/20">Mindful Work Habits</span>
                    <span class="bg-[#E6F7F8] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-[#007984]/20">Desk-Friendly Movement</span>
                    <span class="bg-[#E6F7F8] text-slate-800 text-xs font-bold px-4 py-2 rounded-lg border border-[#007984]/20">Digital Detox Micro-Habits</span>
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
    html = re.sub(corporate_pattern, new_corporate, html, flags=re.DOTALL)

    # 10. Section 9 (Meet Your Trainer): Light Orange (#FFE8DA)
    trainer_pattern = r'<section id="trainer"[^>]*>.*?</section>'
    new_trainer = """    <!-- ========================================================================= -->
    <!-- SECTION 9: TRAINER PROFILE — Background: Light Orange (#FFE8DA)            -->
    <!-- ========================================================================= -->
    <section id="trainer" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FFE8DA] border-b border-orange-200/60">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="p-8 sm:p-12 rounded-3xl bg-white border border-orange-200/80 shadow-md">
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
                    
                    <!-- Trainer Portrait Column -->
                    <div class="lg:col-span-5 flex flex-col items-center">
                        <div class="relative w-64 h-64 sm:w-72 sm:h-72 rounded-2xl overflow-hidden shadow-lg border-4 border-[#FFE8DA]">
                            <img src="rajendra_boddu.webp" alt="Rajendra Boddu - Founder and Trainer" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="mt-4 text-center">
                            <span class="inline-block text-xs font-bold uppercase tracking-wider text-brandOrange bg-[#FFE8DA] px-3.5 py-1 rounded-full border border-orange-200">
                                Founder & Lead Facilitator
                            </span>
                        </div>
                    </div>

                    <!-- Bio Column -->
                    <div class="lg:col-span-7 space-y-4">
                        <div class="section-eyebrow-orange mb-1">
                            <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                            <span>Dedicated Mind-Wellness Educator</span>
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-extrabold text-brandDark">
                            Rajendra Boddu
                        </h2>
                        <p class="text-sm font-semibold text-brandTeal">
                            Founder, Brain Yoga Academy | Certified Yoga & Mind-Wellness Facilitator
                        </p>
                        <p class="text-xs sm:text-sm text-slate-700 leading-relaxed">
                            Rajendra Boddu has guided hundreds of professionals, entrepreneurs, educators, and children in discovering the power of the mind-body connection. His practical, non-dogmatic approach combines ancient mindfulness principles with modern neuroscience-informed brain gym techniques.
                        </p>
                        <p class="text-xs sm:text-sm text-slate-700 leading-relaxed">
                            Whether delivering interactive workshops for corporate organizations or guiding individuals through 1-on-1 focus coaching, Rajendra's mission is to make mental wellness accessible, sustainable, and immediately actionable for busy daily routines.
                        </p>

                        <!-- Key Credentials Pills -->
                        <div class="pt-2 flex flex-wrap gap-2 text-xs">
                            <span class="bg-[#FFE8DA] text-slate-800 font-bold px-3 py-1.5 rounded-lg border border-orange-200/80">
                                🏅 10+ Years Experience
                            </span>
                            <span class="bg-[#FFE8DA] text-slate-800 font-bold px-3 py-1.5 rounded-lg border border-orange-200/80">
                                👥 5,000+ Participants Guided
                            </span>
                            <span class="bg-[#FFE8DA] text-slate-800 font-bold px-3 py-1.5 rounded-lg border border-orange-200/80">
                                🏢 Trusted by Corporate Teams
                            </span>
                        </div>

                        <!-- Direct WhatsApp Contact -->
                        <div class="pt-3">
                            <a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20I%20would%20like%20to%20connect%20regarding%20Brain%20Yoga%20for%20Busy%20Minds." target="_blank" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-sm transition-all">
                                <i data-lucide="message-circle" class="w-4 h-4"></i>
                                <span>Message Rajendra on WhatsApp (+91 83319 29240)</span>
                            </a>
                        </div>
                    </div>

                </div>
            </div>

        </div>
    </section>"""
    html = re.sub(trainer_pattern, new_trainer, html, flags=re.DOTALL)

    # 11. Section 10 (Testimonials): Light Teal Blue (#E6F7F8)
    testimonials_pattern = r'<section id="testimonials"[^>]*>.*?</section>'
    new_testimonials = """    <!-- ========================================================================= -->
    <!-- SECTION 10: TESTIMONIALS — Background: Light Teal Blue (#E6F7F8)           -->
    <!-- Soft light teal background with 6 crisp white participant review cards     -->
    <!-- ========================================================================= -->
    <section id="testimonials" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#E6F7F8] border-b border-teal-200/70">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>Real Experiences</span>
                </div>
                <h2 class="main-heading">
                    What <span style="color: #007984;">Participants Say</span>
                </h2>
                <p class="sub-heading">
                    Real experiences from busy professionals who made mind-wellness a daily habit.
                </p>
            </div>

            <!-- 6 Testimonial Cards: Crisp White on Light Teal Blue -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                
                <!-- 1. Uma Maheswari -->
                <div class="by-card p-6 bg-white border border-[#007984]/20 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-amber-400 mb-3">
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed italic mb-4">
                            "The simple breathing techniques and ambidextrous coordination drills helped me break my continuous chain of work fatigue. I feel noticeably lighter and more present with my family in the evenings."
                        </p>
                    </div>
                    <div class="flex items-center gap-3 pt-3 border-t border-slate-100">
                        <div class="w-10 h-10 rounded-full overflow-hidden bg-slate-100 border border-teal-200 flex-shrink-0">
                            <img src="testimonial_uma_1793758173360.jpg" alt="Uma Maheswari" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Uma Maheswari</h4>
                            <p class="text-[11px] text-slate-500">Senior IT Project Manager</p>
                        </div>
                    </div>
                </div>

                <!-- 2. Aryan Gupta -->
                <div class="by-card p-6 bg-white border border-[#007984]/20 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-amber-400 mb-3">
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed italic mb-4">
                            "The '10 People. 1 Barking Dog' concept completely shifted how I react to crisis emails. Instead of firing off impulsive responses, I pause, reset, and respond with complete calm."
                        </p>
                    </div>
                    <div class="flex items-center gap-3 pt-3 border-t border-slate-100">
                        <div class="w-10 h-10 rounded-full overflow-hidden bg-slate-100 border border-teal-200 flex-shrink-0">
                            <img src="testimonial_aryan_1793758191112.jpg" alt="Aryan Gupta" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Aryan Gupta</h4>
                            <p class="text-[11px] text-slate-500">Tech Lead & Architect</p>
                        </div>
                    </div>
                </div>

                <!-- 3. Kavitha Reddy -->
                <div class="by-card p-6 bg-white border border-[#007984]/20 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-amber-400 mb-3">
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed italic mb-4">
                            "We introduced the 60-minute workshop to our corporate team. Employees praised the practical desk stretches and tapping exercises. It was by far our highest-rated wellness session."
                        </p>
                    </div>
                    <div class="flex items-center gap-3 pt-3 border-t border-slate-100">
                        <div class="w-10 h-10 rounded-full overflow-hidden bg-slate-100 border border-teal-200 flex-shrink-0">
                            <img src="testimonial_kavitha_1793758210904.jpg" alt="Kavitha Reddy" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Kavitha Reddy</h4>
                            <p class="text-[11px] text-slate-500">HR Director, FinTech</p>
                        </div>
                    </div>
                </div>

                <!-- 4. Sravani V. -->
                <div class="by-card p-6 bg-white border border-[#007984]/20 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-amber-400 mb-3">
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed italic mb-4">
                            "Bedtime overthinking used to rob me of 2 hours of sleep every night. The Yoga Nidra relaxation routine from Brain Yoga helped me fall asleep naturally within minutes."
                        </p>
                    </div>
                    <div class="flex items-center gap-3 pt-3 border-t border-slate-100">
                        <div class="w-10 h-10 rounded-full overflow-hidden bg-slate-100 border border-teal-200 flex-shrink-0">
                            <img src="testimonial_sravani_1793758228445.jpg" alt="Sravani V." class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Sravani V.</h4>
                            <p class="text-[11px] text-slate-500">Digital Marketing Consultant</p>
                        </div>
                    </div>
                </div>

                <!-- 5. Vinay Kumar -->
                <div class="by-card p-6 bg-white border border-[#007984]/20 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-amber-400 mb-3">
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed italic mb-4">
                            "As an entrepreneur constantly context-switching, Brain Yoga gave me quick 2-minute reset anchors during meetings that keep my decision-making sharp and calm."
                        </p>
                    </div>
                    <div class="flex items-center gap-3 pt-3 border-t border-slate-100">
                        <div class="w-10 h-10 rounded-full overflow-hidden bg-slate-100 border border-teal-200 flex-shrink-0">
                            <img src="testimonial_vinay_1793758244014.jpg" alt="Vinay Kumar" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Vinay Kumar</h4>
                            <p class="text-[11px] text-slate-500">Startup Founder</p>
                        </div>
                    </div>
                </div>

                <!-- 6. Kiran Shah -->
                <div class="by-card p-6 bg-white border border-[#007984]/20 shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-1 text-amber-400 mb-3">
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                            <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed italic mb-4">
                            "What I appreciate most is that Rajendra ji explains the 'why' behind each technique without any mysticism. It is 100% scientific, sensible, and deeply effective."
                        </p>
                    </div>
                    <div class="flex items-center gap-3 pt-3 border-t border-slate-100">
                        <div class="w-10 h-10 rounded-full overflow-hidden bg-slate-100 border border-teal-200 flex-shrink-0">
                            <img src="testimonial_kiran_1793758263214.jpg" alt="Kiran Shah" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Kiran Shah</h4>
                            <p class="text-[11px] text-slate-500">Chartered Accountant</p>
                        </div>
                    </div>
                </div>

            </div>

        </div>
    </section>"""
    html = re.sub(testimonials_pattern, new_testimonials, html, flags=re.DOTALL)

    # 12. Section 11 (FAQ): Light Orange (#FFE8DA)
    faq_pattern = r'<section id="faq"[^>]*>.*?</section>'
    new_faq = """    <!-- ========================================================================= -->
    <!-- SECTION 11: FAQ — Background: Light Orange (#FFE8DA)                       -->
    <!-- Soft light orange background with clean white accordion cards              -->
    <!-- ========================================================================= -->
    <section id="faq" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#FFE8DA] border-b border-orange-200/60">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow-orange">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span>Got Questions?</span>
                </div>
                <h2 class="main-heading">
                    Frequently Asked <span style="color: #FD8742;">Questions</span>
                </h2>
                <p class="sub-heading">
                    Everything you need to know about starting your Brain Yoga practice.
                </p>
            </div>

            <!-- Accordion List: Clean White Cards on Light Orange -->
            <div class="space-y-4">
                
                <div class="rounded-2xl border border-orange-200/80 bg-white shadow-xs overflow-hidden">
                    <button type="button" class="faq-btn w-full p-6 text-left flex items-center justify-between gap-4 font-bold text-brandDark text-sm sm:text-base hover:text-brandOrange transition-colors" aria-expanded="false">
                        <span>Do I need prior yoga or meditation experience?</span>
                        <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 transition-transform duration-200"></i>
                    </button>
                    <div class="faq-content hidden px-6 pb-6 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-4">
                        Not at all. Brain Yoga for Busy Minds is specifically designed for beginners, desk workers, and people with active, restless minds. There are no complicated poses, flexibility requirements, or religious rituals.
                    </div>
                </div>

                <div class="rounded-2xl border border-orange-200/80 bg-white shadow-xs overflow-hidden">
                    <button type="button" class="faq-btn w-full p-6 text-left flex items-center justify-between gap-4 font-bold text-brandDark text-sm sm:text-base hover:text-brandOrange transition-colors" aria-expanded="false">
                        <span>Can these practices really be done in an office setting?</span>
                        <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 transition-transform duration-200"></i>
                    </button>
                    <div class="faq-content hidden px-6 pb-6 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-4">
                        Yes! All practices are desk-friendly and chair-based. You do not need to change clothes, roll out a yoga mat, or lie on the floor. Everything can be practiced comfortably sitting in your office chair or standing at your desk.
                    </div>
                </div>

                <div class="rounded-2xl border border-orange-200/80 bg-white shadow-xs overflow-hidden">
                    <button type="button" class="faq-btn w-full p-6 text-left flex items-center justify-between gap-4 font-bold text-brandDark text-sm sm:text-base hover:text-brandOrange transition-colors" aria-expanded="false">
                        <span>How much time does daily practice take?</span>
                        <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 transition-transform duration-200"></i>
                    </button>
                    <div class="faq-content hidden px-6 pb-6 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-4">
                        Just 5 to 10 minutes a day is sufficient to experience meaningful shifts in your nervous system. In fact, many of the micro-pause techniques take only 60 to 90 seconds between meetings or before opening your email inbox.
                    </div>
                </div>

                <div class="rounded-2xl border border-orange-200/80 bg-white shadow-xs overflow-hidden">
                    <button type="button" class="faq-btn w-full p-6 text-left flex items-center justify-between gap-4 font-bold text-brandDark text-sm sm:text-base hover:text-brandOrange transition-colors" aria-expanded="false">
                        <span>How do corporate workshop bookings work?</span>
                        <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 transition-transform duration-200"></i>
                    </button>
                    <div class="faq-content hidden px-6 pb-6 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-4">
                        We offer customized corporate workshops ranging from 45-minute energizers to full-day leadership offsites. We can deliver sessions virtually over Zoom/Teams or in-person at your offices across India. Customized proposals are provided within 24 hours.
                    </div>
                </div>

                <div class="rounded-2xl border border-orange-200/80 bg-white shadow-xs overflow-hidden">
                    <button type="button" class="faq-btn w-full p-6 text-left flex items-center justify-between gap-4 font-bold text-brandDark text-sm sm:text-base hover:text-brandOrange transition-colors" aria-expanded="false">
                        <span>Is this suitable for someone struggling with ADHD or intense brain chatter?</span>
                        <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 transition-transform duration-200"></i>
                    </button>
                    <div class="faq-content hidden px-6 pb-6 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-4">
                        Absolutely. Brain Yoga incorporates cross-body coordination, bilateral stimulation, and physical anchoring specifically designed for minds that find traditional silent meditation difficult or frustrating.
                    </div>
                </div>

                <div class="rounded-2xl border border-orange-200/80 bg-white shadow-xs overflow-hidden">
                    <button type="button" class="faq-btn w-full p-6 text-left flex items-center justify-between gap-4 font-bold text-brandDark text-sm sm:text-base hover:text-brandOrange transition-colors" aria-expanded="false">
                        <span>How do I get started with a free session?</span>
                        <i data-lucide="chevron-down" class="w-5 h-5 text-slate-400 transition-transform duration-200"></i>
                    </button>
                    <div class="faq-content hidden px-6 pb-6 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-4">
                        Simply click the "Book a FREE Introductory Session" button on this page or send a message directly on WhatsApp to +91 83319 29240. Our team will share the schedule and invite link.
                    </div>
                </div>

            </div>

        </div>
    </section>"""
    html = re.sub(faq_pattern, new_faq, html, flags=re.DOTALL)

    # 13. Section 12 (Final CTA): Light Teal Blue (#E6F7F8)
    cta_pattern = r'<section id="cta"[^>]*>.*?</section>'
    new_cta = """    <!-- ========================================================================= -->
    <!-- SECTION 12: FINAL CALL TO ACTION — Background: Light Teal Blue (#E6F7F8)  -->
    <!-- ========================================================================= -->
    <section id="cta" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#E6F7F8] border-b border-teal-200/70">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="by-card p-8 sm:p-14 text-center bg-white shadow-xl border border-teal-200 space-y-6">
                
                <div class="inline-flex items-center gap-2 bg-[#FFE8DA] px-4 py-1.5 rounded-full border border-orange-200/80 shadow-xs">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span class="text-xs font-bold uppercase tracking-widest text-brandOrange">Begin Your Practice</span>
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
    html = re.sub(cta_pattern, new_cta, html, flags=re.DOTALL)

    return html

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_c = update_sections(c)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f"Applied perfect alternating light harmony to: {filepath}")

