import os
import re

files = [
    ('dist/github-contribution-grid-snake-dark.svg', '#191d17', '#e1e4da', '#285020'),
    ('dist/github-contribution-grid-snake.svg', '#f4fbf4', '#191c19', '#dce5dc')
]

for path, bg, text_color, badge_bg in files:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Вырезаем только тело SVG
        inner = re.sub(r'^<svg[^>]*>', '', content, flags=re.IGNORECASE)
        inner = re.sub(r'</svg>\s*$', '', inner, flags=re.IGNORECASE)

        # Вырезаем фоновые прямоугольники и контуры, которые генерирует Platane/snk
        inner = re.sub(r'<rect[^>]*fill="var\(--bg\)"[^>]*/>', '', inner)
        inner = re.sub(r'<rect[^>]*class="border"[^>]*/>', '', inner)

        # Переопределяем CSS переменные самого snk, чтобы внутри не рисовался паразитный фон
        inner = re.sub(r'--bg:[^;]+;', f'--bg:{bg};', inner)

        new_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 214" width="840" height="214">
  <!-- Чистый фон без всяких stroke и рамок -->
  <rect width="840" height="214" rx="32" fill="{bg}"/>

  <!-- Шапка -->
  <g transform="translate(32, 24)">
    <circle cx="16" cy="16" r="16" fill="{badge_bg}"/>
    <text x="16" y="22" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="16" text-anchor="middle">🐍</text>
    <text x="44" y="23" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="20" font-weight="600" fill="{text_color}">Contribution Timeline</text>
  </g>

  <!-- Сетка змейки без паразитных рамок -->
  <g transform="translate(10, 48)">
    {inner}
  </g>
</svg>'''

        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_svg)
