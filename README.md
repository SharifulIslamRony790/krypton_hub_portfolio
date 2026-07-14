# Krypton Hub - Premium Enterprise Landing Website

This is a premium, enterprise-grade landing page for **Krypton Hub**, a 360-degree digital and technology agency. The project is built using modern web technologies to ensure high performance, security, and a beautiful user experience.

## Tech Stack
- **Backend**: Django 5+, Python, PostgreSQL
- **Frontend**: Tailwind CSS, Alpine.js, HTML5
- **Animations**: GSAP (GreenSock), Lenis Smooth Scroll
- **Deployment**: Production ready for Render / Heroku with Gunicorn & WhiteNoise

## Project Structure
- `/core`: Django application handling core views and logic.
- `/templates`: Modular HTML templates including `base.html`, `loader.html`, `navbar.html`, `footer.html`.
- `/static`: Contains all assets including `css`, `images`, `icons`, and `js`.
- `config/`: Django project configuration files.

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SharifulIslamRony790/krypton_hub_portfolio.git
   cd krypton_hub_portfolio
   ```

2. **Create a virtual environment & install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install Node modules & build Tailwind CSS:**
   ```bash
   npm install
   npm run build
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   DATABASE_URL=postgres://user:password@localhost:5432/krypton_db
   ```
   *(If you want to use SQLite locally instead of Postgres, comment out the `dj_database_url` config in `settings.py`)*

5. **Run Migrations & Start Server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Customizing Assets (Images & Logos)
To update the website's assets without changing code, replace the following files:
- **Main Logo:** `static/icons/logo.svg`
- **Loader Logo (White):** `static/icons/logo_white.svg`
- **Team Photos:** `static/images/team/[name].svg` (Replace with your actual images or change the `.svg` extension in `home.html` to `.jpg/.png`).

## Deployment
The project is configured for seamless deployment on platforms like Render. It includes:
- `render.yaml` for infrastructure as code.
- `Procfile` configured with Gunicorn.
- `WhiteNoise` integration for static file serving.
