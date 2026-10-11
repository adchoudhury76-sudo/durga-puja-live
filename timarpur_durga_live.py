from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1500, 1200
img = Image.new("RGB", (W, H), "black")
d = ImageDraw.Draw(img)

# ---------- Colors ----------
GOLD = (214, 175, 85)
GOLD_DARK = (181, 137, 50)
RED = (196, 18, 27)
RED_DEEP = (154, 12, 18)
GREEN = (18, 94, 74)
GREEN_DARK = (10, 68, 58)
CREAM = (236, 218, 171)
BEIGE = (221, 193, 120)

# ---------- Helper ----------
def draw_circle(x, y, r, fill, outline=None, outline_w=2):
    d.ellipse((x-r, y-r, x+r, y+r), fill=fill, outline=outline, width=outline_w)

def draw_line(x1, y1, x2, y2, color, width=2):
    d.line((x1, y1, x2, y2), fill=color, width=width)

def draw_arc(cx, cy, r, start, end, color, width=4):
    d.arc((cx-r, cy-r, cx+r, cy+r), start=start, end=end, fill=color, width=width)

def text_center(txt, x, y, size, color, font_name="DejaVuSans-Bold.ttf", anchor="mm"):
    try:
        font = ImageFont.truetype(font_name, size)
    except Exception:
        font = ImageFont.load_default()
    d.text((x, y), txt, font=font, fill=color, anchor=anchor)

def star_points(cx, cy, outer, inner, n=5):
    pts = []
    for i in range(2*n):
        angle = -math.pi/2 + i*math.pi/n
        r = outer if i % 2 == 0 else inner
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        pts.append((x, y))
    return pts

# ---------- Background gold panel ----------
# Main platform / arch
main_plate = (250, 600, 1250, 820)
d.rounded_rectangle(main_plate, radius=50, fill=CREAM, outline=GOLD_DARK, width=8)

# Gold arch top behind circle
arch_top = (250, 150, 1250, 640)
d.rounded_rectangle(arch_top, radius=50, fill=CREAM, outline=GOLD_DARK, width=8)

# ---------- Rays behind circle ----------
center = (750, 385)
for ang in range(0, 360, 4):
    rad = math.radians(ang)
    x1 = center[0] + 250 * math.cos(rad)
    y1 = center[1] + 250 * math.sin(rad)
    x2 = center[0] + 430 * math.cos(rad)
    y2 = center[1] + 430 * math.sin(rad)
    draw_line(x1, y1, x2, y2, GOLD, width=3)

# Main red circle / emblem disc
circle_r = 260
# golden outer ring
draw_circle(center[0], center[1], circle_r + 36, fill=GOLD, outline=GOLD_DARK, outline_w=8)
draw_circle(center[0], center[1], circle_r, fill=RED, outline=GOLD, outline_w=8)

# Thin inner gold ring
# Draw stylized face
# crown / halo
for i in range(12):
    ang = math.radians(i * 30)
    x1 = center[0] + 150 * math.cos(ang)
    y1 = center[1] - 150 * math.sin(ang) + 5
    x2 = center[0] + 190 * math.cos(ang)
    y2 = center[1] - 190 * math.sin(ang) + 5
    draw_line(x1, y1, x2, y2, GOLD, width=4)

# central crown top
crown = [(center[0]-150, center[1]-70), (center[0]-110, center[1]-20), (center[0]-70, center[1]-50),
         (center[0]-30, center[1]-10), (center[0], center[1]-70), (center[0]+30, center[1]-10),
         (center[0]+70, center[1]-50), (center[0]+110, center[1]-20), (center[0]+150, center[1]-70)]
# Stylized crown arcs
for px, py in [(center[0]-130, center[1]-70), (center[0], center[1]-90), (center[0]+130, center[1]-70)]:
    draw_arc(px, py+30, 60, 200, 340, GOLD, width=4)

# Face shape / ornate mask
# forehead and hair outline
# use circular head
head = (center[0]-140, center[1]-150, center[0]+140, center[1]+120)
d.ellipse(head, fill=GOLD, outline=GOLD_DARK, width=4)

# face area mask in lighter gold
face = (center[0]-120, center[1]-110, center[0]+120, center[1]+80)
d.ellipse(face, fill=GOLD, outline=GOLD_DARK, width=3)

# center medallion / forehead bindi
draw_circle(center[0], center[1]-40, 18, GOLD_DARK)

