# Krypton 360° | Premium Digital & Tech Agency

![Krypton 360 Logo](static/icons/logo_white.svg)

Krypton 360° is a high-performance, dynamic technical agency web application and CRM system built on a modern Django Monolithic Architecture. It is designed to handle high traffic securely while providing an ultra-premium user experience with smooth GSAP animations and Alpine.js reactivity.

## ✨ Key Features

- **Dynamic Services & Team:** Easily manage agency services and team members dynamically from the premium admin dashboard.
- **Advanced Lead Generation:** A highly secure contact form that blocks fake emails using DNS MX Record verification.
- **Enterprise-Grade Security:**
  - Google reCAPTCHA v2 (Bot Protection)
  - API Rate Limiting (Brute-Force Protection)
  - Zero-Trust Input Sanitization (XSS Prevention)
  - Server-Side Regex Phone Validation
- **High-Performance Caching:** Database queries on the landing page are cached in memory to handle thousands of concurrent users seamlessly.
- **Premium Admin Dashboard:** Custom Django Jazzmin dashboard with interactive Chart.js analytics for lead tracking.

---

## 🏗️ Architecture & Tech Stack

- **Backend:** Python 3.12+, Django 5.2+ (MVT Architecture)
- **Database:** PostgreSQL (Neon DB for production, SQLite for local dev)
- **Frontend:** HTML5, Tailwind CSS, Alpine.js, GSAP (GreenSock Animation Platform)
- **Security Layer:** `django-ratelimit`, `email-validator`, Google reCAPTCHA API
- **Deployment:** Render.com (via `render.yaml` Infrastructure as Code)

---

## 🚀 Local Development Setup

Follow these instructions to set up the project locally on your machine.

### 1. Prerequisites
- Python 3.12 or higher installed.
- Git installed.

### 2. Clone the Repository
```bash
git clone https://github.com/SharifulIslamRony790/krypton_hub_portfolio.git
cd krypton_hub_portfolio
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Environment Variables
Create a `.env` file in the root directory and add the following keys:
```env
SECRET_KEY=your_secure_django_secret_key
DEBUG=True
DB_NAME=krypton_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
RECAPTCHA_SITE_KEY=your_google_recaptcha_site_key
RECAPTCHA_SECRET_KEY=your_google_recaptcha_secret_key
```

### 6. Apply Migrations & Populate Data
```bash
python manage.py migrate
python populate_db.py
```

### 7. Run the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to view the site!

---

## 🔒 Security Best Practices Implemented
This project strictly follows the **8 Rules of Clean Coding** and advanced security protocols:
1. **No Hardcoded Secrets:** All sensitive API keys are loaded via `.env`.
2. **Rate Limiting:** Form submissions are restricted to `5/minute` per IP.
3. **Database Caching:** Optimized static queries (`Service`, `TeamMember`) using memory caching logic.

## 📄 License
© 2026 Krypton 360 Agency. All rights reserved.
