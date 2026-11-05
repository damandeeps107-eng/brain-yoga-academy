import re

files = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html'
]

white_footer = """    <!-- ========================================================================= -->
    <!-- SECTION 13: COMPREHENSIVE WHITE FOOTER (bg-white)                         -->
    <!-- All Section Links, Social Links (Instagram & Facebook), WhatsApp & Rights  -->
    <!-- ========================================================================= -->
    <footer id="footer" class="bg-white border-t border-slate-200 text-slate-600 text-xs py-14 sm:py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <!-- 4-Column Structured Footer Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 lg:gap-12 pb-12 border-b border-slate-200">
                
                <!-- Col 1: Brand Info & Social Links (lg:col-span-4) -->
                <div class="lg:col-span-4 space-y-4">
                    <a href="#" class="inline-flex items-center gap-2">
                        <img src="official_logo.png" alt="Brain Yoga Academy" class="h-10 sm:h-11 w-auto object-contain">
                    </a>
                    <p class="text-xs text-slate-600 leading-relaxed max-w-sm">
                        Practical Mind-Wellness & Neuro-Movement for Adults, Working Professionals, and Corporate Organizations. Founded by Rajendra Boddu.
                    </p>
                    
                    <!-- Direct WhatsApp Connect Banner -->
                    <div class="pt-1">
                        <a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20I%20want%20to%20know%20more%20about%20Brain%20Yoga%20for%20Busy%20Minds." target="_blank" class="inline-flex items-center gap-2.5 px-3.5 py-2 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200 hover:bg-emerald-100 font-bold text-xs transition-colors shadow-2xs">
                            <i data-lucide="message-circle" class="w-4 h-4 text-emerald-600"></i>
                            <span>WhatsApp: +91 83319 29240</span>
                        </a>
                    </div>

                    <!-- Social Icons (Instagram, Facebook, Phone, Email) -->
                    <div class="pt-1 flex items-center gap-3">
                        <!-- Instagram -->
                        <a href="https://www.instagram.com/brain_yoga_academy?utm_source=ig_web_button_share_sheet&srtk=ZDNlZDc0MzIxNw==" target="_blank" rel="noopener noreferrer" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-gradient-to-tr hover:from-amber-500 hover:via-rose-500 hover:to-purple-600 hover:text-white text-slate-700 flex items-center justify-center transition-all shadow-xs" aria-label="Brain Yoga Academy Instagram">
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                        </a>

                        <!-- Facebook -->
                        <a href="https://www.facebook.com/brainyogaacademy" target="_blank" rel="noopener noreferrer" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-[#1877F2] hover:text-white text-slate-700 flex items-center justify-center transition-all shadow-xs" aria-label="Brain Yoga Academy Facebook">
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"/></svg>
                        </a>

                        <!-- Phone Direct -->
                        <a href="tel:+918331929240" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-[#007984] hover:text-white text-slate-700 flex items-center justify-center transition-all shadow-xs" aria-label="Call Rajendra Boddu">
                            <i data-lucide="phone" class="w-4 h-4"></i>
                        </a>

                        <!-- Email Direct -->
                        <a href="mailto:rajendraboddu@gmail.com" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-[#FD8742] hover:text-white text-slate-700 flex items-center justify-center transition-all shadow-xs" aria-label="Email Rajendra Boddu">
                            <i data-lucide="mail" class="w-4 h-4"></i>
                        </a>
                    </div>
                </div>

                <!-- Col 2: Program Navigation (lg:col-span-3) -->
                <div class="lg:col-span-3 space-y-3">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-brandDark">
                        Program Sections
                    </h4>
                    <ul class="space-y-2 text-xs">
                        <li>
                            <a href="#challenges" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandTeal"></span>
                                <span>Everyday Reality Check</span>
                            </a>
                        </li>
                        <li>
                            <a href="#shift" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandOrange"></span>
                                <span>The Shift (1 Barking Dog)</span>
                            </a>
                        </li>
                        <li>
                            <a href="#about" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandTeal"></span>
                                <span>What is Brain Yoga?</span>
                            </a>
                        </li>
                        <li>
                            <a href="#practices" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandOrange"></span>
                                <span>Our 8 Practices & Techniques</span>
                            </a>
                        </li>
                        <li>
                            <a href="#benefits" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandTeal"></span>
                                <span>What Regular Practice Builds</span>
                            </a>
                        </li>
                        <li>
                            <a href="#how-it-works" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandOrange"></span>
                                <span>How the Program Works</span>
                            </a>
                        </li>
                    </ul>
                </div>

                <!-- Col 3: Workshops & About (lg:col-span-3) -->
                <div class="lg:col-span-3 space-y-3">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-brandDark">
                        Workshops & Trainer
                    </h4>
                    <ul class="space-y-2 text-xs">
                        <li>
                            <a href="#corporate" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandTeal"></span>
                                <span>Corporate Workshops</span>
                            </a>
                        </li>
                        <li>
                            <a href="#trainer" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandOrange"></span>
                                <span>Meet Rajendra Boddu</span>
                            </a>
                        </li>
                        <li>
                            <a href="#testimonials" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandTeal"></span>
                                <span>Participant Experiences</span>
                            </a>
                        </li>
                        <li>
                            <a href="#faq" class="text-slate-600 hover:text-brandTeal transition-colors flex items-center gap-1.5">
                                <span class="w-1.5 h-1.5 rounded-full bg-brandOrange"></span>
                                <span>Frequently Asked Questions</span>
                            </a>
                        </li>
                        <li class="pt-2">
                            <a href="kids.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-md bg-[#FFE8DA] text-brandOrange font-bold text-[11px] border border-orange-200/80 hover:bg-brandOrange hover:text-white transition-all shadow-2xs">
                                <span>🧒 Brain Yoga for Children</span>
                                <i data-lucide="arrow-up-right" class="w-3.5 h-3.5"></i>
                            </a>
                        </li>
                    </ul>
                </div>

                <!-- Col 4: Quick Contact Details (lg:col-span-2) -->
                <div class="lg:col-span-2 space-y-3">
                    <h4 class="text-xs font-bold uppercase tracking-wider text-brandDark">
                        Contact Details
                    </h4>
                    <div class="space-y-2.5 text-xs text-slate-600">
                        <div>
                            <p class="font-bold text-slate-800">WhatsApp / Call:</p>
                            <a href="https://wa.me/918331929240" target="_blank" class="text-brandTeal hover:underline font-semibold block mt-0.5">
                                +91 83319 29240
                            </a>
                        </div>
                        <div>
                            <p class="font-bold text-slate-800">Email:</p>
                            <a href="mailto:rajendraboddu@gmail.com" class="text-brandTeal hover:underline block mt-0.5 truncate">
                                rajendraboddu@gmail.com
                            </a>
                        </div>
                        <div>
                            <p class="font-bold text-slate-800">Location:</p>
                            <p class="text-slate-600 mt-0.5 leading-relaxed">
                                Hyderabad, India<br>
                                <span class="text-[11px] text-slate-500">(Online & On-site across India)</span>
                            </p>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Bottom Copyright Bar -->
            <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left text-xs text-slate-500">
                <div>
                    &copy; 2026 <strong>Brain Yoga Academy</strong>. All Rights Reserved.
                </div>
                <div class="flex flex-wrap items-center justify-center gap-4 text-[11px]">
                    <a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20I%20have%20an%20enquiry." target="_blank" class="hover:text-brandTeal transition-colors">Contact Support</a>
                    <span>•</span>
                    <a href="#about" class="hover:text-brandTeal transition-colors">Program Philosophy</a>
                    <span>•</span>
                    <a href="kids.html" class="hover:text-brandTeal transition-colors">Children's Academy</a>
                </div>
            </div>

        </div>
    </footer>"""

footer_pattern = r'<footer id="footer"[^>]*>.*?</footer>'

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(footer_pattern, white_footer, content, flags=re.DOTALL)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully built clean white footer in: {fpath}')

