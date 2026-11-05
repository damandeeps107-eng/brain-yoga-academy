# Upgrade Section 3 with Illustration and Expressive Emojis
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
    <!-- With Story Illustration, Expressive Emojis & Cognitive Framework          -->
    <!-- ========================================================================= -->
    <section id="shift" class="scroll-mt-24 lg:scroll-mt-28 py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <!-- Section Header -->
            <div class="text-center max-w-3xl mx-auto mb-10 sm:mb-14">
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

            <!-- Story Visual Illustration Card (Strictly NO text on top of image) -->
            <div class="by-card mb-10 overflow-hidden">
                <div class="aspect-[16/9] sm:aspect-[21/9] w-full bg-slate-100 overflow-hidden">
                    <img src="barking_dog_mindset_story.webp" alt="10 People and 1 Barking Dog - Mindset Metaphor" class="w-full h-full object-cover object-center" loading="lazy" decoding="async">
                </div>
                <div class="p-4 sm:p-5 bg-white border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
                    <div class="flex items-center gap-2">
                        <span class="text-xl">🐕</span>
                        <p class="text-xs sm:text-sm font-semibold text-slate-700">
                            <strong>The Situation:</strong> One stimulus. Ten individuals. Five completely different reactions.
                        </p>
                    </div>
                    <span class="text-[11px] font-bold text-brandTeal bg-brandTealLight px-3 py-1 rounded-full border border-brandTeal/20 whitespace-nowrap">
                        Perception vs Reality
                    </span>
                </div>
            </div>

            <!-- The 5 Reactions: Expressive Emojis + Professional Labels -->
            <div class="grid grid-cols-2 sm:grid-cols-5 gap-3 sm:gap-4 mb-10">
                
                <!-- Reaction 1 -->
                <div class="by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between hover:border-amber-400 transition-all">
                    <div class="w-12 h-12 rounded-2xl bg-amber-50 flex items-center justify-center mb-3 border border-amber-200 shadow-2xs">
                        <span class="text-2xl" role="img" aria-label="Irritated">😤</span>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-amber-700 uppercase tracking-wider block mb-1">Frustration</span>
                        <p class="text-xs sm:text-sm font-bold text-slate-800">Some get irritated</p>
                    </div>
                </div>

                <!-- Reaction 2 -->
                <div class="by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between hover:border-rose-400 transition-all">
                    <div class="w-12 h-12 rounded-2xl bg-rose-50 flex items-center justify-center mb-3 border border-rose-200 shadow-2xs">
                        <span class="text-2xl" role="img" aria-label="Frightened">😨</span>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-rose-700 uppercase tracking-wider block mb-1">Anxiety</span>
                        <p class="text-xs sm:text-sm font-bold text-slate-800">Some feel frightened</p>
                    </div>
                </div>

                <!-- Reaction 3 -->
                <div class="by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between hover:border-brandOrange transition-all">
                    <div class="w-12 h-12 rounded-2xl bg-orange-50 flex items-center justify-center mb-3 border border-brandOrange/30 shadow-2xs">
                        <span class="text-2xl" role="img" aria-label="Shouting">🗣️</span>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-brandOrangeDark uppercase tracking-wider block mb-1">Aggression</span>
                        <p class="text-xs sm:text-sm font-bold text-slate-800">Some shout at the dog</p>
                    </div>
                </div>

                <!-- Reaction 4 -->
                <div class="by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between hover:border-slate-400 transition-all">
                    <div class="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center mb-3 border border-slate-200 shadow-2xs">
                        <span class="text-2xl" role="img" aria-label="Walking away">🚶‍♂️</span>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-slate-600 uppercase tracking-wider block mb-1">Avoidance</span>
                        <p class="text-xs sm:text-sm font-bold text-slate-800">Some simply walk away</p>
                    </div>
                </div>

                <!-- Reaction 5 (Highlighted Brain Yoga Mindful State) -->
                <div class="col-span-2 sm:col-span-1 by-card p-4 sm:p-5 text-center flex flex-col items-center justify-between bg-gradient-to-b from-brandTealLight to-white border-2 border-brandTeal shadow-md">
                    <div class="w-12 h-12 rounded-2xl bg-brandTeal flex items-center justify-center mb-3 shadow-sm">
                        <span class="text-2xl" role="img" aria-label="Conscious calm">🧘‍♂️</span>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-brandTeal uppercase tracking-wider block mb-1">Mindful Composure</span>
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
                                <span class="text-lg">⚡</span>
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
                                <span class="text-lg">🌿</span>
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
        print(f"Successfully added image and emojis to Section 3 in: {filepath}")
    else:
        print(f"Section 3 pattern not matched in: {filepath}")
