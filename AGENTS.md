# 🤖 Agent Context & Architectural System Documentation: Krypton 360°

This document is optimized specifically for AI Coding Agents (LLMs, pair programmers, subagents) working on the **Krypton 360°** codebase. It provides explicit system context, architectural constraints, schemas, deployment workflows, and coding rules required to safely navigate, modify, and extend this project.

---

## 1. System Overview & Technology Stack

**Krypton 360°** is a high-performance, dynamic technical agency web application and CRM system built on a modern Django Monolithic Architecture.

### Core Stack
- **Framework:** Python 3.12+ / Django 5.2+
- **Architecture Pattern:** MVT (Model-View-Template)
- **Database:** PostgreSQL (Hosted on Neon DB in production via `DATABASE_URL`; fallback to local SQLite for development)
- **Admin & Dashboard:** `django-jazzmin` with custom KPI cards & Chart.js doughnut analytics
- **Static File Handling:** WhiteNoise (`CompressedManifestStaticFilesStorage`)
- **Media File Handling:** Production media serving via `django.views.static.serve` (`re_path(r'^media/(?P<path>.*)$')`)
- **Production Server:** Gunicorn (WSGI)
- **Deployment Platform:** Render.com (Managed via `render.yaml` Blueprint)

### Frontend Stack
- **Styling:** Tailwind CSS (Built via npm build pipeline)
- **Interactivity:** Alpine.js (Lightweight reactive state for navbar, dynamic UI elements)
- **Animations:** GSAP (GreenSock Animation Platform for smooth scroll & hero animations)
- **Icons:** Lucide Icons (Web component SVG icons)

---

## 2. Directory & Module Map

```text
Krypton 360/
├── config/                      # Project Configuration Package
│   ├── __init__.py
│   ├── settings.py              # Core settings (DB, Jazzmin, Installed Apps, Static/Media)
│   ├── urls.py                  # Global URL routing & Production Media serving handler
│   ├── wsgi.py                  # WSGI entry point for Gunicorn
│   └── asgi.py                  # ASGI entry point
├── core/                        # Main Application Package
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── dashboard_tags.py    # Custom tags (`get_dashboard_stats`) for Admin metrics & Chart data
│   ├── templates/core/
│   │   └── home.html            # Main dynamic landing page template
│   ├── admin.py                 # Django admin registrations for ContactMessage, Service, TeamMember
│   ├── apps.py                  # Core app configuration
│   ├── models.py                # Database schemas (ContactMessage, Service, TeamMember)
│   ├── urls.py                  # Application routes (Home view & Contact form handler)
│   └── views.py                 # View functions (`home_view`)
├── templates/                   # Global & Override Templates
│   ├── base.html                # Main layout (Meta, OG, Tailwind output CSS, Alpine, GSAP)
│   ├── admin/
│   │   └── index.html           # Jazzmin override for custom Analytics Dashboard & Chart.js
│   └── components/
│       ├── navbar.html          # Alpine.js-powered responsive navigation bar
│       ├── footer.html          # Footer component
│       └── loader.html          # Dynamic preloader component
├── static/                      # Source & Processed Static Assets
│   ├── css/                     # Tailwind input & compiled output CSS
│   ├── icons/                   # Brand SVGs (logo.svg, logo_white.svg, favicon.svg)
│   └── images/                  # Static team headshots & hero background SVG
├── media/                       # User/Script Uploaded Media Files
│   └── team/                    # Team member 1:1 WebP images
├── populate_db.py               # Database initial populator & static-to-media image copier
├── render.yaml                  # Infrastructure as Code (IaC) deployment definition for Render
├── Procfile                     # Gunicorn process definition
├── requirements.txt             # Python dependencies
└── manage.py                    # Django CLI runner
```

---

## 3. Database Schema & Data Models (`core/models.py`)

### 3.1 `ContactMessage`
Stores client leads submitted via the landing page contact form.
- `name` (CharField, max 255): Client full name.
- `email` (EmailField): Client email address.
- `company` (CharField, max 255, optional): Company name.
- `phone` (CharField, max 50, optional): Phone number.
- `service` (CharField, max 50): Chosen service key (`software`, `cybersecurity`, `marketing`, `design`, `full_stack`, `other`).
- `message` (TextField): Inquiry details.
- `created_at` (DateTimeField, `auto_now_add=True`): Timestamp.
- `is_read` (BooleanField, default=False): Status flag for dashboard tracking.

