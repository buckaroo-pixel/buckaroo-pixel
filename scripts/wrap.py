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

        # viewBox 870 190 дает место снизу под шкалу, x="16" центрирует влево, y="18" держит баланс
        new_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 870 190" width="870" height="190">
  <rect width="870" height="190" rx="32" fill="{bg}"/>
  <g transform="translate(16, 18)">
    {inner}
  </g>
</svg>'''

        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_svg)
