import os
import glob
from PIL import Image, ImageEnhance
try:
    from rembg import remove
except ImportError:
    print("rembg not found. Please install it.")
    exit(1)

source_dir = os.path.join(os.path.dirname(__file__), 'Team Image')
target_dir = os.path.join(
    os.path.dirname(__file__),
    'static',
    'images',
    'team')

os.makedirs(target_dir, exist_ok=True)
image_files = glob.glob(os.path.join(source_dir, '*.*'))

TARGET_SIZE = (800, 1000)  # 4:5 aspect ratio


def create_gradient_bg(size, top_color, bottom_color):
    base = Image.new('RGB', size, top_color)
    Image.new('RGB', size, top_color)
    bottom = Image.new('RGB', size, bottom_color)
    mask = Image.new('L', size)
    mask_data = []
    for y in range(size[1]):
        mask_data.extend([int(255 * (y / size[1]))] * size[0])
    mask.putdata(mask_data)
    base.paste(bottom, (0, 0), mask)
    return base


bg_image = create_gradient_bg(
    TARGET_SIZE, (17, 17, 17), (31, 41, 55))  # 111111 to #1F2937


def process_image(filepath):
    try:
        filename = os.path.basename(filepath)
        name = filename.split('.')[0]
        target_path = os.path.join(target_dir, f"{name}.webp")

        with open(filepath, 'rb') as f:
            input_bytes = f.read()

        # Remove background using rembg
        output_bytes = remove(input_bytes)

        # rembg remove returns bytes of a PNG, so we must load it via BytesIO
        import io
        img = Image.open(io.BytesIO(output_bytes)).convert("RGBA")

        # Enhance foreground (the person)
        img = ImageEnhance.Contrast(img).enhance(1.05)
        img = ImageEnhance.Color(img).enhance(1.1)
        img = ImageEnhance.Sharpness(img).enhance(1.2)

        # Crop to aspect ratio (center crop)
        target_aspect = TARGET_SIZE[0] / TARGET_SIZE[1]
        img_aspect = img.width / img.height

        if img_aspect > target_aspect:
            new_width = int(target_aspect * img.height)
            left = (img.width - new_width) // 2
            img = img.crop((left, 0, left + new_width, img.height))
        elif img_aspect < target_aspect:
            new_height = int(img.width / target_aspect)
            top = (img.height - new_height) // 2
            img = img.crop((0, top, img.width, top + new_height))

        # Resize to fit the background
        img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)

        # Composite over gradient background
        final_img = bg_image.copy()
        final_img.paste(img, (0, 0), img)

        # Save as WebP
        final_img.save(target_path, 'WEBP', quality=90)
        print(
            f"Professional corporate portrait created: {name} -> {target_path}")  # noqa: E501

    except Exception as e:
        print(f"Error processing {filepath}: {e}")


for filepath in image_files:
    process_image(filepath)

print("Corporate Team image processing complete.")
