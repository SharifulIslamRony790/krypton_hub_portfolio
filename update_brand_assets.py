import os
import re

static_icons_dir = os.path.join(os.path.dirname(__file__), 'static', 'icons')
static_hero_dir = os.path.join(
    os.path.dirname(__file__),
    'static',
    'images',
    'hero')
templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
core_templates_dir = os.path.join(
    os.path.dirname(__file__), 'core', 'templates')

os.makedirs(static_icons_dir, exist_ok=True)
os.makedirs(static_hero_dir, exist_ok=True)

svg_logo_dark_text = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 60" width="250" height="60">  # noqa: E501
    <defs>
        <clipPath id="front-ring-clip">
            <rect x="0" y="55" width="45" height="45" />
        </clipPath>
    </defs>
    <g transform="translate(5, 5) scale(0.5)">
        <ellipse cx="55" cy="50" rx="40" ry="15" transform="rotate(-30 55 50)" fill="none" stroke="#2563EB" stroke-width="8"/>  # noqa: E501
        <path d="M 35 20 L 35 80 M 35 55 L 70 20 M 50 40 L 80 80" fill="none" stroke="#2563EB" stroke-width="8" stroke-linecap="square" stroke-linejoin="miter"/>  # noqa: E501
        <ellipse cx="55" cy="50" rx="40" ry="15" transform="rotate(-30 55 50)" fill="none" stroke="#2563EB" stroke-width="8" clip-path="url(#front-ring-clip)"/>  # noqa: E501
    </g>
    <text x="65" y="42" font-family="'Inter', system-ui, -apple-system, sans-serif" font-size="28" font-weight="700" fill="#111111">Krypton 360°</text>  # noqa: E501
</svg>"""

svg_logo_white_text = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 250 60" width="250" height="60">  # noqa: E501
    <defs>
        <clipPath id="front-ring-clip">
            <rect x="0" y="55" width="45" height="45" />
        </clipPath>
    </defs>
    <g transform="translate(5, 5) scale(0.5)">
        <ellipse cx="55" cy="50" rx="40" ry="15" transform="rotate(-30 55 50)" fill="none" stroke="#2563EB" stroke-width="8"/>  # noqa: E501
        <path d="M 35 20 L 35 80 M 35 55 L 70 20 M 50 40 L 80 80" fill="none" stroke="#2563EB" stroke-width="8" stroke-linecap="square" stroke-linejoin="miter"/>  # noqa: E501
        <ellipse cx="55" cy="50" rx="40" ry="15" transform="rotate(-30 55 50)" fill="none" stroke="#2563EB" stroke-width="8" clip-path="url(#front-ring-clip)"/>  # noqa: E501
    </g>
    <text x="65" y="42" font-family="'Inter', system-ui, -apple-system, sans-serif" font-size="28" font-weight="700" fill="#FFFFFF">Krypton 360°</text>  # noqa: E501
</svg>"""

svg_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60" width="60" height="60">  # noqa: E501
    <defs>
        <clipPath id="front-ring-clip">
            <rect x="0" y="55" width="45" height="45" />
        </clipPath>
    </defs>
    <g transform="translate(5, 5) scale(0.5)">
        <ellipse cx="55" cy="50" rx="40" ry="15" transform="rotate(-30 55 50)" fill="none" stroke="#2563EB" stroke-width="8"/>  # noqa: E501
        <path d="M 35 20 L 35 80 M 35 55 L 70 20 M 50 40 L 80 80" fill="none" stroke="#2563EB" stroke-width="8" stroke-linecap="square" stroke-linejoin="miter"/>  # noqa: E501
        <ellipse cx="55" cy="50" rx="40" ry="15" transform="rotate(-30 55 50)" fill="none" stroke="#2563EB" stroke-width="8" clip-path="url(#front-ring-clip)"/>  # noqa: E501
    </g>
</svg>"""

svg_hero_watermark = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">  # noqa: E501
    <defs>
        <clipPath id="front-ring-clip">
            <rect x="0" y="55" width="45" height="45" />
        </clipPath>
    </defs>
    <!-- Huge faint stylized K Icon watermark -->
    <g transform="translate(850, 250) scale(15)" opacity="0.05">
        <ellipse cx="55" cy="50" rx="40" ry="15" transform="rotate(-30 55 50)" fill="none" stroke="#FFFFFF" stroke-width="8"/>  # noqa: E501
        <path d="M 35 20 L 35 80 M 35 55 L 70 20 M 50 40 L 80 80" fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="square" stroke-linejoin="miter"/>  # noqa: E501
        <ellipse cx="55" cy="50" rx="40" ry="15" transform="rotate(-30 55 50)" fill="none" stroke="#FFFFFF" stroke-width="8" clip-path="url(#front-ring-clip)"/>  # noqa: E501
    </g>
</svg>"""

files_to_write = {
    os.path.join(static_icons_dir, 'logo.svg'): svg_logo_dark_text,
    os.path.join(static_icons_dir, 'logo_dark.svg'): svg_logo_dark_text,
    os.path.join(static_icons_dir, 'logo_white.svg'): svg_logo_white_text,
    os.path.join(static_icons_dir, 'logo_master.svg'): svg_logo_dark_text,
    os.path.join(static_icons_dir, 'logo_icon.svg'): svg_icon,
    os.path.join(static_icons_dir, 'favicon.svg'): svg_icon,
    os.path.join(static_hero_dir, 'hero_image.svg'): svg_hero_watermark,
}

for filepath, content in files_to_write.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {filepath}")


def update_cache_busters(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace any ?v=X with ?v=8 for svg files
                new_content = re.sub(r'(\.svg)\?v=\d+', r'\1?v=8', content)

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated cache busters in: {filepath}")


update_cache_busters(templates_dir)
update_cache_busters(core_templates_dir)

print("Brand assets updated perfectly!")
