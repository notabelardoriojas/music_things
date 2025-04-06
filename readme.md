# 🎵 music_thing.py

`music_thing.py` is a Python script that helps you generate a personalized **Topster** (a grid-style collage of album covers) based on themed music categories. Just provide image file paths for each category, and the script will create a beautifully organized poster featuring your selections.

---

## 🖼️ What It Does

- Prompts you to input album cover image paths for 24 custom categories.
- Automatically resizes and arranges them into a labeled 6x5 grid.
- Adds each category title above the album art.
- Saves the finished collage as a `.jpg` file.

---

## 📦 Requirements

- Python 3
- [Pillow](https://python-pillow.org/) (Python Imaging Library fork)

Install Pillow with:

```bash
pip install Pillow
```

---

## 🚀 How to Use

1. **Run the script** in your terminal:
   ```bash
   python music_thing.py
   ```

2. **Provide image paths** (absolute or relative) for each prompted category. You can skip any by leaving it blank.

3. The script will:
   - Arrange your albums in a 6x5 grid.
   - Add titles like "Favourite Album", "Best Vocals", "Overrated", etc.
   - Save the result to your Desktop as `result.jpg`.

---

## 🧠 Category List

Here are the 24 music-related categories the script uses:

- Favourite Album
- Best Narrative
- Favourite Cover
- I'll Listen Someday
- Personal Impact
- Bad Day Cure
- You enjoy but most don't
- You don't enjoy but most do
- Underrated
- Overrated
- Not usually my thing but..
- Best Instrumental
- Best Vocals
- Simple but fun
- Best Mixtape
- Consistent Discography
- Biggest Letdown
- Biggest Surprise
- Best Soundtrack
- Most Unique
- Favourite Band
- Favourite Solo Artist
- Best EP
- Most Depressing

---

## ✏️ Customization Tips

- **Font**: The script uses `Arial Bold Italic.ttf` by default (macOS path). You can change the font path to any `.ttf` file on your system.
- **Output location**: Modify the `output_path` variable to save your collage elsewhere.
- **Grid size**: Tweak `grid_cols`, `grid_rows`, and `cell_size` at the top of the script to customize layout.

---

## 💡 Example Use Case

Want to post your music taste online, curate a themed collection, or just visualize your listening history? This is a perfect way to flex your favorite records with an aesthetic grid.

---

## 🧃 Author

Made by Abelardo R. — indie/emo enjoyer and lifelong /mu/ head.

---

Let me know if you want a version that works with drag-and-drop or automatic album art fetching!
