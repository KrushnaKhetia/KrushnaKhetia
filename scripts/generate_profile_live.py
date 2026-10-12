"""Build the theme-aware animated profile.sh-style SVG banner."""

from html import escape
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
AVATAR = ROOT / "assets/avatar.png"
WIDTH, HEIGHT = 1180, 610
ROWS = [
    ("Subject", "Krushna Khetia"),
    ("Role", "B.Tech IT Student"),
    ("Origin", "LJ University · India"),
    ("Status", "Learning + Building + Growing"),
    ("ToolChain", "Java · SQL · Git"),
    ("Core.Lang", "Java · Python · SQL"),
    ("Core.Frontend", "Learning Full Stack Development"),
    ("Core.Backend", "Java · Python"),
    ("Core.Database", "MySQL · DBMS"),
    ("Core.Tools", "Git · GitHub · VS Code"),
    ("Grid.Mail", "—"),
    ("Grid.LinkedIn", "/in/krushna-khetia-562579230"),
    ("Grid.GitHub", "KrushnaKhetia"),
    ("Grid.Focus", "Practical Software Projects"),
]

THEMES = {
    "dark": dict(bg="#0A101F", panel="#0D1628", panel2="#101B30", line="#25344C",
                 muted="#8291A8", text="#DDE7F5", portrait="#AA9BEF", chrome="#22D3EE",
                 shadow="#02050B"),
    "light": dict(bg="#F6F8FA", panel="#FFFFFF", panel2="#EDF3F7", line="#CBD7E1",
                  muted="#64748B", text="#172033", portrait="#4A3D7A", chrome="#0891B2",
                  shadow="#AAB7C4"),
}


def render(theme_name: str, avatar_uri: str) -> str:
    t = THEMES[theme_name]
    portrait = portrait_path(theme_name)
    lines = []
    y = 153
    for label, value in ROWS:
        value_len = len(value) * 8.47
        label_end = 491 + len(label) * 8.47 + 12
        leader_end = 1127 - value_len - 12
        dots = "".join(
            f'<circle cx="{x}" cy="{y - 4}" r=".8" fill="{t["line"]}"/>'
            for x in range(int(label_end), int(leader_end), 7)
        )
        lines.append(
            f'<text x="491" y="{y}" fill="{t["muted"]}" class="mono">{escape(label)}</text>'
            f'<g>{dots}</g><text x="1127" y="{y}" text-anchor="end" fill="{t["text"]}" '
            f'class="mono" textLength="{value_len:.0f}" lengthAdjust="spacingAndGlyphs">{escape(value)}</text>'
        )
        y += 23

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">Krushna's live system profile</title>
<desc id="desc">Animated terminal profile with Krushna's portrait and personal information.</desc>
<defs>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="{t['shadow']}" flood-opacity=".28"/></filter>
  <filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="3" result="b"/><feFlood flood-color="{t['chrome']}" flood-opacity=".35"/><feComposite in2="b" operator="in"/><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <clipPath id="photo"><rect x="74" y="154" width="340" height="340" rx="3"/></clipPath>
  <pattern id="scan" width="5" height="5" patternUnits="userSpaceOnUse"><path d="M0 4.5H5" stroke="{t['portrait']}" stroke-opacity=".22" stroke-width=".7"/></pattern>
  <style>.mono{{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:14px}} .logo{{fill:none;stroke:{t['portrait']};stroke-width:10;stroke-linecap:round;stroke-linejoin:round}}</style>
</defs>
<rect width="1180" height="610" rx="18" fill="{t['bg']}"/>
<rect x="13" y="13" width="1154" height="584" rx="13" fill="{t['panel']}" stroke="{t['line']}" filter="url(#shadow)"/>
<path d="M13 62H1167" stroke="{t['line']}"/>
<circle cx="38" cy="38" r="6" fill="#FF5F57"/><circle cx="59" cy="38" r="6" fill="#FEBC2E"/><circle cx="80" cy="38" r="6" fill="#28C840"/>
<text x="590" y="43" text-anchor="middle" fill="{t['muted']}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" letter-spacing=".4">profile.sh --live</text>
<rect x="35" y="88" width="418" height="472" rx="6" fill="{t['panel2']}" stroke="{t['line']}"/><path d="M35 124H453" stroke="{t['line']}"/>
<text x="49" y="111" fill="{t['chrome']}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="1.2">VISUAL.MAP</text>
<text x="438" y="111" text-anchor="end" fill="{t['muted']}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11">PROFILE / 1-BIT</text>
<path d="M49 141h12M49 141v12M439 141h-12M439 141v12M49 539h12M49 539v-12M439 539h-12M439 539v-12" fill="none" stroke="{t['chrome']}" opacity=".55"/>
<g clip-path="url(#photo)" shape-rendering="crispEdges"><path d="{portrait}" fill="none" stroke="{t['portrait']}" stroke-width="1"/><rect x="74" y="154" width="340" height="340" fill="url(#scan)" opacity=".25"/>
  <g class="logo" opacity="0"><path d="M244 190l24 14v28l-24 14-24-14v-28zM244 176v14m0 56v14m-37-53-12-7m98 56-12-7m-74 0-12 7m98-56-12 7"/><animate attributeName="opacity" values="0;0;.8;.8;0" keyTimes="0;.18;.23;.36;.42" dur="8s" repeatCount="indefinite"/></g>
  <g class="logo" opacity="0"><path d="M211 263l-29-26 29-26m66 0 29 26-29 26m-20-72-27 92"/><animate attributeName="opacity" values="0;0;.9;.9;0" keyTimes="0;.42;.47;.61;.67" dur="8s" repeatCount="indefinite"/></g>
  <g opacity="0" fill="{t['chrome']}"><path d="M244 186l12 39 40 0-32 23 12 39-32-24-32 24 12-39-32-23h40z"/><animate attributeName="opacity" values="0;0;.9;.9;0" keyTimes="0;.67;.72;.86;.92" dur="8s" repeatCount="indefinite"/></g>
  <rect x="74" y="154" width="340" height="340" fill="none" stroke="{t['line']}"/></g>
