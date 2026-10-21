import os

files = [
    ('dist/github-contribution-grid-snake-dark.svg', '#101712', '#1d2c20'),
    ('dist/github-contribution-grid-snake.svg', '#f4fbf4', '#dce5dc')
]

for path, bg, border in files:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        start = content.find('>') + 1
        end = content.rfind('</svg>')
        inner = content[start:end] if (start > 0 and end > 0) else content

        card = (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 230" width="100%" height="100%">\n'
            f'  <rect x="2" y="2" width="876" height="226" rx="28" fill="{bg}" stroke="{border}" stroke-width="2"/>\n'
            '  <g transform="translate(32, 28)">\n'
            '    <circle cx="12" cy="12" r="14" fill="#1b3823"/>\n'
            '    <text x="12" y="17" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" text-anchor="middle">🐍</text>\n'
            '    <text x="36" y="17" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="17" font-weight="700" fill="#f0fdf4">Contribution Timeline</text>\n'
            '  </g>\n'
            '  <g transform="translate(20, 52)">\n'
            + inner +
            '  </g>\n'
            '</svg>'
        )

        with open(path, 'w', encoding='utf-8') as f:
            f.write(card)
