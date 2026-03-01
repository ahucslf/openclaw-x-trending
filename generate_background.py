#!/usr/bin/env python3
"""
Generate a dark elegant website background for OpenCLAW
"""
from PIL import Image, ImageDraw, ImageFont
import math
import random

# Set random seed for reproducibility
random.seed(42)

# Canvas size (horizontal banner)
width, height = 1920, 600

# Colors
bg_color = (10, 10, 10)  # #0a0a0a
accent_color = (255, 107, 53)  # #ff6b35
accent_color_light = (255, 159, 67)  # #ff9f43
white = (255, 255, 255)

# Create image
img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)

# Draw radial gradients (simulated with circles)
for i in range(8):
    x = random.randint(0, width)
    y = random.randint(0, height)
    radius = random.randint(200, 600)

    # Create gradient effect with multiple circles
    for r in range(radius, 0, -20):
        alpha = int(255 * (r / radius) * 0.15)
        color = (*accent_color[:2], alpha) if len(accent_color) == 3 else (accent_color[0], accent_color[1], accent_color[2], alpha)

        # Draw arc for gradient effect
        draw.ellipse([x-r, y-r, x+r, y+r], outline=color[:3])

# Draw floating particles/nodes
particles = []
for _ in range(50):
    particles.append({
        'x': random.randint(0, width),
        'y': random.randint(0, height),
        'size': random.randint(1, 4),
        'alpha': random.randint(50, 200)
    })

for p in particles:
    draw.ellipse([p['x']-p['size'], p['y']-p['size'],
                 p['x']+p['size'], p['y']+p['size']],
                 fill=(*accent_color_light, p['alpha']))

# Draw network lines
for _ in range(20):
    x1, y1 = random.randint(0, width), random.randint(0, height)
    x2, y2 = random.randint(0, width), random.randint(0, height)
    alpha = random.randint(20, 80)
    draw.line([x1, y1, x2, y2], fill=(*accent_color_light, alpha), width=1)

# Draw lobster silhouette (stylized)
# Center position
cx, cy = width // 2, height // 2

# Simple lobster shape using ellipses and lines
lobster_color = (*accent_color, 180)

# Body (main ellipse)
draw.ellipse([cx-80, cy-30, cx+80, cy+30], fill=(*accent_color, 200))

# Head
draw.ellipse([cx-60, cy-60, cx+40, cy-10], fill=(*accent_color, 200))

# Eyes
draw.ellipse([cx-45, cy-55, cx-35, cy-45], fill=(255, 255, 255, 230))
draw.ellipse([cx-15, cy-55, cx-5, cy-45], fill=(255, 255, 255, 230))
draw.ellipse([cx-42, cy-52, cx-38, cy-48], fill=(0, 0, 0))
draw.ellipse([cx-12, cy-52, cx-8, cy-48], fill=(0, 0, 0))

# Antennae
draw.line([cx-30, cy-60, cx-60, cy-100], fill=(*accent_color, 150), width=2)
draw.line([cx-30, cy-60, cx, cy-95], fill=(*accent_color, 150), width=2)

# Claws (simplified)
draw.ellipse([cx-100, cy-20, cx-70, cy+20], fill=(*accent_color, 180))
draw.ellipse([cx-110, cy-40, cx-60, cy], fill=(*accent_color, 180))

draw.ellipse([cx+70, cy-20, cx+100, cy+20], fill=(*accent_color, 180))
draw.ellipse([cx+60, cy-40, cx+110, cy], fill=(*accent_color, 180))

# Tail segments
for i in range(5):
    x_offset = 70 + i * 25
    draw.ellipse([cx+x_offset, cy-15, cx+x_offset+20, cy+15], fill=(*accent_color, 180 - i*20))

# Glow effect behind lobster
for i in range(5):
    glow_radius = 150 + i * 30
    alpha = 30 - i * 5
    draw.ellipse([cx-glow_radius, cy-glow_radius, cx+glow_radius, cy+glow_radius],
                 outline=(*accent_color, alpha))

# Add "OpenCLAW" text
try:
    # Try to load a bold font
    font_large = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 120)
    font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
except:
    font_large = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Draw text shadow
shadow_color = (0, 0, 0)
text = "OpenCLAW"
bbox = draw.textbbox((0, 0), text, font=font_large)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Position text
tx = width // 2 - text_width // 2
ty = height // 2 + 80

# Draw shadow
draw.text((tx+3, ty+3), text, font=font_large, fill=shadow_color)

# Draw main text
# For gradient effect, draw multiple times with slight color variations
for i in range(5):
    offset = i * 0.5
    color = tuple(min(255, int(white[j] * (1 - i/5) + accent_color[j] * (i/5))) for j in range(3))
    draw.text((tx - offset, ty - offset), text, font=font_large, fill=color)

draw.text((tx, ty), text, font=font_large, fill=white)

# Add subtitle
subtitle = "X.COM TRENDING"
sub_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
sub_width = sub_bbox[2] - sub_bbox[0]
draw.text((width//2 - sub_width//2, ty + 140), subtitle, font=font_small, fill=(102, 102, 102))

# Save
img.save('/Users/fei/openclaw-posts/background.png', 'PNG', quality=95)
print("Background saved to /Users/fei/openclaw-posts/background.png")
