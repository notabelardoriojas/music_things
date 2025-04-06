from PIL import Image, ImageDraw, ImageFont
import os

# Grid and canvas settings
grid_cols = 6
grid_rows = 5
cell_size = 200
padding = 20
label_height = 40
font_size = 15
canvas_width = grid_cols * (cell_size + padding) + padding
canvas_height = grid_rows * (cell_size + label_height + padding) + padding

# Ordered categories
categories = [
    "Favourite Album", "Best Narrative", "Favourite Cover", "I'll Listen Someday", "Personal Impact", "Bad Day Cure",
    "You enjoy but most don't", "You don't enjoy but most do", "Underrated", "Overrated", "Not usually my thing but..", "Best Instrumental",
    "Best Vocals", "Simple but fun", "Best Mixtape", "Consistent Discography", "Biggest Letdown", "Biggest Surprise",
    "Best Soundtrack", "Most Unique", "Favourite Band", "Favourite Solo Artist", "Best EP", "Most Depressing"
]

# Collect user input
album_images = {}
print("Paste image file paths for each category (or leave blank to skip):\n")

for cat in categories:
    path = input(f"{cat}: ").strip()
    if path and os.path.exists(path):
        album_images[cat] = path
    elif path:
        print("  [!] File not found, skipping.")

# Create canvas
canvas = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(canvas)

# Load font

font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf", font_size)
# except:
#     font = ImageFont.load_default()

# Paste covers and write text
for idx, category in enumerate(categories):
    row = idx // grid_cols
    col = idx % grid_cols
    x = padding + col * (cell_size + padding)
    y = padding + row * (cell_size + label_height + padding)

    # Center text using textbbox for modern Pillow
    bbox = draw.textbbox((0, 0), category, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = x + (cell_size - text_width) // 2
    text_y = y + (label_height - text_height) // 2
    draw.text((text_x, text_y), category, fill="black", font=font)

    if category in album_images:
        img = Image.open(album_images[category]).convert("RGB").resize((cell_size, cell_size))
        canvas.paste(img, (x, y + label_height))

# Save output
output_path = "/Users/abelardoriojas/Desktop/result.jpg"
canvas.save(output_path)

print(f"\nDone! Saved to {output_path}")