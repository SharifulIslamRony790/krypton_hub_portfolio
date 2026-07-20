# 🚀 Krypton 360° - Project Information & SSOT (Single Source of Truth)

This document serves as the **Single Source of Truth (SSOT)** for the **Krypton 360°** project. Any human developer or AI assistant working on this project MUST read and adhere to the guidelines, architecture, and principles outlined in this file before making any changes.

---

## 1. প্রজেক্ট পরিচিতি (Project Overview)
**Krypton 360°** (পূর্বে *Krypton Hub 360*) হলো একটি আধুনিক, প্রিমিয়াম এবং হাই-পারফরম্যান্স টেকনিক্যাল ও ডিজিটাল এজেন্সির পোর্টফোলিও ওয়েবসাইট। এটি মূলত কোম্পানির সার্ভিস, টিম মেম্বারদের পরিচিতি এবং ব্র্যান্ড আইডেন্টিটি বিশ্ববাসীর কাছে একটি অত্যন্ত প্রফেশনাল এবং কর্পোরেট রূপে উপস্থাপন করার জন্য তৈরি করা হয়েছে। 

## 2. উদ্দেশ্য ও ভিশন (Vision & Goals)
- **Vision:** "Design Bold. Build Secure. Scale Smart." - এই স্লোগানটিকে কেন্দ্র করে একটি বিশ্বস্ত, আধুনিক এবং সিকিউর ডিজিটাল উপস্থিতি তৈরি করা।
- **Goals:** 
  - ভিজিটরদের প্রথম দেখাতেই (First Impression) প্রিমিয়াম ফিল দেওয়া।
  - একটি ডার্ক-থিম ভিত্তিক, অত্যাধুনিক UI/UX নিশ্চিত করা।
  - লাইটওয়েট এবং অত্যন্ত দ্রুত লোড হওয়া ওয়েবসাইট তৈরি করা।

## 3. সম্পূর্ণ Planning ও Development Process
প্রজেক্টটি কয়েকটি ধাপে (Phases) ডেভেলপ করা হয়েছে:
- **Phase 1 (Foundation):** Django-এর মাধ্যমে বেসিক প্রজেক্ট এবং অ্যাপ স্ট্রাকচার তৈরি। 
- **Phase 2 (UI/UX Overhaul):** Tailwind CSS, Alpine.js এবং GSAP ব্যবহার করে সম্পূর্ণ ওয়েবসাইটটিকে একটি মডার্ন ডার্ক-থিমে রূপান্তর এবং অ্যানিমেশন যুক্ত করা।
- **Phase 3 (Brand Identity Update):** পুরানো লোগো এবং নাম পরিবর্তন করে সম্পূর্ণ নতুন "Krypton 360°" ব্র্যান্ড আইডেন্টিটি তৈরি। এর মধ্যে ছিল জ্যামিতিক (Geometric) interlocking "K" লোগো, হিরো সেকশনের ওয়াটারমার্ক এবং টিম মেম্বারদের ছবিগুলোকে Advanced Alpha Matting-এর মাধ্যমে কর্পোরেট স্টুডিও ব্যাকগ্রাউন্ডে রূপান্তর।
- **Phase 4 (Production Readiness):** Render.com-এ ডেপ্লয়মেন্টের জন্য `render.yaml`, PostgreSQL, Gunicorn এবং WhiteNoise কনফিগারেশন।

## 4. Project Architecture
প্রজেক্টটি ক্লাসিক **Monolithic Architecture** অনুসরণ করে তৈরি, যা Django-এর **MVT (Model-View-Template)** ডিজাইন প্যাটার্নের ওপর ভিত্তি করে দাঁড়িয়ে আছে। ফ্রন্টএন্ড এবং ব্যাকএন্ড একই সাথে সার্ভড হয়, যা পোর্টফোলিও ওয়েবসাইটের জন্য সবচেয়ে কার্যকর ও সহজ রক্ষণাবেক্ষণযোগ্য পদ্ধতি।

