import os
import glob
from PIL import Image

source_dir = os.path.join(os.path.dirname(__file__), 'Team Image')
target_dir = os.path.join(os.path.dirname(__file__), 'static', 'images', 'team')

os.makedirs(target_dir, exist_ok=True)
image_files = glob.glob(os.path.join(source_dir, '*.*'))

TARGET_SIZE = (500, 500) # 1:1 aspect ratio

def process_image(filepath):
    try:
        filename = os.path.basename(filepath)
        name = filename.split('.')[0]
        target_path = os.path.join(target_dir, f"{name}.webp")
        
        img = Image.open(filepath).convert("RGB")
        
        # Center Crop to 1:1
        size = min(img.width, img.height)
        left = (img.width - size) // 2
        top = (img.height - size) // 2
        img = img.crop((left, top, left + size, top + size))
            
        # Resize to fit
        img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        
        # Save as WebP
        img.save(target_path, 'WEBP', quality=95)
        print(f"Original photo perfectly cropped and saved: {name} -> {target_path}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

for filepath in image_files:
    process_image(filepath)

print("Original image processing complete.")
