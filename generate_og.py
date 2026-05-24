from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
BG = (8, 8, 8)
ACCENT = (255, 107, 26)
WHITE = (255, 255, 255)
MUTED = (144, 144, 144)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

PADDING = 80

def load_font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/SFNS.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

font_label = load_font(18)
font_name  = load_font(72, bold=True)
font_title = load_font(36)
font_url   = load_font(22)

# dot + label
dot_x, dot_y = PADDING, PADDING
draw.ellipse([dot_x, dot_y + 6, dot_x + 10, dot_y + 16], fill=ACCENT)
draw.text((dot_x + 20, dot_y), "CONTENT OPERATIONS · AI-ASSISTED", font=font_label, fill=ACCENT)

# name
draw.text((PADDING, H // 2 - 90), "Marco Doria", font=font_name, fill=WHITE)

# headline
draw.text((PADDING, H // 2 + 10), "AI-Assisted Content Operations", font=font_title, fill=(212, 212, 212))

# accent line
line_y = H // 2 + 68
draw.rectangle([PADDING, line_y, PADDING + 260, line_y + 2], fill=ACCENT)

# URL
draw.text((PADDING, H - PADDING - 28), "marcodoria.consulting", font=font_url, fill=MUTED)

out = os.path.join(os.path.dirname(__file__), "og-image.png")
img.save(out, "PNG", optimize=True)
print(f"Saved: {out}")
