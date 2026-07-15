import os

def create_svg(path, text, width, height, bg_color="#1E293B", text_color="#F8FAFC"):
    font_size = min(width // 10, height // 3)
    font_size = max(font_size, 16)
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <rect width="100%" height="100%" fill="{bg_color}"/>
    <text x="50%" y="50%" font-family="system-ui, -apple-system, sans-serif" font-size="{font_size}" font-weight="600" fill="{text_color}" text-anchor="middle" dominant-baseline="middle">{text}</text>
</svg>'''
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg_content)

base_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(base_dir, 'static')

# Create placeholders
create_svg(os.path.join(static_dir, 'images', 'hero', 'hero_image.svg'), "Hero Image (1920x1080)", 1920, 1080, "#0F172A", "#38BDF8")

# Team
team_members = ['nabid', 'rony', 'khairul', 'abdullah', 'farzana', 'afia', 'nurul', 'rifat']
for member in team_members:
    create_svg(os.path.join(static_dir, 'images', 'team', f'{member}.svg'), f"{member.title()} (400x400)", 400, 400)

# Services
services = ['software', 'cybersecurity', 'marketing', 'design']
for service in services:
    create_svg(os.path.join(static_dir, 'images', 'services', f'{service}.svg'), f"{service.title()} (800x600)", 800, 600)

# Clients
for i in range(1, 6):
    create_svg(os.path.join(static_dir, 'images', 'clients', f'client_{i}.svg'), f"Client {i}", 200, 100, "#334155", "#94A3B8")

# Logo
create_svg(os.path.join(static_dir, 'icons', 'logo.svg'), "Krypton 360°", 200, 60, "transparent", "#111111")
create_svg(os.path.join(static_dir, 'icons', 'logo_white.svg'), "Krypton 360°", 200, 60, "transparent", "#FAFAFA")
create_svg(os.path.join(static_dir, 'icons', 'logo_dark.svg'), "Krypton 360°", 200, 60, "transparent", "#FAFAFA")
create_svg(os.path.join(static_dir, 'icons', 'logo_master.svg'), "Krypton 360°", 400, 120, "transparent", "#111111")
create_svg(os.path.join(static_dir, 'icons', 'logo_icon.svg'), "360°", 120, 120, "#111111", "#FAFAFA")
create_svg(os.path.join(static_dir, 'icons', 'favicon.svg'), "360°", 64, 64, "#111111", "#FAFAFA")
create_svg(os.path.join(static_dir, 'icons', 'apple-touch-icon.png'), "360°", 180, 180, "#111111", "#FAFAFA")
