"""Colourful section titles + animated divider. Run: python scripts/colorize.py"""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
MONO = "ui-monospace,SFMono-Regular,Consolas,Menlo,monospace"
TITLES = {  # file: (text, gradient start, gradient end)
    "whoami": ("whoami", "#39d353", "#22d3ee"),
    "toolbox": ("toolbox", "#22d3ee", "#3b82f6"),
    "skill-radar": ("skill radar", "#3b82f6", "#a855f7"),
    "contribution-calendar": ("contribution calendar", "#a855f7", "#ec4899"),
    "the-numbers": ("the numbers", "#ec4899", "#f97316"),
    "selected-work": ("selected work", "#f97316", "#eab308"),
}
for slug, (label, c1, c2) in TITLES.items():
    w = int(18 + 54 + 14 + len(label) * 16 + 18)
    open(f"{OUT}/title-{slug}.svg", "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 52" width="{w}" height="52" role="img"><title>{label}</title>
<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>
<rect x="9" y="6" width="54" height="40" rx="10" fill="#161b22" stroke="{c1}" stroke-opacity=".6"/>
<text x="36" y="34" text-anchor="middle" font-family="{MONO}" font-size="22" font-weight="700" fill="{c1}">~/</text>
<text x="80" y="36" font-family="{MONO}" font-size="26" font-weight="700" fill="url(#g)">{label}</text></svg>''')

stops = ["#39d353", "#22d3ee", "#60a5fa", "#a78bfa", "#f472b6", "#a78bfa", "#60a5fa", "#22d3ee", "#39d353"]
st = "".join(f'<stop offset="{i/8:.3f}" stop-color="{c}"/>' for i, c in enumerate(stops))
open(f"{OUT}/divider.svg", "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 6" width="800" height="6" role="presentation">
<defs><linearGradient id="d" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="400" y2="0" spreadMethod="repeat">{st}
<animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="400 0" dur="9s" repeatCount="indefinite"/></linearGradient></defs>
<rect y="1" width="800" height="4" rx="2" fill="url(#d)" opacity=".9"/></svg>''')