# Left and right eye almond shapes
for dx in (-70, 70):
    d.polygon([(center[0]+dx-32, center[1]-10), (center[0]+dx+32, center[1]-10),
               (center[0]+dx+18, center[1]+32), (center[0]+dx-18, center[1]+32)], fill=GOLD_DARK)
    # white eye
    d.ellipse((center[0]+dx-22, center[1]-6, center[0]+dx+22, center[1]+26), fill=(245, 245, 245), outline=GOLD_DARK, width=2)
    # pupil
    draw_circle(center[0]+dx, center[1]+8, 7, "black")

# nose and lips
draw_line(center[0], center[1]+18, center[0], center[1]+68, GOLD_DARK, width=3)
# mouth arc
d.arc((center[0]-38, center[1]+52, center[0]+38, center[1]+96), start=210, end=330, fill=GOLD_DARK, width=4)

# side ornaments
for dx in (-130, 130):
    draw_circle(center[0]+dx, center[1]-5, 34, GOLD, outline=GOLD_DARK, outline_w=3)
    # small flowers in ornaments
    for j in range(8):
        ang = math.radians(j*45)
        x = center[0] + dx + 13*math.cos(ang)
        y = center[1] - 5 + 13*math.sin(ang)
        d.ellipse((x-5, y-5, x+5, y+5), fill=RED_DEEP)

# floral border around face
for gx in range(-140, 141, 70):
    for gy in range(-120, 121, 80):
        if abs(gx) < 110 and abs(gy) < 80:
            continue
        draw_circle(center[0]+gx, center[1]+gy, 20, GOLD, outline=GOLD_DARK, outline_w=3)
        for j in range(8):
            ang = math.radians(j*45)
            x = center[0]+gx + 26*math.cos(ang)
            y = center[1]+gy + 26*math.sin(ang)
            d.ellipse((x-4, y-4, x+4, y+4), fill=RED_DEEP)

# Create decorative stars above bottom platform
for i in range(9):
    x = 250 + i * 110
    y = 695
    pts = star_points(x, y, 18, 10, 5)
    d.polygon(pts, fill=RED, outline=GOLD)

# ---------- Big 113 and texts ----------
# Main number 113 at bottom center
try:
    large_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 230)
except Exception:
    large_font = ImageFont.load_default()

# create a green plate behind the number, like the logo
n_plate = (390, 585, 1110, 930)
d.rounded_rectangle(n_plate, radius=40, fill=CREAM, outline=GOLD_DARK, width=8)
# green number area
n_area = (430, 610, 1070, 880)
d.rounded_rectangle(n_area, radius=35, fill=GOLD, outline=GOLD_DARK, width=8)
d.rounded_rectangle((465, 640, 1035, 845), radius=22, fill=GREEN, outline=GREEN_DARK, width=4)

d.text((750, 750), "113", font=large_font, fill=GOLD, anchor="mm")

# Text under 113
try:
    mid_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 58)
except Exception:
    mid_font = ImageFont.load_default()

d.text((750, 880), "Years of Pride & Celebration", font=mid_font, fill=GREEN_DARK, anchor="mm")
d.text((750, 950), "1914-2026", font=mid_font, fill=GREEN_DARK, anchor="mm")

# Bottom slogan, rotated vertically like the reference image
try:
    vfont = ImageFont.truetype("DejaVuSans-Bold.ttf", 44)
except Exception:
    vfont = ImageFont.load_default()
# Draw vertical text by creating a temporary image
# (This gives the same style as the reference without needing a custom rotated font)
for i, txt in enumerate(["TIMARPUR", "&", "CIVIL LINES", "PUJA", "SAMITY"]):
    y = 1030 + i * 28
    d.text((150, y), txt, font=vfont, fill=GOLD_DARK)
    d.text((1330, y), txt, font=vfont, fill=GOLD_DARK)

# Add a subtle gold title at upper center
try:
    top_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 38)
except Exception:
    top_font = ImageFont.load_default()
d.text((750, 120), "Maa Durga", font=top_font, fill=GOLD, anchor="mm")

# Add some extra radial dots around outer circle for ornamental finish
for ang in range(0, 360, 10):
    rad = math.radians(ang)
    x = center[0] + 390 * math.cos(rad)
    y = center[1] + 390 * math.sin(rad)
    d.ellipse((x-4, y-4, x+4, y+4), fill=GOLD)

# Save output
img.save("timarpur_civil_lines_logo.png")
print("Saved: timarpur_civil_lines_logo.png")