## 5. ব্যবহৃত Technology Stack এবং নির্বাচনের কারণ
- **Backend:** `Python / Django 5.x` (নিরাপদ, দ্রুত ডেভেলপমেন্ট এবং মজবুত কাঠামোর জন্য)।
- **Frontend Styling:** `Tailwind CSS` (Utility-first অ্যাপ্রোচ, কাস্টম ডিজাইন দ্রুত করার জন্য)।
- **Frontend Interactions:** `Alpine.js` (React/Vue-এর মতো ভারী ফ্রেমওয়ার্ক ছাড়া শুধু HTML-এ লাইটওয়েট ইন্টার‍্যাক্টিভিটি যেমন— ন্যাভবার স্ক্রল স্টেট কন্ট্রোল করার জন্য)।
- **Animations:** `GSAP (GreenSock)` (স্মুথ, হাই-পারফরম্যান্স স্ক্রল অ্যানিমেশনের জন্য)।
- **Database:** `PostgreSQL` (Render-এ প্রোডাকশন রেডি, রিলেশনাল ডেটাবেস)।
- **Static Files Serving:** `WhiteNoise` (Django থেকে সরাসরি ফাস্ট স্ট্যাটিক ফাইল সার্ভ করার জন্য)।
- **Production Server:** `Gunicorn` (Python WSGI HTTP Server)।

## 6. Development Workflow
1. Local Development (VS Code / AI IDE)
2. `python manage.py runserver` দিয়ে লোকাল টেস্টিং।
3. GitHub-এ কোড Push (`git add .` -> `git commit` -> `git push origin main`)।
4. Render.com-এ Auto-deployment (GitHub Webhook-এর মাধ্যমে)।

## 7. Implemented Features
- **Dynamic Preloader:** ওয়েবসাইট লোড হওয়ার সময় ব্র্যান্ড আইকন ও প্রোগ্রেস বার।
- **Smart Navbar:** Alpine.js দিয়ে তৈরি ন্যাভবার, যা একদম ওপরে থাকলে `logo_white.svg` এবং স্ক্রল করলে ডার্ক `logo.svg` দেখায়।
- **Hero Section:** GSAP অ্যানিমেটেড টেক্সট এবং ব্যাকগ্রাউন্ডে বিশাল 12% opacity-এর "K" লোগো ওয়াটারমার্ক (`hero_image.svg`)।
- **Professional Team Section:** Advanced Alpha Matting দিয়ে প্রসেস করা প্রফেশনাল কর্পোরেট হেডশট (1:1 Ratio, WebP format, Gray Gradient Background)।
- **Services Grid:** Lucide আইকন সমৃদ্ধ মডার্ন গ্রিড লেআউট।
- **Infrastructure as Code:** `render.yaml` দিয়ে স্বয়ংক্রিয় সার্ভার ও ডেটাবেস প্রভিশনিং।

## 8. Planned Features
- Admin প্যানেল থেকে Services এবং Team Members ডায়নামিক্যালি আপডেট করার সিস্টেম।
- ডার্ক ও লাইট থিম টগল (Theme Switcher)।
- Contact Form-এর সাথে ইমেইল নটিফিকেশন (SMTP) ইন্টিগ্রেশন।

## 9. Future Roadmap
- **Q3:** ব্লগ (Insights/Articles) সেকশন যুক্ত করা, যেখানে টেকনোলজি ও সাইবার সিকিউরিটি নিয়ে পোস্ট থাকবে।
- **Q4:** ক্লায়েন্ট পোর্টাল, যেখানে ক্লায়েন্টরা লগিন করে তাদের প্রজেক্টের স্ট্যাটাস দেখতে পারবে।

## 10. UI/UX Design System
- **Theme:** Dark Mode Default.
- **Background Color:** Deep Dark Gray/Black (`bg-textMain` / `#111111` approx).
- **Brand Colors:**
  - *Tech Blue (Primary):* `#3B82F6` থেকে `#2563EB` (Gradient)।
  - *Secure Emerald (Secondary):* `#10B981` থেকে `#059669` (Gradient)।
- **Typography:** `Inter`, `system-ui`, `-apple-system`, `sans-serif` (ক্লিন এবং কর্পোরেট লুকের জন্য)।
- **Asset Aesthetic:** লোগো এবং আইকনগুলো সম্পূর্ণ জ্যামিতিক, স্মুথ এজ (Round cap) বিশিষ্ট।

