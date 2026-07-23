# 🚀 Krypton 360° - Project Information & SSOT (Single Source of Truth)

This document serves as the **Single Source of Truth (SSOT)** for the **Krypton 360°** project. Any human developer or AI assistant working on this project MUST read and adhere to the guidelines, architecture, and principles outlined in this file before making any changes.

---

## 1. প্রজেক্ট পরিচিতি (Project Overview)
**Krypton 360°** (পূর্বে *Krypton Hub 360*) হলো একটি আধুনিক, প্রিমিয়াম এবং হাই-পারফরম্যান্স টেকনিক্যাল ও ডিজিটাল এজেন্সির পোর্টফোলিও ওয়েবসাইট এবং ডায়নামিক CRM সিস্টেম। এটি মূলত কোম্পানির সার্ভিস, টিম মেম্বারদের পরিচিতি, ক্লায়েন্ট লিড এবং ব্র্যান্ড আইডেন্টিটি একটি প্রফেশনাল ও কর্পোরেট রূপের পাশাপাশি অ্যাডমিন ড্যাশবোর্ড থেকে সম্পূর্ণ কাস্টমাইজ করার সুবিধা প্রদান করে।

## 2. উদ্দেশ্য ও ভিশন (Vision & Goals)
- **Vision:** "Design Bold. Build Secure. Scale Smart." - এই স্লোগানটিকে কেন্দ্র করে একটি বিশ্বস্ত, আধুনিক এবং সিকিউর ডিজিটাল উপস্থিতি তৈরি করা।
- **Goals:** 
  - ভিজিটরদের প্রথম দেখাতেই (First Impression) প্রিমিয়াম ফিল দেওয়া।
  - একটি ডার্ক-থিম ভিত্তিক, অত্যাধুনিক UI/UX নিশ্চিত করা।
  - লাইটওয়েট এবং অত্যন্ত দ্রুত লোড হওয়া ওয়েবসাইট তৈরি করা।
  - অ্যাডমিন প্যানেল থেকে সার্ভিস, টিম মেম্বার এবং লিড ম্যানেজমেন্ট সম্পূর্ণ ডায়নামিক্যালি নিয়ন্ত্রণ করা।

## 3. সম্পূর্ণ Planning ও Development Process
প্রজেক্টটি কয়েকটি ধাপে (Phases) ডেভেলপ করা হয়েছে:
- **Phase 1 (Foundation):** Django-এর মাধ্যমে বেসিক প্রজেক্ট এবং অ্যাপ স্ট্রাকচার তৈরি। 
- **Phase 2 (UI/UX Overhaul):** Tailwind CSS, Alpine.js এবং GSAP ব্যবহার করে সম্পূর্ণ ওয়েবসাইটটিকে একটি মডার্ন ডার্ক-থিমে রূপান্তর এবং অ্যানিমেশন যুক্ত করা।
- **Phase 3 (Brand Identity Update):** সম্পূর্ণ নতুন "Krypton 360°" ব্র্যান্ড আইডেন্টিটি তৈরি। Advanced Alpha Matting-এর মাধ্যমে টিম মেম্বারদের ছবিগুলো কর্পোরেট ব্যাকগ্রাউন্ডে রূপান্তর।
- **Phase 4 (Dynamic CRM & Admin Dashboard):** Django Models (`Service`, `TeamMember`, `ContactMessage`), Jazzmin Custom Admin Template, Chart.js Analytics এবং Donut Chart Integration।
- **Phase 5 (Production Readiness & Bug Fixes):** Render.com-এ ডেপ্লয়মেন্টের জন্য `render.yaml`, Neon PostgreSQL, Gunicorn, WhiteNoise এবং Production Media Serving (`django.views.static.serve`) কনফিগারেশন।

## 4. Project Architecture
প্রজেক্টটি ক্লাসিক **Monolithic Architecture** অনুসরণ করে তৈরি, যা Django-এর **MVT (Model-View-Template)** ডিজাইন প্যাটার্নের ওপর ভিত্তি করে দাঁড়িয়ে আছে।

## 5. ব্যবহৃত Technology Stack এবং নির্বাচনের কারণ
- **Backend:** `Python 3.12+ / Django 5.2+`
- **Database:** `PostgreSQL` (Hosted on Neon DB in production via `DATABASE_URL`)
- **Admin Dashboard:** `django-jazzmin` + Custom Dashboard Overrides (`templates/admin/index.html`) + `Chart.js`
- **Frontend Styling:** `Tailwind CSS`
- **Frontend Interactions:** `Alpine.js`
- **Animations:** `GSAP (GreenSock)`
- **Icons:** `Lucide Icons`
- **Static Files Serving:** `WhiteNoise` (`CompressedManifestStaticFilesStorage`)
- **Media Serving:** `django.views.static.serve` via `re_path` for `DEBUG=False` on Render
- **Production Server:** `Gunicorn`

## 6. Folder ও File Structure
```text
Krypton 360/
├── config/                      # Main Django Configuration (settings.py, urls.py, wsgi.py)
├── core/                        # Main Application (models.py, views.py, urls.py, admin.py)
│   └── templatetags/            # Custom template tags (dashboard_tags.py)
├── static/                      # Static Assets (css, images, icons)
├── media/                       # Uploaded Team Member Headshots (media/team/)
├── templates/                   # Global & Override Templates
│   ├── base.html                # Main layout
│   ├── admin/index.html         # Custom Jazzmin Analytics Dashboard override
│   └── components/              # Reusable UI (navbar.html, footer.html, loader.html)
├── populate_db.py               # Auto-population & media copy script for deployment
├── render.yaml                  # Render Blueprint configuration
├── Procfile                     # Gunicorn entry point
├── requirements.txt             # Python dependencies
└── AGENTS.md                    # AI Agent System Architecture Documentation
```

## 7. Database Models (`core/models.py`)
- **`ContactMessage`**: Stores client leads (name, email, company, phone, service, message, is_read, created_at).
- **`Service`**: Stores dynamic services (title, description, icon_name, color_theme, order, features).
- **`TeamMember`**: Stores team members (name, designation, department, bio, image, order).

## 8. Development & Deployment Rules (Strict Guidelines)
1. **Model Imports in Scripts:** Standalone Python scripts (e.g., `populate_db.py`) MUST call `django.setup()` BEFORE importing models.
2. **Production Media Serving:** `config/urls.py` MUST maintain `re_path(r'^media/(?P<path>.*)$', serve, ...)` to serve media images when `DEBUG=False` on Render.
3. **No Raw CSS Hacks:** Always prioritize Tailwind utility classes.
4. **Environment Variables:** Never hardcode `SECRET_KEY` or `DATABASE_URL`. Always read from `os.getenv()`.

---
**Document Status:** 🟢 Up to date  
**Last Updated:** July 2026
