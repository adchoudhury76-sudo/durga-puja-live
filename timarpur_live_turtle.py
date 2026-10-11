import turtle
import math
import time

# ---------- Setup Screen ----------
screen = turtle.Screen()
screen.setup(1600, 1200)
screen.bgcolor("black")
screen.title("Timarpur Civil Lines Puja Samity - Live Drawing")
screen.tracer(0)

# Main drawing turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Text turtle
text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.speed(0)

# ---------- Colors ----------
GOLD = "#d6af55"
GOLD_DARK = "#b58932"
RED = "#c41217"
RED_DEEP = "#9a0c12"
GREEN = "#125e4a"
GREEN_DARK = "#0a443a"
CREAM = "#ecd aab"
WHITE = "white"
BLACK = "black"

# ---------- Helper Functions ----------
def draw_circle(x, y, radius, color, fill=True, outline="", outline_width=0):
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.color(outline if outline else color)
    if fill:
        pen.fillcolor(color)
        pen.begin_fill()
    pen.pendown()
    pen.circle(radius)
    if fill:
        pen.end_fill()
    pen.penup()

def draw_filled_polygon(points, color, outline_color="", outline_width=0):
    pen.penup()
    pen.goto(points[0][0], points[0][1])
    pen.color(outline_color if outline_color else color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.pendown()
    for point in points[1:]:
        pen.goto(point[0], point[1])
    pen.goto(points[0][0], points[0][1])
    pen.end_fill()
    pen.penup()

def draw_line(x1, y1, x2, y2, color, width=2):
    pen.penup()
    pen.goto(x1, y1)
    pen.color(color)
    pen.width(width)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

def draw_arc_live(cx, cy, radius, start_angle, extent, color, width=4):
    pen.penup()
    pen.goto(cx, cy - radius)
    pen.setheading(90)
    pen.color(color)
    pen.width(width)
    pen.pendown()
    pen.setheading(start_angle)
    pen.circle(radius, extent)
    pen.penup()

def draw_star(cx, cy, outer_r, inner_r, points, color):
    coords = []
    for i in range(points * 2):
        angle = (i * 180 / points) - 90
        if i % 2 == 0:
            r = outer_r
        else:
            r = inner_r
        rad = math.radians(angle)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        coords.append((x, y))
    draw_filled_polygon(coords, color, GOLD_DARK, 2)

def draw_text(message, x, y, font_size, color, align="center"):
    text_pen.penup()
    text_pen.goto(x, y)
    text_pen.color(color)
    text_pen.write(message, align=align, font=("Arial", font_size, "bold"))

def draw_rectangle(x, y, width, height, color, outline_color="", outline_width=2):
    pen.penup()
    pen.goto(x - width/2, y - height/2)
    pen.color(outline_color if outline_color else color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.pendown()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()
    pen.penup()

# ---------- Live Drawing Functions ----------

def draw_rays_live(center_x, center_y, frame):
    """Draw animated golden rays"""
    print(f"Drawing rays... Frame {frame}")
    for ang in range(0, 360, 6):
        rad = math.radians(ang + frame % 360)
        x1 = center_x + 250 * math.cos(rad)
        y1 = center_y + 250 * math.sin(rad)
        x2 = center_x + 430 * math.cos(rad)
        y2 = center_y + 430 * math.sin(rad)
        draw_line(x1, y1, x2, y2, GOLD, width=3)

def draw_main_circle_live(center_x, center_y):
    """Draw the main red circle emblem"""
    print("Drawing main red circle...")
    # Outer gold ring
    draw_circle(center_x, center_y, 310, GOLD, fill=False, outline=GOLD_DARK, outline_width=10)
    # Red main circle
    draw_circle(center_x, center_y, 260, RED, outline=GOLD_DARK, outline_width=8)

def draw_crown_live(center_x, center_y):
    """Draw the crown decoration"""
    print("Drawing crown...")
    # Crown rays
    for i in range(12):
        ang = math.radians(i * 30)
        x1 = center_x + 150 * math.cos(ang)
        y1 = center_y - 150 * math.sin(ang) + 5
        x2 = center_x + 190 * math.cos(ang)
        y2 = center_y - 190 * math.sin(ang) + 5
        draw_line(x1, y1, x2, y2, GOLD, width=4)
    
    # Crown arcs
    for px, py in [(center_x - 130, center_y - 70), (center_x, center_y - 90), (center_x + 130, center_y - 70)]:
        draw_arc_live(px, py + 30, 60, 200, 140, GOLD, width=4)

def draw_face_live(center_x, center_y):
    """Draw the goddess face"""
    print("Drawing face...")
    # Face base
    draw_circle(center_x, center_y, 140, GOLD, outline=GOLD_DARK, outline_width=4)
    
    # Bindi (forehead mark)
    draw_circle(center_x, center_y - 40, 18, RED, outline=GOLD_DARK, outline_width=2)
    
    # Eyes
    for dx in (-70, 70):
        # Eye white
        draw_circle(center_x + dx, center_y - 10, 22, WHITE, outline=GOLD_DARK, outline_width=2)
        # Pupil
        draw_circle(center_x + dx, center_y - 10, 7, BLACK)
        # Eye reflection
        draw_circle(center_x + dx + 3, center_y - 7, 3, WHITE)
    
    # Nose
    draw_line(center_x, center_y + 10, center_x, center_y + 60, GOLD_DARK, width=3)
    
    # Nostrils
    draw_circle(center_x - 8, center_y + 40, 3, GOLD_DARK)
    draw_circle(center_x + 8, center_y + 40, 3, GOLD_DARK)
    
    # Mouth (arc)
    draw_arc_live(center_x, center_y + 50, 35, 220, 100, GOLD_DARK, width=3)
    
    # Side ornaments (earrings)
    for dx in (-140, 140):
        draw_circle(center_x + dx, center_y, 35, GOLD, outline=GOLD_DARK, outline_width=3)
        # Small flowers in ornament
        for j in range(8):
            ang = math.radians(j * 45)
            x = center_x + dx + 14 * math.cos(ang)
            y = center_y + 14 * math.sin(ang)
            draw_circle(x, y, 5, RED_DEEP)

def draw_bottom_platform_live(center_x, base_y):
    """Draw the cream bottom platform"""
    print("Drawing bottom platform...")
    # Main cream arch
    pen.penup()
    pen.goto(center_x - 500, base_y)
    pen.color(GOLD_DARK)
    pen.fillcolor(CREAM)
    pen.begin_fill()
    pen.pendown()
    pen.goto(center_x + 500, base_y)
    pen.goto(center_x + 520, base_y + 200)
    pen.goto(center_x - 520, base_y + 200)
    pen.end_fill()
    pen.penup()
    
    # Decorative stars
    for i in range(9):
        x = center_x - 450 + i * 110
        y = base_y + 90
        draw_star(x, y, 18, 10, 5, RED)

def draw_green_panel_live(center_x, panel_y):
    """Draw the green number panel"""
    print("Drawing green panel...")
    # Panel background
    pen.penup()
    pen.goto(center_x - 300, panel_y - 140)
    pen.color(GOLD_DARK)
    pen.fillcolor(GREEN)
    pen.begin_fill()
    pen.pendown()
    pen.goto(center_x + 300, panel_y - 140)
    pen.goto(center_x + 300, panel_y + 140)
    pen.goto(center_x - 300, panel_y + 140)
    pen.goto(center_x - 300, panel_y - 140)
    pen.end_fill()
    pen.penup()

def draw_numbers_live(center_x, panel_y):
    """Draw 113 and text"""
    print("Drawing numbers and text...")
    # Draw 113
    draw_text("113", center_x, panel_y, 200, GOLD)
    
    # Text below
    draw_text("Years of Pride & Celebration", center_x, panel_y - 100, 36, GREEN_DARK)
    draw_text("1914-2026", center_x, panel_y - 150, 36, GREEN_DARK)

def draw_side_text_live(center_x, width):
    """Draw side text"""
    print("Drawing side text...")
    texts = ["TIMARPUR", "&", "CIVIL LINES", "PUJA", "SAMITY"]
    start_x = 100
    end_x = width - 100
    
    for i, txt in enumerate(texts):
        y = 600 + i * 30
        draw_text(txt, start_x, y, 32, GOLD_DARK)
        draw_text(txt, end_x, y, 32, GOLD_DARK)

def draw_title_live(center_x, top_y):
    """Draw title"""
    print("Drawing title...")
    draw_text("Maa Durga", center_x, top_y, 48, GOLD)
    draw_text("শুভ দুর্গা পুজা", center_x, top_y - 50, 44, GOLD)

# ---------- MAIN LIVE DRAWING ANIMATION ----------
def draw_complete_logo_live(frame=0):
    """Complete live drawing sequence"""
    print(f"\n===== FRAME {frame} =====")
    pen.clear()
    text_pen.clear()
    
    # Coordinates
    center_x, center_y = 0, 100
    base_y = -220
    panel_y = -400
    
    # Draw in sequence with live visualization
    draw_rays_live(center_x, center_y, frame)
    time.sleep(0.1)
    screen.update()
    
    draw_main_circle_live(center_x, center_y)
    time.sleep(0.1)
    screen.update()
    
    draw_crown_live(center_x, center_y)
    time.sleep(0.1)
    screen.update()
    
    draw_face_live(center_x, center_y)
    time.sleep(0.1)
    screen.update()
    
    draw_bottom_platform_live(center_x, base_y)
    time.sleep(0.1)
    screen.update()
    
    draw_green_panel_live(center_x, panel_y)
    time.sleep(0.1)
    screen.update()
    
    draw_numbers_live(center_x, panel_y)
    time.sleep(0.1)
    screen.update()
    
    draw_side_text_live(center_x, 1600)
    time.sleep(0.1)
    screen.update()
    
    draw_title_live(center_x, 300)
    time.sleep(0.1)
    screen.update()

# ---------- ANIMATION LOOP ----------
frame = 0
try:
    while True:
        draw_complete_logo_live(frame)
        frame += 1
        time.sleep(2)  # Redraw every 2 seconds with slight animation
except KeyboardInterrupt:
    print("\nDrawing stopped by user")
    screen.bye()
