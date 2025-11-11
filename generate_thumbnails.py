"""
Thumbnail Generator for Pelican Articles

This script scans a source directory for image files (JPG/PNG), generates thumbnails 
with a fixed maximum size, and saves them in a designated output directory. 
It also creates a JSON file that keeps track of which slugs have corresponding thumbnails.

Requirements:
- Python 3.x
- Pillow library (`pip install pillow`)

Author: Ewelina Walkusz
"""

import os
import json
from PIL import Image

SRC_DIR = 'content/static/images'
DST_DIR = 'output/static/images/processed' # Dest dir for generated thumbnails
THUMB_SIZE = (300, 200)
JSON_FILE = 'content/thumbs.json' # JSON file to store thumbnail data

# Create destination directory if it doesn't exist
os.makedirs(DST_DIR, exist_ok=True)

# Dictionary to store which slugs have thumbnails
thumbs_data = {}

# Process all JPG and PNG files in the source directory
for filename in os.listdir(SRC_DIR):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        src_path = os.path.join(SRC_DIR, filename)

        slug = os.path.splitext(filename)[0].replace('_', '-')
        dst_name = f"{slug}-thumb.jpg"
        dst_path = os.path.join(DST_DIR, dst_name)

        # Open the source image and generate thumbnail
        with Image.open(src_path) as img:
            img.thumbnail(THUMB_SIZE, Image.Resampling.LANCZOS)
            img.convert('RGB').save(dst_path, 'JPEG', quality=85)

        thumbs_data[slug] = True
        print(f'Created thumbnail: {dst_path}')

# Save the thumbnail data to JSON
with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(thumbs_data, f, ensure_ascii=False, indent=2)

print('✅ All thumbnails generated!')
