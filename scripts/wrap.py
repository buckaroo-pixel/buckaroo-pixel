import os
import re

files = [
    ('dist/github-contribution-grid-snake-dark.svg', '#101712', '#1d2c20', '#f0fdf4'),
    ('dist/github-contribution-grid-snake.svg', '#f4fbf4', '#dce5dc', '#191c19')
]

for path, bg, border, text_color in files:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Извлекаем внутренности SVG (стили, анимацию, элементы сетки)
        inner = re.sub(r'^<svg[^>]*>', '', content, flags=re.IGNORECASE)
        inner = re.sub(r'</svg>\s*$', '', inner, flags=re.IGNORECASE)

        # Собираем чистый SVG с фиксированной рамкой и правильным смещением
        new_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 890 235" width="100%" height="100%">
  <!-- Скругленная подложка карточки Material You -->
  <rect x="2" y="2" width="886" height="231" rx="28" fill="{bg}" stroke="{border}" stroke-width="2"/>

  <!-- Заголовок секции -->
  <g transform="translate(32, 28)">
    <circle cx="12" cy="12" r="14" fill="#1b3823"/>
    <text x="12" y="17" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" text-anchor="middle">🐍</text>
    <text x="36" y="17" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="17" font-weight="700" fill="{text_color}">Contribution Timeline</text>
  </g>

  <!-- Сетка змейки со смещением внутрь карточки -->
  <g transform="translate(18, 55)">
    {inner}
  </g>
</svg>'''

        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_svg)
