import os

html_code = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brain Yoga for Busy Minds | Corporate Wellness & Mind-Wellness</title>
    <meta name="description" content="Discover practical Brain Yoga, mindful movement, breathing, meditation, and relaxation sessions for working professionals, adults, and corporate teams.">
    
    <!-- Open Graph Meta -->
    <meta property="og:title" content="Brain Yoga for Busy Minds | Corporate Wellness & Mind-Wellness">
    <meta property="og:description" content="Practical mind-wellness program for working professionals, entrepreneurs, and adults to pause, reset, and respond with greater awareness.">
    <meta property="og:image" content="rajindra_boddu_portrait.jpg">
    <meta property="og:type" content="website">

    <!-- Fonts: Poppins for Headings + Inter for Body (Exact Astra / Elementor match from kids.html) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap" rel="stylesheet">

    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brandTeal: '#007984',       // Exact Children BY primary teal
                        brandTealDark: '#085C65',   // Deep Teal
                        brandTealLight: '#E6F7F8',  // Soft Teal Tint
                        brandTealIce: '#D2F0FF',    // Exact Children BY ice blue card background
                        brandOrange: '#FD8742',     // Exact Children BY orange CTA
                        brandOrangeDark: '#D36005', // Exact Children BY dark orange
                        brandPeachLight: '#FFE8DA', // Exact Children BY peach card tint
                        brandPeachBg: '#FFF3EB',    // Exact Children BY soft warm peach background
                        brandDark: '#1F1F1F',       // Clean dark heading text
                        brandBody: '#334155',       // Clean, readable body text
                    },
                    fontFamily: {
                        heading: ['Poppins', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
                        body: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
                    }
                }
            }
        }
    </script>

    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>

    <style>
        /* Exact Typography Matching kids.html */
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 16px;
            line-height: 1.65;
            color: #334155;
            background-color: #FFFFFF;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            overflow-x: hidden;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Poppins', sans-serif;
            color: #1F1F1F;
            letter-spacing: -0.015em;
        }

        /* Clean Section Headers */
        .section-eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.35rem 1rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            background-color: #E6F7F8;
            color: #007984;
            border: 1px solid rgba(0, 121, 132, 0.2);
            margin-bottom: 0.85rem;
        }

        .section-eyebrow-orange {
            background-color: #FFE8DA;
            color: #D36005;
            border-color: rgba(253, 135, 66, 0.25);
        }

        .main-heading {
            font-size: 2rem;
            font-weight: 700;
            line-height: 1.25;
            color: #1F1F1F;
        }
        @media (min-width: 640px) {
            .main-heading {
                font-size: 2.5rem;
            }
        }
        @media (min-width: 1024px) {
            .main-heading {
                font-size: 2.85rem;
            }
        }

        .sub-heading {
            font-size: 1rem;
            line-height: 1.65;
            color: #475569;
            max-width: 42rem;
            margin-left: auto;
            margin-right: auto;
            margin-top: 0.75rem;
        }
        @media (min-width: 640px) {
            .sub-heading {
                font-size: 1.125rem;
            }
        }

        /* Elementor Standard Button Matching kids.html */
        .by-btn-primary {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            background-color: #FD8742;
            color: #FFFFFF;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 0.95rem;
            padding: 0.85rem 1.75rem;
            border-radius: 10px;
            box-shadow: 0 4px 14px rgba(253, 135, 66, 0.28);
            transition: all 0.25s ease;
        }
        .by-btn-primary:hover {
            background-color: #D36005;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(211, 96, 5, 0.35);
        }

        .by-btn-secondary {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            background-color: #FFFFFF;
            color: #007984;
            border: 2px solid #007984;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 0.95rem;
            padding: 0.85rem 1.75rem;
            border-radius: 10px;
            transition: all 0.25s ease;
        }
        .by-btn-secondary:hover {
            background-color: #E6F7F8;
            transform: translateY(-2px);
        }

        .by-btn-teal {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            background-color: #007984;
            color: #FFFFFF;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 0.95rem;
            padding: 0.85rem 1.75rem;
            border-radius: 10px;
            box-shadow: 0 4px 14px rgba(0, 121, 132, 0.28);
            transition: all 0.25s ease;
        }
        .by-btn-teal:hover {
            background-color: #085C65;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(8, 92, 101, 0.35);
        }

        /* Clean Unified Card Style */
        .by-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            box-shadow: 0 4px 20px -2px rgba(15, 37, 55, 0.05);
            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
            overflow: hidden;
        }
        .by-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 28px -4px rgba(0, 121, 132, 0.12);
            border-color: #007984;
        }

        /* Header blur */
        .glass-header {
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid #E2E8F0;
        }

        /* Modals */
        .modal-backdrop {
            background: rgba(15, 37, 55, 0.7);
            backdrop-filter: blur(6px);
        }

        /* WhatsApp pulse animation */
        @keyframes pulseWa {
            0%, 100% { transform: scale(1); box-shadow: 0 10px 25px -4px rgba(37, 211, 102, 0.4); }
            50% { transform: scale(1.05); box-shadow: 0 16px 35px 0px rgba(37, 211, 102, 0.65); }
        }
        .whatsapp-pulse-btn {
            animation: pulseWa 3.2s infinite ease-in-out;
        }
    </style>
