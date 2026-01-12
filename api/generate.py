import random

SIZE = 40
ROWS = 10
COLS = 10

def color():
    return f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"

rects = ""
for y in range(ROWS):
    for x in range(COLS):
        rects += f'''
        <rect x="{x*SIZE}" y="{y*SIZE}"
              width="{SIZE}" height="{SIZE}"
              fill="{color()}" />
        '''

html = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>敷き詰めアート</title>
</head>
<body>
<svg width="{SIZE*COLS}" height="{SIZE*ROWS}">
{rects}
</svg>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html を生成しました")

