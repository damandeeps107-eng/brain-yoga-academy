# Script to upgrade Section 3 (Shift in Perspective) and polish page aesthetics
import os
import re

files = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html'
]

upgraded_shift_html = """    <!-- ========================================================================= -->
    <!-- SECTION 3: A SIMPLE SHIFT IN PERSPECTIVE — Background: Warm Peach #FFF3EB -->
    <!-- Upgraded: Executive Mindset Transformation (No emojis, high-end polish)    -->
    <!-- ========================================================================= -->
    <section id="shift" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <!-- Section Header -->
            <div class="text-center max-w-3xl mx-auto mb-12 sm:mb-16">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>A Simple Shift in Perspective</span>
                </div>
                <h2 class="main-heading">
                    10 People. 1 Barking Dog. <br class="hidden sm:inline">
                    <span style="color: #FD8742;">What Makes the Difference?</span>
                </h2>
                <p class="sub-heading font-medium text-slate-700">
                    Imagine 10 people walking down a street. Suddenly, a dog starts barking at them.
                </p>
            </div>

            <!-- The 5 Reactions: Premium Cards with Professional Icons (NO juvenile emojis) -->
            <div class="grid grid-cols-2 sm:grid-cols-5 gap-3 sm:gap-4 mb-10">
                
                <!-- Reaction 1 -->
                <div class="by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between">
                    <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center mb-3 border border-amber-200/60 shadow-2xs">
                        <i data-lucide="flame" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest block mb-1">Reaction 01</span>
                        <p class="text-xs sm:text-sm font-bold text-slate-800">Some get irritated</p>
                    </div>
                </div>

                <!-- Reaction 2 -->
                <div class="by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between">
                    <div class="w-10 h-10 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center mb-3 border border-rose-200/60 shadow-2xs">
                        <i data-lucide="shield-alert" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest block mb-1">Reaction 02</span>
                        <p class="text-xs sm:text-sm font-bold text-slate-800">Some feel frightened</p>
                    </div>
                </div>

                <!-- Reaction 3 -->
                <div class="by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between">
                    <div class="w-10 h-10 rounded-xl bg-orange-50 text-brandOrange flex items-center justify-center mb-3 border border-brandOrange/25 shadow-2xs">
                        <i data-lucide="volume-2" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest block mb-1">Reaction 03</span>
                        <p class="text-xs sm:text-sm font-bold text-slate-800">Some shout at the dog</p>
                    </div>
                </div>

                <!-- Reaction 4 -->
                <div class="by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between">
                    <div class="w-10 h-10 rounded-xl bg-slate-100 text-slate-600 flex items-center justify-center mb-3 border border-slate-200 shadow-2xs">
                        <i data-lucide="footprints" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest block mb-1">Reaction 04</span>
                        <p class="text-xs sm:text-sm font-bold text-slate-800">Some simply walk away</p>
                    </div>
                </div>

                <!-- Reaction 5 (The Mindful Response) -->
                <div class="col-span-2 sm:col-span-1 by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between bg-gradient-to-b from-brandTealLight to-white border-2 border-brandTeal shadow-md">
                    <div class="w-10 h-10 rounded-xl bg-brandTeal text-white flex items-center justify-center mb-3 shadow-sm">
                        <i data-lucide="sparkles" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-brandTeal uppercase tracking-widest block mb-1">Mindful State</span>
                        <p class="text-xs sm:text-sm font-bold text-brandDark">And some don't even react</p>
                    </div>
                </div>

            </div>

            <!-- The Cognitive Transformation Framework: Reaction vs Response -->
            <div class="by-card p-6 sm:p-10 lg:p-12 mb-10">
                <div class="text-center max-w-2xl mx-auto mb-8">
                    <span class="text-xs font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-3 py-1 rounded-full border border-brandTeal/20">
                        The Core Insight
                    </span>
                    <h3 class="text-xl sm:text-2xl font-bold text-brandDark mt-3">
                        Same dog. Same situation. Different reactions.
                    </h3>
                    <p class="text-sm sm:text-base text-slate-600 mt-2">
                        <strong>It's not always the situation. It's how we perceive and respond to it.</strong>
                    </p>
                </div>

                <!-- Side-by-Side Mental Shift Visual -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8 items-stretch">
                    
                    <!-- Left: Automatic Reaction -->
                    <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
                        <div>
                            <div class="flex items-center justify-between mb-4">
                                <span class="text-xs font-bold uppercase tracking-wider text-rose-600 bg-rose-50 px-2.5 py-1 rounded-md border border-rose-200">
                                    Default Habit
                                </span>
                                <i data-lucide="zap-off" class="w-5 h-5 text-rose-400"></i>
                            </div>
                            <h4 class="text-lg font-bold text-brandDark mb-2">Automatic Reaction</h4>
                            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                                External events immediately dictate your stress level. Instant irritation, defensive responses, emotional exhaustion, and reactive decisions.
                            </p>
                        </div>
                        <div class="mt-4 pt-3 border-t border-slate-200 text-xs font-semibold text-slate-500 flex items-center gap-2">
                            <span class="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
                            <span>Trigger ➔ Immediate Impulse</span>
                        </div>
                    </div>

                    <!-- Right: Conscious Response (Brain Yoga) -->
                    <div class="p-6 rounded-2xl bg-brandTealLight/40 border-2 border-brandTeal/40 flex flex-col justify-between relative shadow-sm">
                        <div>
                            <div class="flex items-center justify-between mb-4">
                                <span class="text-xs font-bold uppercase tracking-wider text-brandTeal bg-white px-2.5 py-1 rounded-md border border-brandTeal/20">
                                    Brain Yoga Shift
                                </span>
                                <i data-lucide="check-circle" class="w-5 h-5 text-brandTeal"></i>
                            </div>
                            <h4 class="text-lg font-bold text-brandDark mb-2">Conscious Response</h4>
                            <p class="text-xs sm:text-sm text-slate-700 font-medium leading-relaxed">
                                A trained micro-pause between trigger and action. You observe the situation calmly, recognize your thoughts, and respond with intentional composure.
                            </p>
                        </div>
                        <div class="mt-4 pt-3 border-t border-brandTeal/20 text-xs font-bold text-brandTeal flex items-center gap-2">
                            <span class="w-1.5 h-1.5 rounded-full bg-brandTeal"></span>
                            <span>Trigger ➔ Mindful Pause ➔ Intentional Response</span>
                        </div>
                    </div>

                </div>

                <!-- Epiphany Quote Banner (Verbatim from Rajendra Boddu's Document) -->
                <div class="mt-8 p-5 sm:p-6 rounded-xl bg-gradient-to-r from-brandDark to-slate-900 text-white text-center shadow-md">
                    <p class="text-xs sm:text-sm font-medium text-slate-300 mb-1">The Fundamental Truth:</p>
                    <p class="text-lg sm:text-2xl font-extrabold text-brandOrange tracking-tight">
                        "It's never just the dog. It's the mindset."
                    </p>
                    <p class="text-xs sm:text-sm text-slate-300 mt-2 max-w-xl mx-auto leading-relaxed">
                        Your situations may not always be under your control. But with awareness and practice, you can learn to respond differently.
                    </p>
                    <div class="pt-4">
                        <button onclick="openModal('individualModal')" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-brandOrange hover:bg-brandOrangeDark text-white text-xs sm:text-sm font-bold shadow-md transition-all">
                            <span>Experience this shift in a session</span>
                            <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>

            </div>

        </div>
    </section>"""

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Section 3 (Shift)
    pattern = r'<section id="shift".*?</section>'
    new_content, count = re.subn(pattern, upgraded_shift_html, content, flags=re.DOTALL)
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully upgraded Section 3 in: {filepath}")
    else:
        print(f"Section 3 pattern not matched in: {filepath}")
