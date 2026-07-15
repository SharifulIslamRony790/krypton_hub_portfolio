import os
from PIL import Image, ImageEnhance
import glob

# Paths
source_dir = os.path.join(os.path.dirname(__file__), 'Team Image')
target_dir = os.path.join(os.path.dirname(__file__), 'static', 'images', 'team')

os.makedirs(target_dir, exist_ok=True)

# List all jpeg/jpg images
image_files = glob.glob(os.path.join(source_dir, '*.*'))

TARGET_SIZE = (800, 1000) # 4:5 aspect ratio

def process_image(filepath):
    try:
        filename = os.path.basename(filepath)
        name, _ = os.path.splitext(filename)
        # Handle cases like name.jpg.jpeg
        name = name.replace('.jpg', '')
        
        target_path = os.path.join(target_dir, f"{name}.webp")
        
        with Image.open(filepath) as img:
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Crop to aspect ratio (center crop)
            target_aspect = TARGET_SIZE[0] / TARGET_SIZE[1]
            img_aspect = img.width / img.height
            
            if img_aspect > target_aspect:
                # Image is too wide
                new_width = int(target_aspect * img.height)
                left = (img.width - new_width) // 2
                img = img.crop((left, 0, left + new_width, img.height))
            elif img_aspect < target_aspect:
                # Image is too tall
                new_height = int(img.width / target_aspect)
                top = (img.height - new_height) // 2
                img = img.crop((0, top, img.width, top + new_height))
            
            # Resize
            img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
            
            # Enhance
            # 1. Contrast
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.05) # slight boost
            # 2. Color
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.1) # slight saturation boost
            # 3. Sharpness
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.2) # crisp professional look
            
            # Save as WebP
            img.save(target_path, 'WEBP', quality=85)
            print(f"Processed: {name} -> {target_path}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

for filepath in image_files:
    process_image(filepath)

print("Team image processing complete.")
