from PIL import Image, ImageDraw, ImageFont
import os

static_dir = os.path.join(os.path.dirname(__file__), 'static', 'icons')

def create_favicon(filename, size=(64, 64), text="360°", font_size=20, bg_color="#111111", text_color="#FAFAFA"):
    img = Image.new('RGBA', size, color=bg_color)
    d = ImageDraw.Draw(img)
    # Try to load a generic font, otherwise default
    try:
        font = ImageFont.truetype("arialbd.ttf", font_size)
    except:
        font = ImageFont.load_default(size=font_size)
    
    # Get bounding box
    bbox = d.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    # Calculate x, y position
    x = (size[0] - text_w) / 2
    y = (size[1] - text_h) / 2
    
    d.text((x, y), text, font=font, fill=text_color)
    img.save(os.path.join(static_dir, filename))
    print(f"Created {filename}")

if __name__ == "__main__":
    create_favicon('favicon.png', size=(64, 64), font_size=24)
    create_favicon('apple-touch-icon.png', size=(180, 180), font_size=60)
