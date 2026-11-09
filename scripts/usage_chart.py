import cairosvg
import os

days = [
    ("Nov 03", 2.538, 14.059),
    ("Nov 04", 2.135, 21.674),
    ("Nov 05", 0.004, 0.728),
    ("Nov 06", 0.0, 0.0),
    ("Nov 07", 0.007, 11.364),
    ("Nov 08", 0.131, 10.455),
    ("Nov 09", 0.103, 8.744),
]

W, H = 1000, 580
margin_l, margin_r, margin_t, margin_b = 70, 40, 80, 90
plot_w = W - margin_l - margin_r
plot_h = H - margin_t - margin_b
maxv = 24.0

def px(v):
    return plot_h * (v / maxv)

FLASH = "#f59e0b"
V4PRO = "#4f46e5"
GRID  = "#e5e7eb"
TEXT  = "#1f2937"
MUTED = "#6b7280"

n = len(days)
slot = plot_w / n
bar_w = slot * 0.58
parts = []

for i, (label, f, v) in enumerate(days):
    x = margin_l + slot * i + (slot - bar_w) / 2
    base_y = margin_t + plot_h
    fh = px(f)
    fy = base_y - fh
    parts.append(f'<rect x="{x:.1f}" y="{fy:.1f}" width="{bar_w:.1f}" height="{fh:.1f}" fill="{FLASH}" rx="2"/>')
    vh = px(v)
    vy = fy - vh
    parts.append(f'<rect x="{x:.1f}" y="{vy:.1f}" width="{bar_w:.1f}" height="{vh:.1f}" fill="{V4PRO}" rx="2"/>')
    cx = margin_l + slot * i + slot / 2
    if v + f == 0:
        parts.append(f'<text x="{cx:.1f}" y="{H - margin_b + 28:.1f}" text-anchor="middle" font-family="Helvetica,Arial" font-size="12" fill="{MUTED}">(gap)</text>')
    else:
        parts.append(f'<text x="{cx:.1f}" y="{H - margin_b + 28:.1f}" text-anchor="middle" font-family="Helvetica,Arial" font-size="15" fill="{TEXT}">{label}</text>')

for gv in [0, 6, 12, 18, 24]:
    gy = margin_t + plot_h - px(gv)
    parts.append(f'<line x1="{margin_l}" y1="{gy:.1f}" x2="{margin_l+plot_w}" y2="{gy:.1f}" stroke="{GRID}" stroke-width="1"/>')
    parts.append(f'<text x="{margin_l - 12:.1f}" y="{gy + 5:.1f}" text-anchor="end" font-family="Helvetica,Arial" font-size="13" fill="{MUTED}">$ {gv}</text>')

parts.append(f'<text x="{margin_l}" y="40" font-family="Helvetica,Arial" font-size="24" font-weight="bold" fill="{TEXT}">DeepSeek Spend — daily, Nov 3-9 2026</text>')
parts.append(f'<text x="{margin_l}" y="66" font-family="Helvetica,Arial" font-size="15" fill="{MUTED}">stacked: flash (amber) + v4-pro (indigo)  ·  total $71.94  ·  all-flash would be ~ $17</text>')

lx = margin_l + plot_w - 270
ly = margin_t + plot_h + 58
parts.append(f'<rect x="{lx}" y="{ly}" width="14" height="14" fill="{V4PRO}" rx="2"/>')
parts.append(f'<text x="{lx+20}" y="{ly+12}" font-family="Helvetica,Arial" font-size="14" fill="{TEXT}">v4-pro  $67.02</text>')
parts.append(f'<rect x="{lx+125}" y="{ly}" width="14" height="14" fill="{FLASH}" rx="2"/>')
parts.append(f'<text x="{lx+145}" y="{ly+12}" font-family="Helvetica,Arial" font-size="14" fill="{TEXT}">flash  $4.92</text>')

svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="' + str(W) + '" height="' + str(H) + '" '
       'viewBox="0 0 ' + str(W) + ' ' + str(H) + '">'
       '<rect width="100%" height="100%" fill="#ffffff"/>' + "".join(parts) + '</svg>')

svg_path = "/tmp/usage_chart.svg"
png_path = "/home/dev/.openclaw/workspace/exports/usage-chart.png"
open(svg_path, "w").write(svg)
cairosvg.svg2png(url=svg_path, write_to=png_path, scale=2)
print("wrote", png_path)