### 3.2 `Service`
Stores agency services dynamically displayed on the landing page and managed via Admin.
- `title` (CharField, max 200): Service title.
- `description` (TextField): Short summary.
- `icon_name` (CharField, max 100): Lucide icon identifier (e.g. `code-2`, `shield-check`, `trending-up`, `palette`).
- `color_theme` (CharField, max 50): Accent color modifier (e.g., `accent`, `success`, `orange-400`, `purple-400`).
- `order` (PositiveIntegerField, default=0): Grid presentation order.
- `features` (TextField): Newline-separated bullet points (`get_features_list()` helper parses this into a list).

### 3.3 `TeamMember`
Stores team profile details managed dynamically via Admin.
- `name` (CharField, max 200): Team member full name.
- `designation` (CharField, max 200): Role title (e.g. `Full-Stack Developer`).
- `department` (CharField, max 100): Department name (e.g. `Advanced Engineering`).
- `bio` (TextField): Short biography.
- `image` (ImageField, upload_to="team/"): WebP format corporate headshot.
- `order` (PositiveIntegerField, default=0): Presentation order.

---

## 4. Key Workflows & Architectural Decisions

### 4.1 Production Media Serving Pattern (`config/urls.py`)
In production (`DEBUG=False`), Django's default `static(settings.MEDIA_URL, ...)` helper does not serve media files. To prevent 404 errors on Render for uploaded team images without requiring an external S3 bucket, `config/urls.py` uses `django.views.static.serve` via `re_path`:
```python
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
```

### 4.2 Automated Initial Data Population (`populate_db.py`)
- Standard standalone script used to initialize default services and copy static team images to `media/team/`.
- **CRITICAL EXECUTION RULE:** `django.setup()` MUST be invoked BEFORE importing models (`from core.models import ...`), otherwise Django throws an `ImproperlyConfigured` exception.
- Automatically invoked during the Render build pipeline.

### 4.3 Production Deployment Pipeline (`render.yaml`)
- Render builds the web service using:
  ```bash
  pip install -r requirements.txt && npm install && npm run build && python manage.py collectstatic --noinput && python manage.py migrate && python populate_db.py
  ```
- Application entry point: `gunicorn config.wsgi:application`.
- Environment Variable: `DATABASE_URL` is configured in the Render Dashboard targeting the Neon PostgreSQL instance.

---

## 5. Custom Admin & Analytics Dashboard

- **Template:** `templates/admin/index.html` overrides Jazzmin's default index view.
- **Template Tag:** `core/templatetags/dashboard_tags.py` defines `{% get_dashboard_stats %}`.
- **KPI Metrics:**
  - `total_leads`: Count of all `ContactMessage` objects.
  - `unread_leads`: Count of `ContactMessage` objects where `is_read=False`.
  - `active_services`: Count of `Service` objects.
  - `team_count`: Count of `TeamMember` objects.
- **Analytics Chart:** Renders a Chart.js Donut chart summarizing leads grouped by requested service (`chart_labels`, `chart_data`).

---

## 6. Strict Rules & Constraints for AI Agents

1. **Do NOT break `django.setup()` order in standalone scripts:**
   Always set `DJANGO_SETTINGS_MODULE` and run `django.setup()` before importing any models from Django apps.
2. **Do NOT remove media URL serving in `config/urls.py`:**
   `re_path(r'^media/(?P<path>.*)$', serve, ...)` must remain active to allow team images to load in production (`DEBUG=False`).
3. **Do NOT hardcode environment secrets:**
   `SECRET_KEY` and `DATABASE_URL` must always be retrieved using `os.getenv()`.
4. **Maintain Design System Aesthetic:**
   - Default: Dark Mode.
   - Primary Accent: Tech Blue (`#3B82F6` to `#2563EB`).
   - Secondary Accent: Secure Emerald (`#10B981` to `#059669`).
   - Styling: Use Tailwind CSS classes exclusively. Avoid raw inline CSS unless necessary for dynamic Chart.js canvas containers.
5. **Cache Busting Rule:**
   When updating static assets (SVGs or WebP images), increment the `?v=X` cache-buster query parameter in the template tags.
