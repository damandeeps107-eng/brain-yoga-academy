import re

files = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html'
]

def update_page(content):
    # 1. Update Tailwind config & CSS variables:
    # Set brandTeal to #007984, brandTealIce to #D2F0FF (exact from kids.html)
    content = content.replace("brandTealLight: '#E6F7F8'", "brandTealLight: '#D2F0FF'")
    content = content.replace("background-color: #E6F7F8;", "background-color: #D2F0FF;")

    # 2. Top Banner: Rich Signature Teal #007984 with White Text
    content = re.sub(
        r'<aside aria-label="Program Announcement" class="[^"]*">',
        '<aside aria-label="Program Announcement" class="bg-[#007984] py-2 px-4 text-center text-xs font-semibold text-white shadow-xs">',
        content
    )

    # 3. Section 2 (Challenges): Clean White Background with Authentic #D2F0FF (Ice Teal Blue) Cards matching kids.html
    challenges_pattern = r'<section id="challenges"[^>]*>.*?</section>'
    new_challenges = """    <!-- ========================================================================= -->
    <!-- SECTION 2: EVERYDAY CHALLENGES — Background: Clean White #FFFFFF           -->
    <!-- Authentic #D2F0FF (Ice Teal Blue) cards matching kids.html Section 3       -->
    <!-- ========================================================================= -->
    <section id="challenges" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-white border-b border-slate-200">
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

            <!-- 9 Relatable Trigger Cards in Exact #D2F0FF Ice Teal Blue from kids.html -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-5 rounded-xl bg-[#D2F0FF] border-2 border-transparent hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                        <i data-lucide="compass" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Constant Distraction</h3>
                        <p class="text-xs text-slate-700 leading-relaxed">Struggling to stay focused while working or studying?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-[#D2F0FF] border-2 border-transparent hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                        <i data-lucide="smartphone" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Compulsive Phone Checking</h3>
                        <p class="text-xs text-slate-700 leading-relaxed">Reaching for your phone repeatedly without realizing it?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-[#D2F0FF] border-2 border-transparent hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                        <i data-lucide="battery-low" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Energy Crash by Afternoon</h3>
                        <p class="text-xs text-slate-700 leading-relaxed">Starting your day motivated, but running on empty by mid-afternoon?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-[#D2F0FF] border-2 border-transparent hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                        <i data-lucide="zap" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Frequent Irritation</h3>
                        <p class="text-xs text-slate-700 leading-relaxed">Getting easily irritated, stressed, or emotionally drained by small interruptions?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-[#D2F0FF] border-2 border-transparent hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                        <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Overthinking at Bedtime</h3>
                        <p class="text-xs text-slate-700 leading-relaxed">Replaying conversations, tasks, and worries long after the workday is done?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-[#D2F0FF] border-2 border-transparent hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                        <i data-lucide="monitor" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Digital Brain Fog</h3>
                        <p class="text-xs text-slate-700 leading-relaxed">Back-to-back meetings, chats, and tabs leaving your mind buzzing and scattered?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-[#D2F0FF] border-2 border-transparent hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                        <i data-lucide="repeat" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Routine Resistance</h3>
                        <p class="text-xs text-slate-700 leading-relaxed">Knowing you should pause or stretch, but trapped in the cycle of "one more task"?</p>
                    </div>
                </div>

                <div class="p-5 rounded-xl bg-[#D2F0FF] border-2 border-transparent hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                        <i data-lucide="coffee" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Restless Rest</h3>
                        <p class="text-xs text-slate-700 leading-relaxed">Even on weekends, your mind stays locked in work mode and emergency readiness?</p>
                    </div>
                </div>

                <div class="md:col-span-2 p-5 rounded-xl bg-[#D2F0FF] border-2 border-transparent hover:border-[#007984] hover:shadow-md transition-all flex items-start gap-4 shadow-xs">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange text-white flex items-center justify-center flex-shrink-0 mt-0.5 shadow-xs">
                        <i data-lucide="sparkles" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-brandDark mb-1">Capable, But Constantly Operating at Mental Capacity</h3>
                        <p class="text-xs text-slate-700 leading-relaxed">You handle your responsibilities well — but beneath the surface, your nervous system is in a state of unending overdrive.</p>
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
    content = re.sub(challenges_pattern, new_challenges, content, flags=re.DOTALL)

    # 4. Section 4 (What is Brain Yoga / About): Clean White Background with #007984 and #D2F0FF
    about_pattern = r'<section id="about"[^>]*>.*?</section>'
    new_about = """    <!-- ========================================================================= -->
    <!-- SECTION 4: WHAT IS BRAIN YOGA — Background: Clean White #FFFFFF            -->
    <!-- Matching kids.html Section 5 ("How Does Brain Balance Help?")              -->
    <!-- ========================================================================= -->
    <section id="about" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-white border-b border-slate-200">
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

            <!-- 4-Pillar Graphic Architecture (Exact colors #D2F0FF and #FFE8DA) -->
            <div class="mb-14 p-8 rounded-2xl bg-slate-50 border border-slate-200 shadow-xs">
                <div class="text-center mb-8">
                    <span class="text-[11px] font-bold uppercase tracking-wider text-brandOrange bg-[#FFE8DA] px-3 py-1 rounded-md border border-brandOrange/20 shadow-xs">
                        The 4-Pillar Mind-Reset Arc
                    </span>
                    <h3 class="text-lg font-bold text-brandDark mt-2">A Complete, Practical Loop for Mental Clarity</h3>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="p-6 rounded-xl bg-[#D2F0FF] border border-[#007984]/25 text-center hover:shadow-md transition-all">
                        <div class="w-12 h-12 mx-auto rounded-xl bg-[#007984] text-white flex items-center justify-center font-bold text-base mb-3 shadow-xs">01</div>
                        <h4 class="font-bold text-brandDark text-sm mb-1.5">Brain-Training Activities</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">Break habitual mental autopilot and stimulate neuroplastic pathways.</p>
                    </div>

                    <div class="p-6 rounded-xl bg-[#FFE8DA] border border-orange-200/80 text-center hover:shadow-md transition-all">
                        <div class="w-12 h-12 mx-auto rounded-xl bg-[#FD8742] text-white flex items-center justify-center font-bold text-base mb-3 shadow-xs">02</div>
                        <h4 class="font-bold text-brandDark text-sm mb-1.5">Mindful Movements</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">Release physical stiffness and ground attention back into the body.</p>
                    </div>

                    <div class="p-6 rounded-xl bg-[#D2F0FF] border border-[#007984]/25 text-center hover:shadow-md transition-all">
                        <div class="w-12 h-12 mx-auto rounded-xl bg-[#007984] text-white flex items-center justify-center font-bold text-base mb-3 shadow-xs">03</div>
                        <h4 class="font-bold text-brandDark text-sm mb-1.5">Breathing Practices</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">Downshift the sympathetic nervous system and soothe stress spikes.</p>
                    </div>

                    <div class="p-6 rounded-xl bg-[#FFE8DA] border border-orange-200/80 text-center hover:shadow-md transition-all">
                        <div class="w-12 h-12 mx-auto rounded-xl bg-[#FD8742] text-white flex items-center justify-center font-bold text-base mb-3 shadow-xs">04</div>
                        <h4 class="font-bold text-brandDark text-sm mb-1.5">Inner Stillness & Meditation</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">Cultivate unshakeable focus and non-reactive cognitive spaciousness.</p>
                    </div>
                </div>
            </div>

            <!-- 3 Mind-Body Connection Pillars -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="by-card p-6 bg-white border border-slate-200 shadow-xs hover:border-[#007984] transition-colors">
                    <div class="w-10 h-10 rounded-lg bg-[#D2F0FF] text-[#007984] flex items-center justify-center mb-4">
                        <i data-lucide="brain" class="w-5 h-5"></i>
                    </div>
                    <h3 class="text-base font-bold text-brandDark mb-2">Notice Thoughts Early</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Recognize spiraling thoughts before they hijack your focus, conversations, or evening rest.
                    </p>
                </div>

                <div class="by-card p-6 bg-white border border-slate-200 shadow-xs hover:border-[#007984] transition-colors">
                    <div class="w-10 h-10 rounded-lg bg-[#FFE8DA] text-brandOrange flex items-center justify-center mb-4">
                        <i data-lucide="heart-pulse" class="w-5 h-5"></i>
                    </div>
                    <h3 class="text-base font-bold text-brandDark mb-2">Soothe Emotional Surges</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Build an internal buffer against urgency, deadline panic, and workplace friction.
                    </p>
                </div>

                <div class="by-card p-6 bg-white border border-slate-200 shadow-xs hover:border-[#007984] transition-colors">
                    <div class="w-10 h-10 rounded-lg bg-[#D2F0FF] text-[#007984] flex items-center justify-center mb-4">
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
    content = re.sub(about_pattern, new_about, content, flags=re.DOTALL)

    # 5. Section 6 (Benefits / Gains): EXACT TEAL BLUE #007984 BACKGROUND matching kids.html Section 6 ("Outcomes That Matter Beyond Academics")
    benefits_pattern = r'<section id="benefits"[^>]*>.*?</section>'
    new_benefits = """    <!-- ========================================================================= -->
    <!-- SECTION 6: BENEFITS — Exact Signature Teal Blue #007984 Background        -->
    <!-- Matching kids.html Section 6 ("Outcomes That Matter Beyond Academics")     -->
    <!-- ========================================================================= -->
    <section id="benefits" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#007984] text-white border-b border-teal-900/40">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="inline-flex items-center gap-2 bg-white/15 px-4 py-1.5 rounded-full border border-white/20 mb-4 backdrop-blur-xs">
                    <span class="w-2 h-2 rounded-full bg-amber-300"></span>
                    <span class="text-xs font-bold uppercase tracking-widest text-white">Sustainable Benefits</span>
                </div>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
                    What Regular Practice <span class="text-amber-300">Can Build</span>
                </h2>
                <p class="text-sm sm:text-base text-teal-100 mt-3 max-w-2xl mx-auto leading-relaxed">
                    Participants may gradually develop:
                </p>
            </div>

            <!-- 6 Pure White Benefit Cards with Teal Checkmark Badges -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-5 rounded-xl bg-white text-slate-800 flex items-center gap-4 shadow-md border border-teal-100">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Greater awareness of stress triggers and habitual reactions.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white text-slate-800 flex items-center gap-4 shadow-md border border-teal-100">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Improved ability to pause before reacting in challenging situations.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white text-slate-800 flex items-center gap-4 shadow-md border border-teal-100">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Practical tools to reset attention and reduce mental fatigue during work.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white text-slate-800 flex items-center gap-4 shadow-md border border-teal-100">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Simple techniques to support emotional balance and calm.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white text-slate-800 flex items-center gap-4 shadow-md border border-teal-100">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Mindful work habits that protect focus and personal well-being.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-white text-slate-800 flex items-center gap-4 shadow-md border border-teal-100">
                    <div class="w-9 h-9 rounded-lg bg-[#007984] text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Healthier boundaries with screens, notifications, and workplace urgency.
                    </p>
                </div>
            </div>

            <!-- Neuroplasticity Box -->
            <div class="mt-8 p-6 rounded-2xl bg-white/10 border border-white/20 shadow-xs flex items-center gap-4 backdrop-blur-xs">
                <div class="w-10 h-10 rounded-full bg-white text-[#007984] flex items-center justify-center flex-shrink-0 shadow-xs">
                    <i data-lucide="sparkles" class="w-5 h-5"></i>
                </div>
                <div>
                    <h4 class="text-sm font-bold text-white">Rooted in Neuroplasticity & Habit Formation</h4>
                    <p class="text-xs text-teal-100 mt-0.5">Brain Yoga trains your brain to break automatic stress responses and replace them with deliberate, conscious choices.</p>
                </div>
            </div>

        </div>
    </section>"""
    content = re.sub(benefits_pattern, new_benefits, content, flags=re.DOTALL)

    # 6. Section 8 (Corporate Workshops): EXACT TEAL BLUE #007984 BACKGROUND matching kids.html Section 12 ("Workshop Details")
    corporate_pattern = r'<section id="corporate"[^>]*>.*?</section>'
    new_corporate = """    <!-- ========================================================================= -->
    <!-- SECTION 8: CORPORATE WORKSHOPS — Exact Signature Teal Blue #007984         -->
    <!-- Matching kids.html Section 12 ("Workshop Details") with crisp white cards  -->
    <!-- ========================================================================= -->
    <section id="corporate" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#007984] text-white border-b border-teal-900/40">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="inline-flex items-center gap-2 bg-white/15 px-4 py-1.5 rounded-full border border-white/20 mb-4 backdrop-blur-xs">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span class="text-xs font-bold uppercase tracking-widest text-white">Corporate Brain Yoga Workshops</span>
                </div>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
                    Bring Brain Yoga to <span class="text-amber-300">Your Workplace</span>
                </h2>
                <p class="text-sm sm:text-base text-teal-100 mt-3 max-w-2xl mx-auto leading-relaxed">
                    Bring Brain Yoga to your startup, IT team, business network, or organization. Our interactive workshops combine engaging brain-training activities with practical techniques that employees can incorporate into their daily lives.
                </p>
            </div>

            <!-- 4 Formats: Crisp White Cards on Signature Teal Blue Background -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                
                <div class="by-card p-6 bg-white text-slate-800 shadow-xl border border-teal-100">
                    <div class="text-xs font-bold text-[#007984] uppercase tracking-wider mb-2">Express Break</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">30 to 45-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Introductory session designed for team all-hands, energizer breaks, or wellness kickoffs.
                    </p>
                </div>

                <div class="by-card p-6 bg-white text-slate-800 shadow-2xl border-2 border-brandOrange relative">
                    <span class="absolute -top-3 right-4 text-[10px] font-bold uppercase tracking-wider bg-brandOrange text-white px-2.5 py-0.5 rounded-full shadow-xs">Popular</span>
                    <div class="text-xs font-bold text-brandOrange uppercase tracking-wider mb-2">Interactive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">60 to 90-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Interactive workshop with live practice, breathing, tapping, and desk-friendly resets.
                    </p>
                </div>

                <div class="by-card p-6 bg-white text-slate-800 shadow-xl border border-teal-100">
                    <div class="text-xs font-bold text-[#007984] uppercase tracking-wider mb-2">Intensive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Half-Day Workshop</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        In-depth training for leadership offsites, retreats, and high-performance teams.
                    </p>
                </div>

                <div class="by-card p-6 bg-white text-slate-800 shadow-xl border border-teal-100">
                    <div class="text-xs font-bold text-[#007984] uppercase tracking-wider mb-2">Sustained</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Multi-Session Program</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Weekly or monthly structured wellness journey for long-term stress resilience.
                    </p>
                </div>

            </div>

            <!-- Topics Cloud (Clean White Badges) -->
            <div class="p-6 sm:p-8 rounded-2xl bg-white/10 border border-white/20 mb-10 shadow-sm backdrop-blur-xs">
                <h4 class="text-sm font-bold text-white uppercase tracking-wider mb-4 text-center">
                    Workshop Topics May Include:
                </h4>
                <div class="flex flex-wrap justify-center gap-2.5 sm:gap-3">
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-xs">Focus and Attention</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-xs">Stress Awareness</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-xs">Emotional Balance</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-xs">Mindful Work Habits</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-xs">Desk-Friendly Movement</span>
                    <span class="bg-white text-slate-800 text-xs font-bold px-4 py-2 rounded-lg shadow-xs">Digital Detox Micro-Habits</span>
                </div>
            </div>

            <!-- Corporate Action CTAs -->
            <div class="text-center space-y-4">
                <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                    <button onclick="openModal('corporateModal')" class="by-btn-primary shadow-xl">
                        <i data-lucide="file-text" class="w-4 h-4"></i>
                        <span>Request a Corporate Proposal</span>
                    </button>
                    <a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20we%20want%20to%20schedule%20a%2015-minute%20discussion%20about%20a%20Corporate%20Brain%20Yoga%20Workshop." target="_blank" class="inline-flex items-center justify-center gap-2 px-7 py-3.5 rounded-lg bg-white/15 hover:bg-white/25 text-white font-bold text-sm border border-white/40 shadow-sm transition-all">
                        <i data-lucide="message-square" class="w-4 h-4"></i>
                        <span>Schedule a 15-Minute Discussion</span>
                    </a>
                </div>
                <p class="text-xs text-teal-100">
                    Customized proposals delivered within 24 hours. Online and in-person delivery available.
                </p>
            </div>

        </div>
    </section>"""
    content = re.sub(corporate_pattern, new_corporate, content, flags=re.DOTALL)

    # 7. Section 10 (Testimonials): EXACT TEAL BLUE #007984 BACKGROUND matching kids.html Section 9 ("Transformation Stories")
    testimonials_pattern = r'<section id="testimonials"[^>]*>.*?</section>'
    new_testimonials = """    <!-- ========================================================================= -->
    <!-- SECTION 10: TESTIMONIALS — Exact Signature Teal Blue #007984 Background   -->
    <!-- Matching kids.html Section 9 ("Transformation Stories") with white cards  -->
    <!-- ========================================================================= -->
    <section id="testimonials" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#007984] text-white border-b border-teal-900/40">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="inline-flex items-center gap-2 bg-white/15 px-4 py-1.5 rounded-full border border-white/20 mb-4 backdrop-blur-xs">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span class="text-xs font-bold uppercase tracking-widest text-white">Real Experiences</span>
                </div>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
                    What <span class="text-amber-300">Participants Say</span>
                </h2>
                <p class="text-sm sm:text-base text-teal-100 mt-3 max-w-2xl mx-auto leading-relaxed">
                    Real experiences from busy professionals who made mind-wellness a daily habit.
                </p>
            </div>

            <!-- 6 Testimonial Cards: Crisp White on Signature Teal Blue #007984 -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                
                <!-- 1. Uma Maheswari -->
                <div class="by-card p-6 bg-white text-slate-800 border border-teal-100 shadow-xl flex flex-col justify-between">
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
                <div class="by-card p-6 bg-white text-slate-800 border border-teal-100 shadow-xl flex flex-col justify-between">
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
                <div class="by-card p-6 bg-white text-slate-800 border border-teal-100 shadow-xl flex flex-col justify-between">
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
                <div class="by-card p-6 bg-white text-slate-800 border border-teal-100 shadow-xl flex flex-col justify-between">
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
                <div class="by-card p-6 bg-white text-slate-800 border border-teal-100 shadow-xl flex flex-col justify-between">
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
                <div class="by-card p-6 bg-white text-slate-800 border border-teal-100 shadow-xl flex flex-col justify-between">
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
    content = re.sub(testimonials_pattern, new_testimonials, content, flags=re.DOTALL)

    # 8. Section 12 (Final CTA): EXACT TEAL BLUE #007984 BACKGROUND
    cta_pattern = r'<section id="cta"[^>]*>.*?</section>'
    new_cta = """    <!-- ========================================================================= -->
    <!-- SECTION 12: FINAL CALL TO ACTION — Exact Signature Teal Blue #007984       -->
    <!-- ========================================================================= -->
    <section id="cta" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-[#007984] border-b border-teal-900/40">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="by-card p-8 sm:p-14 text-center bg-white shadow-2xl border border-teal-200 space-y-6">
                
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
    content = re.sub(cta_pattern, new_cta, content, flags=re.DOTALL)

    return content

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    new_c = update_page(c)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_c)
    print(f'Applied exact Children Teal Blue (#007984 & #D2F0FF) to: {fpath}')

