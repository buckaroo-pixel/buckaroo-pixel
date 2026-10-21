import os
import re

files = [
    ('dist/github-contribution-grid-snake-dark.svg', '#191d17'),
    ('dist/github-contribution-grid-snake.svg', '#f4fbf4')
]

for path, bg in files:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        inner = re.sub(r'^<svg[^>]*>', '', content, flags=re.IGNORECASE)
        inner = re.sub(r'</svg>\s*$', '', inner, flags=re.IGNORECASE)
        inner = re.sub(r'<rect[^>]*width="100%"[^>]*height="100%"[^>]*/>', '', inner, count=1)
        inner = re.sub(r'<rect[^>]*class="border"[^>]*/>', '', inner)

        # Расширяем холст до 870px с запасом по краям, чтобы скругления rx=32 не срезали ячейки
        new_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 870 180" width="870" height="180">
  <rect width="870" height="180" rx="32" fill="{bg}"/>
  <g transform="translate(22, 22)">
    {inner}
  </g>
</svg>'''

        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_svg)