## 11. Folder ও File Structure
```text
Krypton Hub 360/
├── config/              # Main Django Configuration (settings.py, urls.py, wsgi.py)
├── core/                # Main Application (views.py, urls.py, core templates)
├── static/              # Static Assets (css, images, icons, JS)
│   ├── css/             # Tailwind output.css
│   ├── icons/           # SVGs (logo.svg, logo_white.svg, favicon.svg)
│   └── images/          # hero_image.svg, team webp images
├── templates/           # Global Templates
│   ├── base.html        # Main HTML layout
│   └── components/      # Reusable UI (navbar.html, footer.html, loader.html)
├── render.yaml          # Render Blueprint configuration
├── Procfile             # Gunicorn entry point
├── requirements.txt     # Python dependencies
└── manage.py            # Django CLI
```

## 12. Database Design
বর্তমানে পোর্টফোলিও হওয়ায় ডেটাবেস ডিজাইন একদম সিম্পল রাখা হয়েছে। ভবিষ্যতে `TeamMember`, `Service`, `ContactMessage`, `BlogPost` ইত্যাদি মডেল যুক্ত করা হবে। ডেটাবেস হিসেবে প্রোডাকশনে **PostgreSQL** ব্যবহৃত হচ্ছে।

## 13. API Structure
বর্তমানে কোনো REST API (DRF) ব্যবহার করা হয়নি। সব পেজ সরাসরি Django Template Engine দিয়ে রেন্ডার হচ্ছে। ভবিষ্যতে ক্লায়েন্ট পোর্টাল তৈরি হলে API যুক্ত করা হবে।

## 14. Business Logic
View লেয়ার থেকে কন্টেক্সট ডেটা টেমপ্লেটে পাস করা হয়। আপাতত স্ট্যাটিক পোর্টফোলিও হওয়ায় বিজনেস লজিক ন্যূনতম।

## 15. Coding Standards
- **Python:** PEP8 কমপ্লায়েন্ট। ফাংশন এবং ক্লাসগুলোতে স্পষ্ট Docstrings থাকতে হবে।
- **HTML/Django Templates:** সুন্দরভাবে ইনডেন্টেশন (Indentation) করতে হবে।
- **CSS/Tailwind:** প্রথমে Layout, তারপর Spacing, Typography, Colors এবং শেষে Effects/Transitions ক্লাস লিখতে হবে।

## 16. Naming Conventions
- **Python/Django:** `snake_case` (ভেরিয়েবল, ফাংশন, ফাইল নেম)।
- **CSS Classes/IDs:** `kebab-case`।
- **Assets/Images:** `kebab-case` বা `snake_case` (যেমন: `hero_image.svg`, `logo_white.svg`)।

## 17. Reusable Components
Django-এর `{% include %}` ট্যাগ ব্যবহার করে UI কম্পোনেন্টগুলো আলাদা করা হয়েছে:
- `templates/components/navbar.html`
- `templates/components/footer.html`
- `templates/components/loader.html`

## 18. Security Guidelines
- `SECRET_KEY` এবং `DATABASE_URL` সবসময় Environment Variable থেকে লোড করতে হবে। এগুলো কখনো হার্ডকোড করা যাবে না।
- প্রোডাকশনে অবশ্যই `DEBUG = False` থাকতে হবে।
- ফর্মে অবশ্যই `{% csrf_token %}` ব্যবহার করতে হবে।

## 19. Performance Optimization
- **Images:** সব ছবি `WebP` ফরম্যাটে সেভ করা এবং রেসোলিউশন অপ্টিমাইজড (যেমন: টিম মেম্বারদের ছবি 500x500px)।
- **Assets:** লোগো এবং আইকনগুলোর জন্য `SVG` ব্যবহার করা হয়েছে যেন ফেটে না যায় এবং সাইজ ছোট থাকে।
- **Caching:** `WhiteNoise` কম্প্রেসড স্ট্যাটিক ফাইল ক্যাশিং ব্যবহার করে। কোড আপডেট করলে HTML-এ ইমেজের নামের শেষে `?v=X` (Cache buster) আপডেট করে দিতে হবে (যেমন: `?v=8`)।

## 20. SEO Strategy
- Semantic HTML (`<header>`, `<main>`, `<section>`, `<footer>`) ব্যবহার করা।
- `base.html`-এ Open Graph (OG) মেটা ট্যাগ যুক্ত করা আছে।
- ইমেজে সব সময় অর্থবহ `alt` টেক্সট ব্যবহার করতে হবে।