</head>
<body class="selection:bg-brandOrange selection:text-white">

    <!-- ========================================================================= -->
    <!-- TOP NOTIFICATION BANNER: BRAIN YOGA FOR CHILDREN LINK -->
    <!-- ========================================================================= -->
    <aside aria-label="Program Announcement" class="bg-brandPeachLight border-b border-brandOrange/20 py-2.5 px-4 text-center text-xs font-medium text-slate-800">
        <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap">
            <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase bg-brandOrange text-white">
                Child Wellness
            </span>
            <span>Looking for our proven memory & concentration training for kids?</span>
            <a href="kids.html" class="inline-flex items-center gap-1 font-bold text-brandOrangeDark hover:underline transition-colors">
                <span>Visit Brain Yoga For Children</span>
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </a>
        </div>
    </aside>

    <!-- ========================================================================= -->
    <!-- TOP STICKY NAVBAR (With Official Logo) -->
    <!-- ========================================================================= -->
    <header class="sticky top-0 z-40 w-full glass-header shadow-sm transition-all">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
            <!-- Official Brand Logo -->
            <a href="busy-minds.html" class="flex items-center gap-3 group">
                <img src="official_logo.png" alt="Brain Yoga Academy" class="h-10 sm:h-12 w-auto object-contain">
                <span class="hidden sm:inline-block text-[11px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-1 rounded-md border border-brandTeal/20">
                    For Busy Minds
                </span>
            </a>

            <!-- Desktop Navigation Links -->
            <nav class="hidden lg:flex items-center gap-6 xl:gap-7 text-sm font-semibold text-slate-700">
                <a href="#about" class="hover:text-brandTeal transition-colors">About</a>
                <a href="#challenges" class="hover:text-brandTeal transition-colors">Everyday Challenges</a>
                <a href="#shift" class="hover:text-brandTeal transition-colors">Shift in Perspective</a>
                <a href="#practices" class="hover:text-brandTeal transition-colors">Our Practices</a>
                <a href="#benefits" class="hover:text-brandTeal transition-colors">Gains</a>
                <a href="#corporate" class="hover:text-brandTeal transition-colors">Corporate Workshops</a>
                <a href="#trainer" class="hover:text-brandTeal transition-colors">Your Trainer</a>
                <a href="#testimonials" class="hover:text-brandTeal transition-colors">Testimonials</a>
                <a href="#faq" class="hover:text-brandTeal transition-colors">FAQ</a>
            </nav>

            <!-- Action Buttons -->
            <div class="flex items-center gap-3">
                <a href="kids.html" class="hidden sm:inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-brandTealLight hover:bg-brandTealIce text-brandTeal text-xs font-bold border border-brandTeal/20 transition-all">
                    <span>Brain Yoga For Children</span>
                    <i data-lucide="arrow-up-right" class="w-3.5 h-3.5"></i>
                </a>

                <button onclick="openModal('individualModal')" class="by-btn-primary !py-2 !px-4 !text-xs sm:!text-sm">
                    <i data-lucide="calendar" class="w-4 h-4"></i>
                    <span>Book FREE Session</span>
                </button>

                <button type="button" id="mobileMenuToggle" aria-label="Toggle navigation menu" class="lg:hidden w-10 h-10 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 flex items-center justify-center transition-all">
                    <i data-lucide="menu" id="menuIcon" class="w-5 h-5"></i>
                </button>
            </div>
        </div>

        <!-- Mobile Drawer -->
        <div id="mobileDrawerMenu" class="hidden lg:hidden border-t border-slate-200 bg-white/98 backdrop-blur-xl px-5 py-6 space-y-4 shadow-xl">
            <nav class="flex flex-col space-y-3 text-sm font-semibold text-slate-800">
                <a href="#about" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">About Program <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#challenges" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Everyday Challenges <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#shift" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Shift in Perspective <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#practices" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Our Practices <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#benefits" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">What Regular Practice Can Build <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#corporate" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between text-brandTeal font-bold">Corporate Workshops <i data-lucide="chevron-right" class="w-4 h-4 text-brandTeal"></i></a>
                <a href="#trainer" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Meet Trainer (Rajendra Boddu) <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#testimonials" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">Testimonials <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="#faq" class="mobile-nav-link py-2 border-b border-slate-100 flex items-center justify-between">FAQs <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400"></i></a>
                <a href="kids.html" class="mobile-nav-link py-2 text-brandOrangeDark font-bold flex items-center justify-between">Brain Yoga For Children →</a>
            </nav>
            <div class="pt-2 flex flex-col gap-2.5">
                <button onclick="openModal('individualModal')" class="w-full py-3 rounded-lg bg-brandOrange hover:bg-brandOrangeDark text-white font-bold text-center text-sm shadow-md">
                    Book a FREE Introductory Session
                </button>
                <button onclick="openModal('corporateModal')" class="w-full py-3 rounded-lg bg-brandTeal hover:bg-brandTealDark text-white font-bold text-center text-sm shadow-md">
                    Enquire About Corporate Workshops
                </button>
            </div>
        </div>
    </header>

    <!-- ========================================================================= -->
    <!-- 1. HERO SECTION (Background: Warm Peach #FFF3EB) -->
    <!-- ========================================================================= -->
    <section class="relative bg-brandPeachBg pt-12 pb-16 lg:pt-20 lg:pb-24 border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
                
                <!-- Left Content Column (7 cols) -->
                <div class="lg:col-span-7 space-y-6">
                    <div class="section-eyebrow">
                        <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                        <span>Practical, hands-on sessions • Mind-Wellness For Adults</span>
                    </div>

                    <!-- Client Hook Highlight Box -->
                    <div>
                        <div class="inline-flex items-center gap-2 bg-white px-4 py-2 rounded-xl border border-brandOrange/30 shadow-sm">
                            <span class="w-2.5 h-2.5 rounded-full bg-brandOrange animate-pulse"></span>
                            <p class="text-brandOrange font-bold text-base sm:text-lg">
                                "Body at home. Mind still at the office."
                            </p>
                        </div>
                    </div>

                    <!-- Main Headline -->
                    <h1 class="main-heading">
                        Your Work Is Demanding. <br class="hidden sm:inline">
                        <span style="color: #007984;">Your Mind Needs Care Too.</span>
                    </h1>

                    <!-- Subheading -->
                    <p class="text-base sm:text-lg text-slate-700 leading-relaxed font-medium max-w-2xl">
                        Develop calmness, focus, and emotional balance through practical Brain Yoga techniques designed for everyday work and life.
                    </p>

                    <!-- Paragraph -->
                    <p class="text-sm sm:text-base text-slate-600 leading-relaxed max-w-2xl">
                        <strong>Brain Yoga for Busy Minds</strong> is a practical mind-wellness program for working professionals, entrepreneurs, and adults who want to pause, reset, and respond to life's challenges with greater awareness.
                    </p>

                    <!-- CTAs -->
                    <div class="pt-2 flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
                        <button onclick="openModal('individualModal')" class="by-btn-primary">
                            <i data-lucide="check-circle-2" class="w-5 h-5"></i>
                            <span>Book a FREE Introductory Session</span>
                        </button>
                        
                        <button onclick="openModal('corporateModal')" class="by-btn-secondary">
                            <i data-lucide="building-2" class="w-5 h-5"></i>
                            <span>Enquire About Corporate Workshops</span>
                        </button>
                    </div>

                    <!-- Trust Tags -->
                    <div class="pt-2 flex flex-wrap items-center gap-6 text-xs font-semibold text-slate-600">
                        <div class="flex items-center gap-2">
                            <i data-lucide="check" class="w-4 h-4 text-brandTeal"></i>
                            <span>Practical, hands-on sessions</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="monitor" class="w-4 h-4 text-brandTeal"></i>
                            <span>Online & In-Person Sessions</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <i data-lucide="briefcase" class="w-4 h-4 text-brandOrange"></i>
                            <span>Corporate & Individual</span>
                        </div>
                    </div>
                </div>

                <!-- Right Visual Column (5 cols) -->
                <!-- Strictly NO TEXT ON TOP OF IMAGE as requested by user -->
                <div class="lg:col-span-5 space-y-4">
                    <div class="by-card">
                        <!-- Clean, unobstructed portrait photo -->
                        <div class="relative aspect-[4/4] bg-slate-100 overflow-hidden">
                            <img src="rajindra_boddu_portrait.jpg" alt="Rajendra Boddu - Brain Yoga Trainer" class="w-full h-full object-cover object-top" loading="eager" fetchpriority="high">
                        </div>

                        <!-- Info cleanly placed BELOW the photo, not on top! -->
                        <div class="p-5 bg-white border-t border-slate-100">
                            <div class="flex items-start justify-between gap-3">
                                <div>
                                    <h3 class="text-lg font-bold text-brandDark">Rajendra Boddu</h3>
                                    <p class="text-xs font-semibold text-brandTeal mt-0.5">Brain Yoga Trainer | Yoga Therapist</p>
                                    <p class="text-xs text-slate-500 mt-1">15 Yrs IT Veteran (TCS & Capgemini)</p>
                                </div>
                                <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-brandPeachLight px-2.5 py-1 rounded-md border border-brandOrange/20 whitespace-nowrap">
                                    Lead Facilitator
                                </span>
                            </div>
                        </div>

                        <!-- Video Introductory Card Below Photo -->
                        <div class="p-4 bg-brandTealLight/60 border-t border-slate-100 flex items-center justify-between gap-4">
                            <div class="flex items-center gap-3">
                                <button onclick="openVideoModal()" class="w-11 h-11 rounded-lg bg-brandOrange hover:bg-brandOrangeDark text-white flex items-center justify-center shadow-md transition-all flex-shrink-0" aria-label="Play video introduction">
                                    <i data-lucide="play" class="w-5 h-5 ml-0.5 fill-current"></i>
                                </button>
                                <div>
                                    <h4 class="text-xs sm:text-sm font-bold text-brandDark">Watch Quick Intro Video</h4>
                                    <p class="text-[11px] text-slate-600">Sample preview of Brain Yoga techniques</p>
                                </div>
                            </div>
                            <button onclick="openVideoModal()" class="text-[11px] font-bold text-brandTeal bg-white px-3 py-1.5 rounded-lg border border-brandTeal/20 shadow-sm hover:bg-brandTeal hover:text-white transition-all whitespace-nowrap">
                                2 Mins Demo ▶
                            </button>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 2. EVERYDAY CHALLENGES (Background: Clean White #FFFFFF) -->
    <!-- ========================================================================= -->
    <section id="challenges" class="py-16 sm:py-24 bg-white border-b border-slate-200">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <!-- Standardized Clean Section Header -->
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow section-eyebrow-orange">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span>Everyday Reality Check</span>
                </div>
                <h2 class="main-heading">
                    Does This Sound Familiar? <span style="color: #007984;">You're Not Alone.</span>
                </h2>
                <p class="sub-heading">
                    Your work is important. But what about your mental well-being?
                </p>
            </div>

            <!-- 9 Relatable Stress Triggers Checklist -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 hover:border-brandTeal transition-colors flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange/15 text-brandOrangeDark flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="clock" class="w-4 h-4"></i>
                    </div>
                    <p class="text-sm font-medium text-slate-800 leading-relaxed">
                        Your mind keeps working even after the workday ends.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 hover:border-brandTeal transition-colors flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange/15 text-brandOrangeDark flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="zap-off" class="w-4 h-4"></i>
                    </div>
                    <p class="text-sm font-medium text-slate-800 leading-relaxed">
                        Small situations trigger frustration, irritation, or stress.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 hover:border-brandTeal transition-colors flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange/15 text-brandOrangeDark flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="smartphone" class="w-4 h-4"></i>
                    </div>
                    <p class="text-sm font-medium text-slate-800 leading-relaxed">
                        You check your mobile phone more often than you intend.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 hover:border-brandTeal transition-colors flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange/15 text-brandOrangeDark flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="users" class="w-4 h-4"></i>
                    </div>
                    <p class="text-sm font-medium text-slate-800 leading-relaxed">
                        You struggle to stay present during meetings and conversations.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 hover:border-brandTeal transition-colors flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange/15 text-brandOrangeDark flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="battery-low" class="w-4 h-4"></i>
                    </div>
                    <p class="text-sm font-medium text-slate-800 leading-relaxed">
                        You feel mentally tired even when you have been sitting all day.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 hover:border-brandTeal transition-colors flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange/15 text-brandOrangeDark flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="compass" class="w-4 h-4"></i>
                    </div>
                    <p class="text-sm font-medium text-slate-800 leading-relaxed">
                        You know your goals but struggle to stay connected to them.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 hover:border-brandTeal transition-colors flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange/15 text-brandOrangeDark flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="message-square-off" class="w-4 h-4"></i>
                    </div>
                    <p class="text-sm font-medium text-slate-800 leading-relaxed">
                        You want to respond thoughtfully instead of reacting automatically.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 hover:border-brandTeal transition-colors flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange/15 text-brandOrangeDark flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="calendar-x-2" class="w-4 h-4"></i>
                    </div>
                    <p class="text-sm font-medium text-slate-800 leading-relaxed">
                        <strong>"Every day isn’t Sunday"</strong> — accepting hard days and constant workplace demands.
                    </p>
                </div>

                <div class="md:col-span-2 p-5 rounded-xl bg-slate-50 border border-slate-200 hover:border-brandTeal transition-colors flex items-start gap-4">
                    <div class="w-8 h-8 rounded-lg bg-brandOrange/15 text-brandOrangeDark flex items-center justify-center flex-shrink-0 mt-0.5">
                        <i data-lucide="alert-circle" class="w-4 h-4"></i>
                    </div>
                    <p class="text-sm font-medium text-slate-800 leading-relaxed">
                        <strong>"I’m physically tired and unfit"</strong> — sitting desk fatigue, sluggish energy, and lack of active breaks.
                    </p>
                </div>

            </div>

            <!-- Closing Statement Box -->
            <div class="mt-10 p-6 sm:p-8 rounded-2xl bg-gradient-to-r from-brandTeal to-brandTealDark text-white shadow-lg flex items-center gap-5">
                <div class="w-12 h-12 rounded-xl bg-white/15 flex items-center justify-center flex-shrink-0">
                    <i data-lucide="heart-handshake" class="w-6 h-6 text-brandOrange"></i>
                </div>
                <p class="text-base sm:text-lg font-medium leading-relaxed">
                    "Everyday life may not become less demanding. But we can learn to meet it with greater awareness, calmness, and balance."
                </p>
            </div>

        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 3. A SIMPLE SHIFT IN PERSPECTIVE (Background: Warm Peach #FFF3EB) -->
    <!-- ========================================================================= -->
    <section id="shift" class="py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="by-card p-8 sm:p-12 lg:p-16">
                
                <div class="text-center max-w-3xl mx-auto mb-10">
                    <div class="section-eyebrow">
                        <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                        <span>A Simple Shift in Perspective</span>
                    </div>
                    <h2 class="main-heading">
                        10 People. 1 Barking Dog.
                    </h2>
                    <p class="mt-2 text-xl font-bold text-brandOrange">
                        What Makes the Difference?
                    </p>
                    <p class="sub-heading">
                        Imagine 10 people standing on a street. Suddenly, a dog starts barking at them.
                    </p>
                </div>

                <!-- 5 Reactions Grid -->
                <div class="grid grid-cols-2 sm:grid-cols-5 gap-3 mb-8">
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 text-center">
                        <div class="text-2xl mb-1.5">😤</div>
                        <p class="text-xs font-semibold text-slate-800">Some get irritated</p>
                    </div>
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 text-center">
                        <div class="text-2xl mb-1.5">😨</div>
                        <p class="text-xs font-semibold text-slate-800">Some feel frightened</p>
                    </div>
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 text-center">
                        <div class="text-2xl mb-1.5">📢</div>
                        <p class="text-xs font-semibold text-slate-800">Some shout at the dog</p>
                    </div>
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 text-center">
                        <div class="text-2xl mb-1.5">🚶</div>
                        <p class="text-xs font-semibold text-slate-800">Some simply walk away</p>
                    </div>
                    <div class="bg-brandTealLight/70 p-4 rounded-xl border border-brandTeal/30 text-center">
                        <div class="text-2xl mb-1.5">😌</div>
                        <p class="text-xs font-bold text-brandTeal">And some don't even react</p>
                    </div>
                </div>

                <!-- Core Takeaway -->
                <div class="space-y-6 max-w-2xl mx-auto text-center">
                    <p class="text-base font-bold text-brandTeal">
                        Same dog. Same situation. Different reactions.
                    </p>

                    <div class="p-6 rounded-xl bg-brandTealLight border border-brandTeal/20">
                        <h4 class="text-base font-bold text-brandDark mb-2">What Makes the Difference?</h4>
                        <p class="text-sm text-slate-700 leading-relaxed">
                            It's not always the situation. It's how we perceive and respond to it.
                        </p>
                    </div>

                    <div class="space-y-3">
                        <p class="text-sm sm:text-base text-slate-700">
                            Similarly, Brain Yoga helps us practice a shift in everyday life:
                        </p>
                        <div class="inline-block py-2.5 px-6 rounded-lg bg-brandDark text-white text-sm sm:text-base font-semibold shadow-md">
                            From automatic reaction <span class="text-brandOrange">➔</span> to conscious response.
                        </div>
                    </div>

                    <p class="text-sm text-slate-600 leading-relaxed">
                        Your situations may not always be under your control. But with awareness and practice, you can learn to respond differently.
                    </p>

                    <p class="text-base sm:text-lg font-bold text-brandOrangeDark">
                        "It's never just the dog. It's the mindset."
                    </p>

                    <div class="pt-2">
                        <button onclick="openModal('individualModal')" class="inline-flex items-center gap-2 text-sm font-bold text-brandTeal hover:text-brandOrange transition-colors">
                            <span>Experience this shift in a session</span>
                            <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </button>
                    </div>
                </div>

            </div>

        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 4. WHAT IS BRAIN YOGA FOR BUSY MINDS? (Background: Clean White #FFFFFF) -->
    <!-- ========================================================================= -->
    <section id="about" class="py-16 sm:py-24 bg-white border-b border-slate-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>The Core Philosophy</span>
                </div>
                <h2 class="main-heading">
                    What Is Brain Yoga for Busy Minds?
                </h2>
                <p class="sub-heading font-medium text-slate-700">
                    "Brain Yoga for Busy Minds combines simple brain-training activities, mindful movements, breathing techniques, and meditation to help you become more aware of your thoughts, emotions, and everyday responses."
                </p>
            </div>

            <!-- 4-Pillar Mind-Reset Architecture Graphic -->
            <div class="mb-14 p-8 rounded-2xl bg-brandPeachBg border border-slate-200">
                <div class="text-center mb-8">
                    <span class="text-[11px] font-bold uppercase tracking-wider text-brandOrange bg-white px-3 py-1 rounded-md border border-brandOrange/20 shadow-sm">
                        The 4-Pillar Mind-Reset Architecture
                    </span>
                    <h3 class="text-xl font-bold text-brandDark mt-2">
                        How Brain Yoga Works in Daily Life
                    </h3>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <!-- Step 1 -->
                    <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm text-center">
                        <div class="w-12 h-12 rounded-lg bg-brandTealLight text-brandTeal mx-auto flex items-center justify-center mb-4">
                            <i data-lucide="activity" class="w-6 h-6"></i>
                        </div>
                        <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrange">Step 1</span>
                        <h4 class="font-bold text-brandDark text-base mt-1 mb-2">Mindful Movements</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Gentle desk-friendly coordination & physical resets to release stiffness.
                        </p>
                    </div>

                    <!-- Step 2 -->
                    <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm text-center">
                        <div class="w-12 h-12 rounded-lg bg-brandPeachLight text-brandOrangeDark mx-auto flex items-center justify-center mb-4">
                            <i data-lucide="wind" class="w-6 h-6"></i>
                        </div>
                        <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrange">Step 2</span>
                        <h4 class="font-bold text-brandDark text-base mt-1 mb-2">Breathing Practices</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Pranayama & calming rhythmic breath to regulate the nervous system.
                        </p>
                    </div>

                    <!-- Step 3 -->
                    <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm text-center">
                        <div class="w-12 h-12 rounded-lg bg-brandTealLight text-brandTeal mx-auto flex items-center justify-center mb-4">
                            <i data-lucide="brain" class="w-6 h-6"></i>
                        </div>
                        <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrange">Step 3</span>
                        <h4 class="font-bold text-brandDark text-base mt-1 mb-2">Neurobic Agility</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Ambidextrous drills to snap out of habitual automated thought loops.
                        </p>
                    </div>

                    <!-- Step 4 -->
                    <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm text-center">
                        <div class="w-12 h-12 rounded-lg bg-brandPeachLight text-brandOrangeDark mx-auto flex items-center justify-center mb-4">
                            <i data-lucide="sparkles" class="w-6 h-6"></i>
                        </div>
                        <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrange">Step 4</span>
                        <h4 class="font-bold text-brandDark text-base mt-1 mb-2">Inner Stillness</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Meditation & awareness to choose calm, conscious response over reaction.
                        </p>
                    </div>
                </div>
            </div>

            <!-- 2 Core Philosophies -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="p-6 sm:p-8 rounded-2xl bg-slate-50 border border-slate-200">
                    <div class="w-10 h-10 rounded-lg bg-brandOrange text-white flex items-center justify-center mb-4">
                        <i data-lucide="refresh-cw" class="w-5 h-5"></i>
                    </div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Pause & Recharge</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">
                        The sessions are designed to help participants pause, recharge, and engage with everyday responsibilities more consciously.
                    </p>
                </div>

                <div class="p-6 sm:p-8 rounded-2xl bg-brandTealLight/50 border border-brandTeal/30">
                    <div class="w-10 h-10 rounded-lg bg-brandTeal text-white flex items-center justify-center mb-4">
                        <i data-lucide="shield-check" class="w-5 h-5"></i>
                    </div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Not Escaping Responsibilities</h3>
                    <p class="text-sm text-slate-700 font-medium leading-relaxed">
                        It is not about escaping responsibilities. It is about learning how to handle them with a calmer and more balanced mind.
                    </p>
                </div>
            </div>

        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 5. OUR PRACTICES (8 FULL CARDS - STRICTLY NO TEXT ON IMAGES!) -->
    <!-- ========================================================================= -->
    <section id="practices" class="py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-16">
                <div class="section-eyebrow section-eyebrow-orange">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span>Curriculum & Techniques</span>
                </div>
                <h2 class="main-heading">
                    Our Practices
                </h2>
                <p class="sub-heading">
                    Simple, repeatable mind-wellness practices designed for desk workers, busy professionals, and leaders.
                </p>
            </div>

            <!-- 8 Full Practice Cards with Clean Unobstructed Photos -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                
                <!-- 1. Brain Gym and Brain Coordination -->
                <div class="by-card flex flex-col justify-between">
                    <div>
                        <!-- Pure 100% unobstructed image, no text on top -->
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
                <div class="by-card flex flex-col justify-between">
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
                <div class="by-card flex flex-col justify-between">
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
                <div class="by-card flex flex-col justify-between">
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

                <!-- 5. Meditation and Visualization -->
                <div class="by-card flex flex-col justify-between">
                    <div>
                        <div class="h-48 w-full bg-slate-100 overflow-hidden">
                            <img src="custom_sound_bath.webp" alt="Meditation and Visualization" class="w-full h-full object-cover" loading="lazy" decoding="async">
                        </div>
                        <div class="p-6">
                            <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-0.5 rounded mb-2">
                                Clarity of Intent
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
                <div class="by-card flex flex-col justify-between">
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
                <div class="by-card flex flex-col justify-between">
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
                <div class="by-card flex flex-col justify-between">
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
    </section>

    <!-- ========================================================================= -->
    <!-- 6. WHAT REGULAR PRACTICE CAN BUILD (Background: Clean White #FFFFFF) -->
    <!-- ========================================================================= -->
    <section id="benefits" class="py-16 sm:py-24 bg-white border-b border-slate-200">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>Sustainable Benefits</span>
                </div>
                <h2 class="main-heading">
                    What Regular Practice Can Build
                </h2>
                <p class="sub-heading">
                    Participants may gradually develop:
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-4">
                    <div class="w-9 h-9 rounded-lg bg-brandTeal text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Greater awareness of stress triggers and habitual reactions.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-4">
                    <div class="w-9 h-9 rounded-lg bg-brandTeal text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Practical ways to pause and reset during a demanding day.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-4">
                    <div class="w-9 h-9 rounded-lg bg-brandTeal text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        Improved ability to bring attention back to a task or conversation.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-4">
                    <div class="w-9 h-9 rounded-lg bg-brandTeal text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        A calmer and more intentional approach to everyday challenges.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-4">
                    <div class="w-9 h-9 rounded-lg bg-brandTeal text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        More mindful use of mobile phones and digital breaks.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 flex items-center gap-4">
                    <div class="w-9 h-9 rounded-lg bg-brandTeal text-white flex items-center justify-center flex-shrink-0 shadow-sm">
                        <i data-lucide="check" class="w-5 h-5"></i>
                    </div>
                    <p class="text-sm font-semibold text-slate-800">
                        A simple personal routine for mental and emotional well-being.
                    </p>
                </div>

            </div>

            <!-- Medical Disclaimer Box -->
            <div class="mt-10 p-5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-600 text-center leading-relaxed">
                <i data-lucide="info" class="w-4 h-4 inline-block mr-1 text-slate-500 -mt-0.5"></i>
                <strong>Notice:</strong> Individual experiences vary. This is a wellness and self-practice program, not a substitute for medical or psychological treatment.
            </div>

        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 7. HOW DOES THE PROGRAM WORK? (Background: Warm Peach #FFF3EB) -->
    <!-- ========================================================================= -->
    <section class="py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>Flexible Delivery</span>
                </div>
                <h2 class="main-heading">
                    How Does the Program Work?
                </h2>
                <div class="mt-3 flex flex-wrap justify-center gap-4 text-xs font-bold text-slate-700">
                    <span class="bg-white px-3.5 py-1.5 rounded-lg border border-slate-200 shadow-sm">
                        📍 Format: Live guided sessions, online or in person
                    </span>
                    <span class="bg-white px-3.5 py-1.5 rounded-lg border border-slate-200 shadow-sm">
                        👥 Designed for: Adults, working professionals, entrepreneurs & teams
                    </span>
                </div>
            </div>

            <!-- Corporate Session Showcase Cards - Clean Unobstructed Photos! -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
                <div class="by-card">
                    <div class="aspect-[16/10] w-full overflow-hidden bg-slate-100">
                        <img src="workshop_team.jpg" alt="Corporate Brain Yoga Workshop" class="w-full h-full object-cover" loading="lazy" decoding="async">
                    </div>
                    <div class="p-6 bg-white">
                        <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-0.5 rounded mb-2">
                            Team Wellness In Action
                        </span>
                        <h4 class="text-base sm:text-lg font-bold text-brandDark">Interactive Hands-on Exercises</h4>
                        <p class="text-xs text-slate-600 mt-1 leading-relaxed">Energizing breaks that improve focus, reduce fatigue, and boost team morale.</p>
                    </div>
                </div>

                <div class="by-card">
                    <div class="aspect-[16/10] w-full overflow-hidden bg-slate-100">
                        <img src="workshop_interactive.jpg" alt="Brain Gym and Desk Stretching" class="w-full h-full object-cover" loading="lazy" decoding="async">
                    </div>
                    <div class="p-6 bg-white">
                        <span class="inline-block text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-brandPeachLight px-2.5 py-0.5 rounded mb-2">
                            Desk-Friendly Adaptability
                        </span>
                        <h4 class="text-base sm:text-lg font-bold text-brandDark">Chair & Ergonomic Mind-Breaks</h4>
                        <p class="text-xs text-slate-600 mt-1 leading-relaxed">No special clothing or gym required — perfectly suited for office environments.</p>
                    </div>
                </div>
            </div>

            <!-- Available Formats Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
                
                <div class="by-card p-6 text-center">
                    <div class="w-12 h-12 rounded-lg bg-brandPeachLight text-brandOrangeDark mx-auto flex items-center justify-center mb-3">
                        <i data-lucide="sun" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-brandDark text-base mb-1">Introductory Session</h4>
                    <p class="text-xs text-slate-500">Perfect to experience the core methods firsthand</p>
                </div>

                <div class="by-card p-6 text-center">
                    <div class="w-12 h-12 rounded-lg bg-brandTealLight text-brandTeal mx-auto flex items-center justify-center mb-3">
                        <i data-lucide="target" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-brandDark text-base mb-1">Focused Workshop</h4>
                    <p class="text-xs text-slate-500">Deep-dive on focus, screen habits, or stress</p>
                </div>

                <div class="by-card p-6 text-center">
                    <div class="w-12 h-12 rounded-lg bg-brandPeachLight text-brandOrangeDark mx-auto flex items-center justify-center mb-3">
                        <i data-lucide="layers" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-brandDark text-base mb-1">Multi-Session Program</h4>
                    <p class="text-xs text-slate-500">Progressive habit-building over consecutive weeks</p>
                </div>

                <div class="by-card p-6 text-center">
                    <div class="w-12 h-12 rounded-lg bg-brandTealLight text-brandTeal mx-auto flex items-center justify-center mb-3">
                        <i data-lucide="building-2" class="w-6 h-6"></i>
                    </div>
                    <h4 class="font-bold text-brandDark text-base mb-1">Customized Corporate</h4>
                    <p class="text-xs text-slate-500">Tailored to your organization size and schedule</p>
                </div>

            </div>

            <!-- Action Button -->
            <div class="by-card p-8 text-center max-w-2xl mx-auto">
                <p class="text-sm sm:text-base font-semibold text-slate-800 mb-6">
                    Participants also learn simple activities that they can practice independently at home or during work breaks.
                </p>
                <button onclick="openModal('corporateModal')" class="by-btn-teal">
                    <i data-lucide="users" class="w-4 h-4"></i>
                    <span>Discuss a Program for Your Team</span>
                </button>
            </div>

        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 8. CORPORATE BRAIN YOGA WORKSHOPS (Background: Clean White #FFFFFF) -->
    <!-- ========================================================================= -->
    <section id="corporate" class="py-16 sm:py-24 bg-white border-b border-slate-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow section-eyebrow-orange">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span>Corporate Brain Yoga Workshops</span>
                </div>
                <h2 class="main-heading">
                    Bring Brain Yoga to Your Workplace
                </h2>
                <p class="sub-heading">
                    Bring Brain Yoga to your startup, IT team, business network, or organization. Our interactive workshops combine engaging brain-training activities with practical techniques that employees can incorporate into their daily lives.
                </p>
            </div>

            <!-- 4 Formats -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
                
                <div class="p-6 rounded-xl bg-slate-50 border border-slate-200">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Express Break</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">30 to 45-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Introductory session designed for team all-hands, energizer breaks, or wellness kickoffs.
                    </p>
                </div>

                <div class="p-6 rounded-xl bg-brandTealLight border-2 border-brandTeal">
                    <div class="text-xs font-bold text-brandOrange uppercase tracking-wider mb-2">Most Popular</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">60 to 90-Minute</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Interactive workshop with live practice, breathing, tapping, and desk-friendly resets.
                    </p>
                </div>

                <div class="p-6 rounded-xl bg-slate-50 border border-slate-200">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Intensive</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Half-Day Workshop</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        In-depth training for leadership offsites, retreats, and high-performance teams.
                    </p>
                </div>

                <div class="p-6 rounded-xl bg-slate-50 border border-slate-200">
                    <div class="text-xs font-bold text-brandTeal uppercase tracking-wider mb-2">Sustained</div>
                    <h3 class="text-lg font-bold text-brandDark mb-2">Multi-Session Program</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Weekly or monthly structured wellness journey for long-term stress resilience.
                    </p>
                </div>

            </div>

            <!-- Topics Cloud -->
            <div class="p-6 sm:p-8 rounded-2xl bg-slate-50 border border-slate-200 mb-10">
                <h4 class="text-sm font-bold text-brandDark uppercase tracking-wider mb-4 text-center">
                    Workshop Topics May Include:
                </h4>
                <div class="flex flex-wrap justify-center gap-2.5 sm:gap-3">
                    <span class="bg-white text-slate-800 border border-slate-200 text-xs font-semibold px-4 py-2 rounded-lg shadow-sm">Focus and Attention</span>
                    <span class="bg-white text-slate-800 border border-slate-200 text-xs font-semibold px-4 py-2 rounded-lg shadow-sm">Stress Awareness</span>
                    <span class="bg-white text-slate-800 border border-slate-200 text-xs font-semibold px-4 py-2 rounded-lg shadow-sm">Emotional Balance</span>
                    <span class="bg-white text-slate-800 border border-slate-200 text-xs font-semibold px-4 py-2 rounded-lg shadow-sm">Mindful Screen Habits</span>
                    <span class="bg-white text-slate-800 border border-slate-200 text-xs font-semibold px-4 py-2 rounded-lg shadow-sm">Desk Relaxation</span>
                    <span class="bg-white text-slate-800 border border-slate-200 text-xs font-semibold px-4 py-2 rounded-lg shadow-sm">Present-Moment Awareness</span>
                </div>
            </div>

            <!-- Corporate Action Buttons -->
            <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                <button onclick="openModal('corporateModal')" class="by-btn-primary">
                    <i data-lucide="file-text" class="w-5 h-5"></i>
                    <span>Request a Corporate Proposal</span>
                </button>
                <button onclick="openModal('corporateModal')" class="by-btn-teal">
                    <i data-lucide="calendar" class="w-5 h-5"></i>
                    <span>Schedule a 15-Minute Discussion</span>
                </button>
            </div>

        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 9. MEET YOUR TRAINER (Background: Warm Peach #FFF3EB) -->
    <!-- ========================================================================= -->
    <section id="trainer" class="py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
                
                <!-- Trainer Photo - NO TEXT ON TOP -->
                <div class="lg:col-span-5">
                    <div class="by-card">
                        <div class="aspect-[3/4] bg-slate-100 overflow-hidden">
                            <img src="rajindra_boddu_portrait.jpg" alt="Rajendra Boddu - Brain Yoga Trainer" class="w-full h-full object-cover object-top" loading="lazy" decoding="async">
                        </div>
                        <div class="p-4 bg-white text-center border-t border-slate-100">
                            <h3 class="text-base font-bold text-brandDark">Rajendra Boddu</h3>
                            <p class="text-xs text-brandTeal font-semibold">Brain Yoga Trainer | Yoga Therapist</p>
                        </div>
                    </div>
                </div>

                <!-- Trainer Bio -->
                <div class="lg:col-span-7 space-y-5">
                    <div class="section-eyebrow">
                        <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                        <span>Meet Your Trainer</span>
                    </div>
                    
                    <h2 class="main-heading">
                        Meet Rajendra Boddu: <br class="hidden sm:inline">
                        <span style="color: #007984;">From IT Professional to Brain Yoga Trainer</span>
                    </h2>

                    <div class="space-y-4 text-sm sm:text-base text-slate-700 leading-relaxed font-normal">
                        <p>
                            After 15 years in the IT industry with organizations like <strong>TCS and Capgemini</strong>, I understand the demands of deadlines, multitasking, and professional responsibilities.
                        </p>
                        <p>
                            My journey into Brain Yoga and yoga therapy led me to help adults develop practical habits for greater awareness, calmness, and emotional balance.
                        </p>
                        <p>
                            Today, I combine my corporate experience with Brain Yoga practices to make mind-wellness relevant, practical, and accessible.
                        </p>
                        <p class="font-semibold text-brandDark bg-white p-4 rounded-xl border-l-4 border-brandTeal shadow-sm">
                            His objective is simple: help participants experience practical techniques and explore how to apply them in everyday life.
                        </p>
                    </div>

                    <!-- Verified Credentials List -->
                    <div class="pt-2">
                        <h4 class="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Verified Credentials & Experience:</h4>
                        <div class="p-4 rounded-xl bg-white border border-slate-200 text-xs font-semibold text-slate-800 leading-relaxed shadow-sm flex flex-wrap gap-2">
                            <span class="bg-brandTealLight text-brandTeal px-2.5 py-1 rounded-md">Certified Brain Yoga Trainer</span>
                            <span class="bg-brandTealLight text-brandTeal px-2.5 py-1 rounded-md">Certified Yoga Instructor</span>
                            <span class="bg-brandTealLight text-brandTeal px-2.5 py-1 rounded-md">Certified Yoga Therapist</span>
                            <span class="bg-brandPeachLight text-brandOrangeDark px-2.5 py-1 rounded-md">Quantum Speed Reading Mentor</span>
                            <span class="bg-brandPeachLight text-brandOrangeDark px-2.5 py-1 rounded-md">Certified Subconscious Mind Trainer</span>
                            <span class="bg-brandPeachLight text-brandOrangeDark px-2.5 py-1 rounded-md">Certified Auricular Therapist</span>
                            <span class="bg-slate-100 text-brandDark px-2.5 py-1 rounded-md font-bold">15 Years in IT (TCS & Capgemini)</span>
                        </div>
                    </div>
                </div>

            </div>

        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 10. WHAT PARTICIPANTS SAY (6 Clean Testimonial Cards) -->
    <!-- ========================================================================= -->
    <section id="testimonials" class="py-16 sm:py-24 bg-white border-b border-slate-200">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow section-eyebrow-orange">
                    <span class="w-2 h-2 rounded-full bg-brandOrange"></span>
                    <span>Real Participant Feedback</span>
                </div>
                <h2 class="main-heading">
                    What Participants Say
                </h2>
                <p class="sub-heading">
                    Real Experiences. Practical Learning.
                </p>
            </div>

            <!-- 6 Testimonials Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                
                <!-- 1. IT Professional - Uma Reddy -->
                <div class="by-card p-6 flex flex-col justify-between">
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-1 rounded">
                                IT Professional
                            </span>
                            <div class="text-amber-400 text-sm">★★★★★</div>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-700 leading-relaxed italic">
                            "Coming from an IT background myself, Rajendra's examples felt completely relatable. The breathing exercises and coordination activities have become a refreshing break between back-to-back meetings."
                        </p>
                    </div>
                    <div class="pt-4 border-t border-slate-100 mt-4 flex items-center gap-3">
                        <img src="testimonial_uma.jpg" alt="Uma Reddy" class="w-11 h-11 rounded-full object-cover border border-brandTeal/30 shadow-sm flex-shrink-0" loading="lazy" decoding="async">
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Uma Reddy</h4>
                            <p class="text-[11px] text-slate-500">New Jersey, USA</p>
                        </div>
                    </div>
                </div>

                <!-- 2. Business Owner - Aryan Venkat -->
                <div class="by-card p-6 flex flex-col justify-between">
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrangeDark bg-brandPeachLight px-2.5 py-1 rounded">
                                Business Owner
                            </span>
                            <div class="text-amber-400 text-sm">★★★★★</div>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-700 leading-relaxed italic">
                            "Running a business means dealing with unexpected challenges every day. Rajendra's sessions helped me become more aware of my reactions and approach situations with a calmer mindset."
                        </p>
                    </div>
                    <div class="pt-4 border-t border-slate-100 mt-4 flex items-center gap-3">
                        <img src="testimonial_aryan.jpg" alt="Aryan Venkat" class="w-11 h-11 rounded-full object-cover border border-brandOrange/30 shadow-sm flex-shrink-0" loading="lazy" decoding="async">
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Aryan Venkat</h4>
                            <p class="text-[11px] text-slate-500">Aryan Realty, Hyderabad</p>
                        </div>
                    </div>
                </div>

                <!-- 3. Working Mother - Kavitha -->
                <div class="by-card p-6 flex flex-col justify-between">
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-1 rounded">
                                Working Mother
                            </span>
                            <div class="text-amber-400 text-sm">★★★★★</div>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-700 leading-relaxed italic">
                            "Managing office work and family responsibilities can be overwhelming. These simple Brain Yoga practices give me some time for myself and help me feel more balanced."
                        </p>
                    </div>
                    <div class="pt-4 border-t border-slate-100 mt-4 flex items-center gap-3">
                        <img src="testimonial_kavitha.jpg" alt="Kavitha" class="w-11 h-11 rounded-full object-cover border border-brandTeal/30 shadow-sm flex-shrink-0" loading="lazy" decoding="async">
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Kavitha</h4>
                            <p class="text-[11px] text-slate-500">Visakhapatnam</p>
                        </div>
                    </div>
                </div>

                <!-- 4. Corporate Employee - Sravani -->
                <div class="by-card p-6 flex flex-col justify-between">
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrangeDark bg-brandPeachLight px-2.5 py-1 rounded">
                                Corporate Employee
                            </span>
                            <div class="text-amber-400 text-sm">★★★★★</div>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-700 leading-relaxed italic">
                            "What I liked most was that the techniques were simple and practical. I can practise them at my desk without disturbing my work schedule."
                        </p>
                    </div>
                    <div class="pt-4 border-t border-slate-100 mt-4 flex items-center gap-3">
                        <img src="testimonial_sravani.jpg" alt="Sravani" class="w-11 h-11 rounded-full object-cover border border-brandOrange/30 shadow-sm flex-shrink-0" loading="lazy" decoding="async">
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Sravani</h4>
                            <p class="text-[11px] text-slate-500">TCS, Hyderabad</p>
                        </div>
                    </div>
                </div>

                <!-- 5. Entrepreneur - Vinay -->
                <div class="by-card p-6 flex flex-col justify-between">
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-2.5 py-1 rounded">
                                Entrepreneur
                            </span>
                            <div class="text-amber-400 text-sm">★★★★★</div>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-700 leading-relaxed italic">
                            "I always had so many thoughts running through my mind. The meditation and breathing practices helped me slow down and become more aware of my thoughts."
                        </p>
                    </div>
                    <div class="pt-4 border-t border-slate-100 mt-4 flex items-center gap-3">
                        <img src="testimonial_vinay.jpg" alt="Vinay" class="w-11 h-11 rounded-full object-cover border border-brandTeal/30 shadow-sm flex-shrink-0" loading="lazy" decoding="async">
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Vinay</h4>
                            <p class="text-[11px] text-slate-500">Marine Works, Visakhapatnam</p>
                        </div>
                    </div>
                </div>

                <!-- 6. IT Team Leader - Kiran Ravoori -->
                <div class="by-card p-6 flex flex-col justify-between">
                    <div class="space-y-3">
                        <div class="flex items-center justify-between">
                            <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrangeDark bg-brandPeachLight px-2.5 py-1 rounded">
                                IT Team Leader
                            </span>
                            <div class="text-amber-400 text-sm">★★★★★</div>
                        </div>
                        <p class="text-xs sm:text-sm text-slate-700 leading-relaxed italic">
                            "Handling deadlines and managing a team can be mentally exhausting. Brain Yoga gave me some useful techniques to pause, regain composure, and respond more thoughtfully."
                        </p>
                    </div>
                    <div class="pt-4 border-t border-slate-100 mt-4 flex items-center gap-3">
                        <img src="testimonial_kiran.jpg" alt="Kiran Ravoori" class="w-11 h-11 rounded-full object-cover border border-brandOrange/30 shadow-sm flex-shrink-0" loading="lazy" decoding="async">
                        <div>
                            <h4 class="text-xs font-bold text-brandDark">Kiran Ravoori</h4>
                            <p class="text-[11px] text-slate-500">Hyderabad</p>
                        </div>
                    </div>
                </div>

            </div>

        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 11. FREQUENTLY ASKED QUESTIONS (Background: Warm Peach #FFF3EB) -->
    <!-- ========================================================================= -->
    <section id="faq" class="py-16 sm:py-24 bg-brandPeachBg border-b border-slate-200">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            
            <div class="text-center max-w-3xl mx-auto mb-14">
                <div class="section-eyebrow">
                    <span class="w-2 h-2 rounded-full bg-brandTeal"></span>
                    <span>Got Questions?</span>
                </div>
                <h2 class="main-heading">
                    Frequently Asked Questions
                </h2>
                <p class="sub-heading">
                    Clear answers to help you get started with Brain Yoga for Busy Minds
                </p>
            </div>

            <!-- Accordion List -->
            <div class="space-y-4">
                
                <div class="by-card">
                    <button class="w-full p-5 text-left flex items-center justify-between font-bold text-brandDark text-sm sm:text-base focus:outline-none" onclick="toggleFaq(this)">
                        <span>Do I need prior yoga or meditation experience?</span>
                        <i data-lucide="chevron-down" class="faq-chevron w-5 h-5 text-slate-400 transition-transform"></i>
                    </button>
                    <div class="faq-answer px-5 pb-5 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
                        No. The sessions are beginner-friendly. Every practice is explained and guided step by step.
                    </div>
                </div>

                <div class="by-card">
                    <button class="w-full p-5 text-left flex items-center justify-between font-bold text-brandDark text-sm sm:text-base focus:outline-none" onclick="toggleFaq(this)">
                        <span>Is this suitable for people with busy schedules?</span>
                        <i data-lucide="chevron-down" class="faq-chevron w-5 h-5 text-slate-400 transition-transform"></i>
                    </button>
                    <div class="faq-answer px-5 pb-5 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
                        Yes. The program includes simple practices that can be adapted to daily routines and work breaks.
                    </div>
                </div>

                <div class="by-card">
                    <button class="w-full p-5 text-left flex items-center justify-between font-bold text-brandDark text-sm sm:text-base focus:outline-none" onclick="toggleFaq(this)">
                        <span>Is this a fitness or medical program?</span>
                        <i data-lucide="chevron-down" class="faq-chevron w-5 h-5 text-slate-400 transition-transform"></i>
                    </button>
                    <div class="faq-answer px-5 pb-5 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
                        It is a mind-wellness and self-awareness program. It is not medical treatment or a replacement for professional care.
                    </div>
                </div>

                <div class="by-card">
                    <button class="w-full p-5 text-left flex items-center justify-between font-bold text-brandDark text-sm sm:text-base focus:outline-none" onclick="toggleFaq(this)">
                        <span>Can you conduct workshops for our company?</span>
                        <i data-lucide="chevron-down" class="faq-chevron w-5 h-5 text-slate-400 transition-transform"></i>
                    </button>
                    <div class="faq-answer px-5 pb-5 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
                        Yes. Introductory sessions and customized workshops can be arranged based on your team's requirements, size, and schedule.
                    </div>
                </div>

                <div class="by-card">
                    <button class="w-full p-5 text-left flex items-center justify-between font-bold text-brandDark text-sm sm:text-base focus:outline-none" onclick="toggleFaq(this)">
                        <span>Can the sessions be conducted online?</span>
                        <i data-lucide="chevron-down" class="faq-chevron w-5 h-5 text-slate-400 transition-transform"></i>
                    </button>
                    <div class="faq-answer px-5 pb-5 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
                        Yes. Both online and in-person sessions can be discussed.
                    </div>
                </div>

                <div class="by-card">
                    <button class="w-full p-5 text-left flex items-center justify-between font-bold text-brandDark text-sm sm:text-base focus:outline-none" onclick="toggleFaq(this)">
                        <span>What should participants bring?</span>
                        <i data-lucide="chevron-down" class="faq-chevron w-5 h-5 text-slate-400 transition-transform"></i>
                    </button>
                    <div class="faq-answer px-5 pb-5 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
                        Comfortable clothing and a chair or quiet space. Special equipment is generally not required.
                    </div>
                </div>

            </div>

        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- 12. FINAL CALL TO ACTION (Deep Teal Gradient) -->
    <!-- ========================================================================= -->
    <section class="py-16 sm:py-24 bg-gradient-to-r from-brandTealDark via-brandTeal to-brandTealDark text-white relative overflow-hidden">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10 space-y-6">
            <span class="text-xs font-bold uppercase tracking-widest text-brandOrange bg-white/10 px-4 py-1.5 rounded-full inline-block border border-white/10">
                Begin Your Practice
            </span>

            <h2 class="text-3xl sm:text-5xl font-bold tracking-tight leading-tight">
                Give Your Mind a Practical Pause.
            </h2>

            <p class="text-base sm:text-lg text-slate-200 max-w-2xl mx-auto leading-relaxed">
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

                <button onclick="openModal('corporateModal')" class="by-btn-secondary !bg-white/10 !text-white !border-white/30 hover:!bg-white/20">
                    <i data-lucide="building-2" class="w-5 h-5"></i>
                    <span>Request a Corporate Workshop</span>
                </button>
            </div>

            <p class="text-xs text-slate-300 pt-4">
                Direct WhatsApp Contact: <a href="https://wa.me/918331929240" class="underline font-bold text-white">+91 83319 29240</a>
            </p>
        </div>
    </section>

    <!-- ========================================================================= -->
    <!-- FOOTER (With Official Logo) -->
    <!-- ========================================================================= -->
    <footer class="bg-[#111827] text-slate-400 py-12 border-t border-slate-800 text-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row items-center justify-between gap-6 text-center md:text-left">
                <div>
                    <img src="official_logo.png" alt="Brain Yoga Academy" class="h-9 w-auto brightness-0 invert opacity-95 mb-2 mx-auto md:mx-0">
                    <p class="text-slate-400 text-xs">
                        Practical Mind-Wellness & Neuro-Movement for Adults and Corporate Teams.
                    </p>
                </div>

                <div class="flex flex-wrap items-center justify-center gap-6 text-xs">
                    <a href="kids.html" class="text-amber-400 hover:underline font-bold">Brain Yoga For Children</a>
                    <a href="#about" class="hover:text-white transition-colors">About</a>
                    <a href="#practices" class="hover:text-white transition-colors">Our Practices</a>
                    <a href="#corporate" class="hover:text-white transition-colors">Corporate</a>
                    <a href="#trainer" class="hover:text-white transition-colors">Trainer</a>
                    <a href="#testimonials" class="hover:text-white transition-colors">Testimonials</a>
                    <a href="#faq" class="hover:text-white transition-colors">FAQ</a>
                </div>

                <div class="text-slate-500 text-[11px]">
                    &copy; 2026 Brain Yoga Academy. All Rights Reserved.
                </div>
            </div>
        </div>
    </footer>

    <!-- ========================================================================= -->
    <!-- FLOATING WHATSAPP BUTTON (ALWAYS VISIBLE) -->
    <!-- ========================================================================= -->
    <aside aria-label="Quick WhatsApp Contact" class="fixed bottom-6 right-6 z-50">
        <a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20I%20am%20interested%20in%20Brain%20Yoga%20for%20Busy%20Minds.%20Please%20guide%20me." target="_blank" rel="noopener noreferrer" class="whatsapp-pulse-btn group flex items-center gap-2.5 bg-emerald-500 hover:bg-emerald-600 text-white pl-4 pr-5 py-3 rounded-full shadow-2xl hover:scale-105 transition-all" aria-label="Enquire on WhatsApp">
            <div class="w-6 h-6 flex items-center justify-center">
                <i data-lucide="message-circle" class="w-6 h-6 fill-current"></i>
            </div>
            <div class="text-left">
                <span class="text-[10px] block uppercase font-bold tracking-wider leading-none opacity-90">Quick Chat</span>
                <span class="text-xs font-bold block leading-none mt-0.5">WhatsApp</span>
            </div>
        </a>
    </aside>

    <!-- ========================================================================= -->
    <!-- MODALS -->
    <!-- ========================================================================= -->
    <div id="individualModal" class="fixed inset-0 z-50 hidden modal-backdrop flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative border border-slate-200 overflow-y-auto max-h-[90vh]">
            <button onclick="closeModal('individualModal')" class="absolute top-5 right-5 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center transition-colors">
                <i data-lucide="x" class="w-4 h-4"></i>
            </button>

            <div class="mb-5">
                <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-brandPeachLight px-3 py-1 rounded-md">
                    Free Introductory Session
                </span>
                <h3 class="text-xl sm:text-2xl font-bold text-brandDark mt-2">
                    Reserve Your Free Session
                </h3>
                <p class="text-xs text-slate-500 mt-1">
                    Experience practical Brain Yoga techniques firsthand. Please fill in your details:
                </p>
            </div>

            <form onsubmit="handleSessionSubmit(event)" class="space-y-4">
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Your Full Name *</label>
                    <input type="text" id="sessionName" required placeholder="e.g. Rahul Sharma" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:border-brandTeal focus:ring-1 focus:ring-brandTeal outline-none">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">WhatsApp / Phone Number *</label>
                    <input type="tel" id="sessionPhone" required placeholder="e.g. 9876543210" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:border-brandTeal focus:ring-1 focus:ring-brandTeal outline-none">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Profession / Role</label>
                    <input type="text" id="sessionRole" placeholder="e.g. Software Engineer / Consultant" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:border-brandTeal focus:ring-1 focus:ring-brandTeal outline-none">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Preferred Mode</label>
                    <select id="sessionMode" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:border-brandTeal outline-none">
                        <option value="Online (Zoom / Meet)">Online (Zoom / Google Meet)</option>
                        <option value="In-Person">In-Person (Studio / Workspace)</option>
                    </select>
                </div>

                <button type="submit" class="w-full by-btn-primary !w-full">
                    <i data-lucide="send" class="w-4 h-4"></i>
                    <span>Confirm Free Session Booking</span>
                </button>
            </form>
        </div>
    </div>

    <div id="corporateModal" class="fixed inset-0 z-50 hidden modal-backdrop flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative border border-slate-200 overflow-y-auto max-h-[90vh]">
            <button onclick="closeModal('corporateModal')" class="absolute top-5 right-5 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center transition-colors">
                <i data-lucide="x" class="w-4 h-4"></i>
            </button>

            <div class="mb-5">
                <span class="text-[10px] font-bold uppercase tracking-wider text-brandTeal bg-brandTealLight px-3 py-1 rounded-md">
                    Corporate Wellness Proposal
                </span>
                <h3 class="text-xl sm:text-2xl font-bold text-brandDark mt-2">
                    Enquire for Your Team
                </h3>
                <p class="text-xs text-slate-500 mt-1">
                    Customized workshops for startups, IT teams, and organizations:
                </p>
            </div>

            <form onsubmit="handleCorporateSubmit(event)" class="space-y-4">
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Contact Name *</label>
                    <input type="text" id="corpName" required placeholder="e.g. Priya Verma" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:border-brandTeal focus:ring-1 focus:ring-brandTeal outline-none">
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Company / Organization *</label>
                    <input type="text" id="corpCompany" required placeholder="e.g. Infosys / Tech Solutions" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:border-brandTeal focus:ring-1 focus:ring-brandTeal outline-none">
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Team Size</label>
                        <select id="corpSize" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:border-brandTeal outline-none">
                            <option value="10-30 Members">10-30 Members</option>
                            <option value="30-100 Members">30-100 Members</option>
                            <option value="100+ Members">100+ Members</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Format</label>
                        <select id="corpFormat" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:border-brandTeal outline-none">
                            <option value="30-45 Mins Intro">30-45 Mins Intro</option>
                            <option value="60-90 Mins Workshop">60-90 Mins Workshop</option>
                            <option value="Half-Day Workshop">Half-Day Workshop</option>
                            <option value="Multi-Session Program">Multi-Session Program</option>
                        </select>
                    </div>
                </div>
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Phone / WhatsApp *</label>
                    <input type="tel" id="corpPhone" required placeholder="e.g. 9876543210" class="w-full px-4 py-2.5 rounded-lg border border-slate-300 text-sm focus:border-brandTeal focus:ring-1 focus:ring-brandTeal outline-none">
                </div>

                <button type="submit" class="w-full by-btn-teal !w-full">
                    <i data-lucide="send" class="w-4 h-4"></i>
                    <span>Send Corporate Enquiry</span>
                </button>
            </form>
        </div>
    </div>

    <!-- Video Modal -->
    <div id="videoModal" class="fixed inset-0 z-50 hidden modal-backdrop flex items-center justify-center p-4">
        <div class="bg-[#1F1F1F] rounded-2xl max-w-2xl w-full p-4 sm:p-6 shadow-2xl relative border border-slate-700">
            <button onclick="closeModal('videoModal')" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center transition-colors z-20">
                <i data-lucide="x" class="w-4 h-4"></i>
            </button>
            
            <div class="pt-2 pb-3 text-center">
                <span class="text-[10px] font-bold uppercase tracking-wider text-brandOrange bg-white/10 px-3 py-1 rounded">
                    Video Introduction
                </span>
                <h3 class="text-lg font-bold text-white mt-1.5">Brain Yoga for Busy Minds</h3>
                <p class="text-xs text-slate-300">Conducted by Rajendra Boddu (Brain Yoga Facilitator)</p>
            </div>

            <!-- Functional HTML5 Video with Poster -->
            <div class="relative aspect-video rounded-xl overflow-hidden bg-black flex items-center justify-center border border-slate-700">
                <video id="introVideoPlayer" controls class="w-full h-full object-cover" poster="workshop_team.jpg">
                    <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>

            <div class="mt-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left bg-slate-800/80 p-3.5 rounded-xl border border-slate-700">
                <div>
                    <h5 class="text-xs font-bold text-white">Want the full guided practice or corporate demo?</h5>
                    <p class="text-[11px] text-slate-400">Rajendra ji can share direct recordings and tailored outlines.</p>
                </div>
                <a href="https://wa.me/918331929240?text=Hello%20Rajendra%20ji%2C%20please%20share%20the%20Brain%20Yoga%20introductory%20video%20and%20session%20schedule." target="_blank" class="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs whitespace-nowrap shadow-md">
                    <i data-lucide="message-circle" class="w-4 h-4"></i>
                    <span>Connect on WhatsApp</span>
                </a>
            </div>
        </div>
    </div>

    <!-- Javascript -->
    <script>
        lucide.createIcons();

        // Mobile Menu Toggle
        const menuBtn = document.getElementById('mobileMenuToggle');
        const drawer = document.getElementById('mobileDrawerMenu');
        menuBtn.addEventListener('click', () => {
            drawer.classList.toggle('hidden');
        });

        document.querySelectorAll('.mobile-nav-link').forEach(link => {
            link.addEventListener('click', () => {
                drawer.classList.add('hidden');
            });
        });

        // Modal Controls
        function openModal(id) {
            const el = document.getElementById(id);
            if (el) {
                el.classList.remove('hidden');
                document.body.classList.add('overflow-hidden');
            }
        }

        function closeModal(id) {
            const el = document.getElementById(id);
            if (el) {
                el.classList.add('hidden');
                document.body.classList.remove('overflow-hidden');
                if (id === 'videoModal') {
                    const vid = document.getElementById('introVideoPlayer');
                    if (vid) vid.pause();
                }
            }
        }

        function openVideoModal() {
            openModal('videoModal');
            const vid = document.getElementById('introVideoPlayer');
            if (vid) {
                vid.currentTime = 0;
                vid.play().catch(e => console.log('Autoplay handled'));
            }
        }

        window.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal-backdrop')) {
                e.target.classList.add('hidden');
                document.body.classList.remove('overflow-hidden');
                const vid = document.getElementById('introVideoPlayer');
                if (vid) vid.pause();
            }
        });

        window.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                ['individualModal', 'corporateModal', 'videoModal'].forEach(id => closeModal(id));
            }
        });

        // FAQ Toggle
        function toggleFaq(btn) {
            const parent = btn.parentElement;
            const answer = parent.querySelector('.faq-answer');
            const chevron = btn.querySelector('.faq-chevron');
            
            const isHidden = answer.classList.contains('hidden');
            document.querySelectorAll('.faq-answer').forEach(ans => ans.classList.add('hidden'));
            document.querySelectorAll('.faq-chevron').forEach(chev => chev.classList.remove('rotate-180'));

            if (isHidden) {
                answer.classList.remove('hidden');
                chevron.classList.add('rotate-180');
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            const answers = document.querySelectorAll('.faq-answer');
            answers.forEach((ans, idx) => {
                if (idx !== 0) ans.classList.add('hidden');
            });
            const firstChevron = document.querySelector('.faq-chevron');
            if (firstChevron) firstChevron.classList.add('rotate-180');
        });

        // Forms
        function handleSessionSubmit(e) {
            e.preventDefault();
            const name = document.getElementById('sessionName').value;
            const phone = document.getElementById('sessionPhone').value;
            const role = document.getElementById('sessionRole').value || 'Not specified';
            const mode = document.getElementById('sessionMode').value;

            const text = `Hello Rajendra ji, I want to book a FREE Introductory Session for Brain Yoga for Busy Minds.%0A%0A*Name:* ${encodeURIComponent(name)}%0A*Phone:* ${encodeURIComponent(phone)}%0A*Profession:* ${encodeURIComponent(role)}%0A*Preferred Mode:* ${encodeURIComponent(mode)}`;
            window.open(`https://wa.me/918331929240?text=${text}`, '_blank');
            closeModal('individualModal');
        }

        function handleCorporateSubmit(e) {
            e.preventDefault();
            const name = document.getElementById('corpName').value;
            const company = document.getElementById('corpCompany').value;
            const size = document.getElementById('corpSize').value;
            const format = document.getElementById('corpFormat').value;
            const phone = document.getElementById('corpPhone').value;

            const text = `Hello Rajendra ji, we would like to enquire about a Corporate Brain Yoga Workshop for our team.%0A%0A*Contact Name:* ${encodeURIComponent(name)}%0A*Company:* ${encodeURIComponent(company)}%0A*Team Size:* ${encodeURIComponent(size)}%0A*Format:* ${encodeURIComponent(format)}%0A*Phone:* ${encodeURIComponent(phone)}`;
            window.open(`https://wa.me/918331929240?text=${text}`, '_blank');
            closeModal('corporateModal');
        }
    </script>
</body>
</html>
"""

targets = [
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/index.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds.html',
    '/Users/user/.gemini/antigravity/scratch/brain-yoga-landing/brain-yoga-for-busy-minds/index.html',
]

for t in targets:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    with open(t, 'w', encoding='utf-8') as f:
        f.write(html_code)
    print(f"Rebuilt clean typography in {t}")

print("Clean typography rebuild finished successfully!")
