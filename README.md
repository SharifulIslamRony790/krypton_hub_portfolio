# 🚀 Krypton 360° - Enterprise Technical Agency Web Application & Dynamic CRM

**Krypton 360°** is a high-performance, dynamic technical agency web application, portfolio, and Content Management System (CRM) built on a modern Django Monolithic Architecture. It showcases agency services, team members, and client lead management with a custom-built analytics admin dashboard.

---

## 🌟 Key Features

- **Dynamic Landing Page**: Responsive dark-mode interface featuring dynamic Services grid and Team Member roster.
- **Custom Admin & Analytics Dashboard**: Built on `django-jazzmin` with live KPI metric cards (Total Leads, Unread Inquiries, Active Services, Team Members) and an interactive **Chart.js** Donut Chart ("Leads by Service").
- **Dynamic Content Management (CRM)**: Agency owners can manage Services, Team Members, and Client Messages directly from the Admin Dashboard without touching code.
- **Interactive UI & Smooth Animations**: Powered by Alpine.js for lightweight state management and GSAP (GreenSock) for smooth scroll animations.
- **Production Media & Asset Handling**: Self-contained production media serving via `django.views.static.serve` and WhiteNoise static asset compression.
- **Automated Data Seeding**: Includes `populate_db.py` to auto-initialize default agency services, corporate team headshots, and data during build/deployment.
- **Infrastructure as Code**: Configured for automated deployment on Render.com via `render.yaml` Blueprint.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend Framework** | Python 3.12+ / Django 5.2+ |
| **Database** | PostgreSQL (Neon DB in Production via `DATABASE_URL`) / SQLite (Local Fallback) |
| **Admin & CRM** | Django Jazzmin, Custom Template Tags, Chart.js Analytics |
| **Frontend Styling** | Tailwind CSS (Compiled via npm build pipeline) |
| **Interactivity** | Alpine.js |
| **Animations** | GSAP (GreenSock) |
| **Icons** | Lucide Icons (Web Components) |
| **Production Server** | Gunicorn (WSGI) |
| **Static & Media** | WhiteNoise (`CompressedManifestStaticFilesStorage`), Django Static Serve |
| **Deployment** | Render.com (`render.yaml` Blueprint) |

---

## 📁 Project Directory Structure

```text
Krypton 360/
├── config/                      # Core Django Project Configuration
│   ├── settings.py              # Environment, DB, Jazzmin, Static & Media settings
│   ├── urls.py                  # Global Routing & Production Media Handler
│   └── wsgi.py                  # Gunicorn WSGI Entry Point
├── core/                        # Main Application Package
│   ├── templatetags/
│   │   └── dashboard_tags.py    # Custom tags (`get_dashboard_stats`) for Admin metrics & Chart data
│   ├── templates/core/
│   │   └── home.html            # Dynamic Landing Page Template
│   ├── admin.py                 # Admin Registrations (ContactMessage, Service, TeamMember)
│   ├── models.py                # Database Schemas
│   ├── urls.py                  # Application Routes & Form Processing
│   └── views.py                 # Landing Page View & Lead Capture Handler
├── templates/                   # Global Templates & Overrides
│   ├── base.html                # Main Layout (Tailwind output, Alpine, GSAP)
│   ├── admin/
│   │   └── index.html           # Custom Analytics Dashboard Override with Chart.js
│   └── components/              # Reusable UI (navbar.html, footer.html, loader.html)
├── static/                      # Compiled CSS, Brand SVGs, and Raw Assets
├── media/                       # Uploaded & Seeded Media Files (media/team/)
├── populate_db.py               # Auto-population script for Services & Team Members
├── render.yaml                  # Render Blueprint IaC configuration
├── Procfile                     # Gunicorn Process Definition
├── requirements.txt             # Python Dependencies
├── AGENTS.md                    # AI Agent System Context & Architectural Guidelines
└── project_information.md       # Project Single Source of Truth (SSOT)
```

---

## 🗄️ Database Schemas (`core/models.py`)

1. **`ContactMessage`**: Client inquiry leads submitted via the landing page form.
   - Fields: `name`, `email`, `company`, `phone`, `service`, `message`, `is_read`, `created_at`.
2. **`Service`**: Agency offerings dynamically rendered on the website.
   - Fields: `title`, `description`, `icon_name` (Lucide icon identifier), `color_theme`, `order`, `features` (newline-separated bullet list).
3. **`TeamMember`**: Dynamic team profiles.
   - Fields: `name`, `designation`, `department`, `bio`, `image` (WebP corporate headshots uploaded to `media/team/`), `order`.

---

## 💻 Local Development Setup

### 1. Clone & Setup Virtual Environment
```bash
git clone https://github.com/SharifulIslamRony790/krypton_hub_portfolio.git
cd krypton_hub_portfolio

python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
npm install
```

### 3. Build Static Assets
```bash
npm run build
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://user:password@localhost:5432/krypton_db
```

### 5. Run Migrations & Populate Initial Data
```bash
python manage.py migrate
python populate_db.py
```

### 6. Start Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser. Access the custom admin panel at `http://127.0.0.1:8000/admin/`.

---

## 🚀 Production Deployment (Render.com)

The application is fully pre-configured for automated deployment on Render using the `render.yaml` blueprint.

- **Build Command**:
  ```bash
  pip install -r requirements.txt && npm install && npm run build && python manage.py collectstatic --noinput && python manage.py migrate && python populate_db.py
  ```
- **Start Command**:
  ```bash
  gunicorn config.wsgi:application
  ```
- **Environment Configuration**: Set `DATABASE_URL` in the Render dashboard pointing to your PostgreSQL database instance (e.g. Neon DB).

---

## 🤖 AI Agent & Developer Guidelines

For developers or AI coding agents working on this project, please consult:
- **`AGENTS.md`**: Contains strict constraints, execution rules, and system details for AI agents.
- **`project_information.md`**: Single Source of Truth (SSOT) covering vision, architecture, and changelog.

---

## 📝 License & Copyright

© **Krypton 360° Agency**. All rights reserved.
