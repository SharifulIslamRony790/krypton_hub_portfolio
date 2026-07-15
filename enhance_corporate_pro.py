import os
import glob
from PIL import Image, ImageEnhance
try:
    from rembg import remove, new_session
except ImportError:
    print("rembg not found. Please install it.")
    exit(1)

source_dir = os.path.join(os.path.dirname(__file__), 'Team Image')
target_dir = os.path.join(os.path.dirname(__file__), 'static', 'images', 'team')

os.makedirs(target_dir, exist_ok=True)
image_files = glob.glob(os.path.join(source_dir, '*.*'))

TARGET_SIZE = (500, 500)

def create_gradient_bg(size, top_color, bottom_color):
    base = Image.new('RGB', size, top_color)
    bottom = Image.new('RGB', size, bottom_color)
    mask = Image.new('L', size)
    mask_data = []
    for y in range(size[1]):
        mask_data.extend([int(255 * (y / size[1]))] * size[0])
    mask.putdata(mask_data)
    base.paste(bottom, (0, 0), mask)
    return base

# Create a sleek corporate light-gray/blue-gray background for the white cards
bg_image = create_gradient_bg(TARGET_SIZE, (243, 244, 246), (229, 231, 235)) # Tailwind gray-100 to gray-200

# We use u2net session
session = new_session("u2net")

def process_image(filepath):
    try:
        filename = os.path.basename(filepath)
        name = filename.split('.')[0]
        target_path = os.path.join(target_dir, f"{name}.webp")
        
        with open(filepath, 'rb') as f:
            input_bytes = f.read()
        
        # Remove background using rembg WITH Alpha Matting for high quality edges
        output_bytes = remove(
            input_bytes, 
            session=session,
            alpha_matting=True,
            alpha_matting_foreground_threshold=240,
            alpha_matting_background_threshold=10,
            alpha_matting_erode_size=10
        )
        
        import io
        img = Image.open(io.BytesIO(output_bytes)).convert("RGBA")
        
        # Enhance foreground (the person) to look more professional (slightly more contrast and color)
        img = ImageEnhance.Contrast(img).enhance(1.05)
        img = ImageEnhance.Color(img).enhance(1.05)
        
        # Center Crop the face/body
        size = min(img.width, img.height)
        left = (img.width - size) // 2
        top = (img.height - size) // 2
        img = img.crop((left, top, left + size, top + size))
            
        # Resize to fit the background
        img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        
        # Composite over corporate background
        final_img = bg_image.copy()
        final_img.paste(img, (0, 0), img)
        
        # Save as WebP
        final_img.save(target_path, 'WEBP', quality=95)
        print(f"Professional corporate portrait created: {name} -> {target_path}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

for filepath in image_files:
    process_image(filepath)

print("Corporate Team image processing with Alpha Matting complete.")