## 21. Accessibility Guidelines
- ডার্ক থিমে টেক্সট কনট্রাস্ট রেশিও (Contrast Ratio) মেইনটেইন করা (কালো ব্যাকগ্রাউন্ডে অফ-হোয়াইট বা গ্রে টেক্সট)।
- ফোকাস স্টেট (Focus states) এবং কীবোর্ড নেভিগেশন মাথায় রেখে ফর্ম ও লিংক ডিজাইন করা।

## 22. Deployment Process
- **Platform:** Render.com
- **Method:** Blueprint (`render.yaml`)
- **Workflow:** গিটহাবে `main` ব্রাঞ্চে কোড পুশ করলেই স্বয়ংক্রিয়ভাবে `pip install`, `npm build`, `collectstatic`, এবং `migrate` রান হয়ে ডেপ্লয়মেন্ট হয়ে যাবে।
- **Web Server:** `gunicorn config.wsgi:application`

## 23. Testing Strategy
বর্তমানে ম্যানুয়াল (Manual) UI/UX ও রেস্পন্সিভনেস টেস্টিং করা হয়। ভবিষ্যতে লজিক বাড়লে `pytest` এবং `pytest-django` সেটআপ করা হবে।

## 24. Version History / Changelog
- **v1.0.0:** Initial Setup (Django).
- **v1.1.0:** Tailwind Integration & Dark Theme UI.
- **v1.2.0:** Brand Asset Update (New Interlocking K Logo, Hero Watermark, Pro Team Images).
- **v1.3.0:** Production Ready Setup (Render YAML, Postgres, Gunicorn).

## 25. Known Issues
বর্তমানে কোনো পরিচিত বাগ (Bug) বা সমস্যা নেই। প্রোজেক্ট সম্পূর্ণ স্টেবল অবস্থায় আছে।

## 26. Future Improvements
- Admin ড্যাশবোর্ডে কাস্টম থিম (Jazzmin) যুক্ত করা।
- পারফরম্যান্স আরও বাড়াতে Redis Caching যুক্ত করা।

## 27. Development Rules (Strict Guidelines)
1. **NO HACKY CSS:** কাস্টম CSS ফাইল যতটা সম্ভব এড়িয়ে চলতে হবে। সবকিছু Tailwind Classes দিয়ে করতে হবে।
2. **NO HEAVY JS:** React/Vue/jQuery যুক্ত করা যাবে না। সাধারণ UI লজিকের জন্য `Alpine.js` যথেষ্ট। 
3. **DO NOT MODIFY BRAND LOGO:** লোগোর জিওমেট্রিক ডিজাইন (SVG Paths) ক্লায়েন্টের সম্মতি ছাড়া পরিবর্তন করা যাবে না।
4. **ALWAYS BUMP CACHE BUSTER:** স্ট্যাটিক ফাইল (SVG/WebP) পরিবর্তন করলে HTML ফাইলে `?v=X` ভার্সন নম্বর এক বাড়িয়ে দিতে হবে, নইলে ইউজারের ব্রাউজারে পুরানো ছবি ক্যাশ হয়ে থাকবে।

## 28. AI Collaboration Guidelines (Instructions for Future AIs)
- **Read this first:** প্রজেক্টের যেকোনো বড় কাজ শুরু করার আগে এই `project_information.md` ফাইলটি পড়ে কনটেক্সট বুঝে নিতে হবে।
- **Maintain Aesthetic:** প্রজেক্টটি একটি কর্পোরেট এবং প্রিমিয়াম টেক এজেন্সির পোর্টফোলিও। তাই যেকোনো নতুন কম্পোনেন্ট ডিজাইন করার সময় ডার্ক ব্যাকগ্রাউন্ড এবং Blue/Green অ্যাক্সেন্ট কালারের সাথে সামঞ্জস্য রাখতে হবে।
- **Stay in Scope:** ইউজার নির্দিষ্ট কোনো সেকশন এডিট করতে বললে শুধু সেই সেকশনেই হাত দেওয়া যাবে। পুরো পেজের অন্য কোনো লজিক বা ডিজাইন ভাঙা যাবে না।
- **Use Exact Tools:** টার্মিনাল কমান্ড বা ফাইল এডিটের ক্ষেত্রে সবচেয়ে নিরাপদ এবং স্পেসিফিক টুল (যেমন: `replace_file_content`) ব্যবহার করতে হবে। `sed` বা `cat >>` এড়িয়ে চলতে হবে।

---
**Document Status:** 🟢 Stable & Up to date  
**Last Updated:** July 2026