<text x="58" y="551" fill="{t['muted']}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="10">PROFILE IMAGE · KRUSHNAKHETIA</text>
<rect x="474" y="88" width="672" height="472" rx="6" fill="{t['panel2']}" stroke="{t['line']}"/><path d="M474 124H1146" stroke="{t['line']}"/>
<text x="490" y="111" fill="{t['chrome']}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="13" font-weight="700" letter-spacing="1.2">SYSTEM.INFO</text>
<g filter="url(#glow)"><circle cx="915" cy="106" r="4" fill="#FF4D5A"><animate attributeName="opacity" values="1;.3;1" dur="1.6s" repeatCount="indefinite"/></circle></g>
<text x="927" y="111" fill="#FF4D5A" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="12" font-weight="700">LIVE</text>
<rect x="982" y="94" width="146" height="24" rx="12" fill="{t['chrome']}" opacity=".16" stroke="{t['chrome']}"/><text x="1055" y="111" text-anchor="middle" fill="{t['chrome']}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="14" font-weight="700">@KrushnaKhetia</text>
{''.join(lines)}
<path d="M490 530H1130" stroke="{t['line']}"/><text x="491" y="548" fill="#10B981" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11">● ALL SYSTEMS NOMINAL</text><text x="1128" y="548" text-anchor="end" fill="{t['muted']}" font-family="ui-monospace,SFMono-Regular,Consolas,monospace" font-size="11">INDIA · IST NODE</text>
</svg>'''


def main() -> None:
    if not AVATAR.exists():
        raise SystemExit(f"Missing profile avatar: {AVATAR}")
    for theme in THEMES:
        out = ROOT / "assets" / f"profile-live-{theme}.svg"
        out.write_text(render(theme, ""), encoding="utf-8")
        print(f"Wrote {out.relative_to(ROOT)}")


def portrait_path(theme: str) -> str:
    """Dither the public profile avatar into compact terminal-style dot paths."""
    image = Image.open(AVATAR).convert("RGB")
    side = min(image.size)
    left = (image.width - side) // 2
    top = (image.height - side) // 2
    image = image.crop((left, top, left + side, top + side)).resize((300, 300), Image.Resampling.LANCZOS)
    canvas = Image.new("L", (300, 340), 0)
    canvas.paste(ImageOps.grayscale(image), (0, 20))
    values = np.asarray(canvas, dtype=np.float32) / 255.0
    dots = np.zeros(values.shape, dtype=bool)
    for y in range(values.shape[0]):
        xs = range(values.shape[1]) if y % 2 == 0 else range(values.shape[1] - 1, -1, -1)
        direction = 1 if y % 2 == 0 else -1
        for x in xs:
            old = values[y, x]
            new = 1.0 if old >= .5 else 0.0
            dots[y, x] = new > 0 if theme == "dark" else new == 0
            error = old - new
            nx = x + direction
            if 0 <= nx < values.shape[1]:
                values[y, nx] += error * 7 / 16
            if y + 1 < values.shape[0]:
                if 0 <= x - direction < values.shape[1]:
                    values[y + 1, x - direction] += error * 3 / 16
                values[y + 1, x] += error * 5 / 16
                if 0 <= nx < values.shape[1]:
                    values[y + 1, nx] += error / 16
    paths = []
    for y, row in enumerate(dots):
        xs = np.flatnonzero(row)
        if not len(xs):
            continue
        start = previous = int(xs[0])
        for x in map(int, xs[1:]):
            if x > previous + 1:
                paths.append(f"M{74 + start} {154 + y}h{previous - start + 1}")
                start = x
            previous = x
        paths.append(f"M{74 + start} {154 + y}h{previous - start + 1}")
    return "".join(paths)


if __name__ == "__main__":
    main()
