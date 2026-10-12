"""Build the theme-aware animated profile.sh-style SVG banner."""

from html import escape
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parents[1]
AVATAR = ROOT / "assets/krushna-cutout.png"
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
    portrait, travellers = portrait_art(theme_name, t["portrait"])
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
<g clip-path="url(#photo)" shape-rendering="crispEdges">{portrait}<g>{travellers}</g>
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


def num(value: float) -> str:
    return f"{value:.1f}".rstrip("0").rstrip(".")


def point_path(points: np.ndarray) -> str:
    if not len(points):
        return ""
    integer = np.rint(points).astype(int)
    unique = sorted({(int(x), int(y)) for x, y in integer}, key=lambda p: (p[1], p[0]))
    chunks = []
    i = 0
    while i < len(unique):
        x0, y = unique[i]
        x1 = x0
        i += 1
        while i < len(unique) and unique[i][1] == y and unique[i][0] <= x1 + 1:
            x1 = unique[i][0]
            i += 1
        chunks.append(f"M{x0} {y}h{x1 - x0 + 1}")
    return "".join(chunks)


def portrait_art(theme: str, color: str) -> tuple[str, str]:
    """Dither the avatar and animate a sample of its dots into tech silhouettes."""
    from PIL import ImageDraw

    # The supplied photo already has a real alpha cutout. Fit the complete
    # subject into the 300×340 dither canvas, rather than approximating it with
    # a polygon and clipping the shoulders at the frame border.
    source = Image.open(AVATAR).convert("RGBA")
    bounds = source.getchannel("A").getbbox()
    if bounds is None:
        raise SystemExit("Profile image must include a visible subject")
    subject = source.crop(bounds)
    scale = min(282 / subject.width, 320 / subject.height)
    subject = subject.resize(
        (round(subject.width * scale), round(subject.height * scale)),
        Image.Resampling.LANCZOS,
    )
    crop = Image.new("RGBA", (300, 340), (0, 0, 0, 0))
    crop.alpha_composite(subject, ((300 - subject.width) // 2, 340 - subject.height - 10))
    alpha = np.asarray(crop.getchannel("A"), dtype=np.float32) / 255.0
    visible = alpha > 0.08
    mask = Image.fromarray(np.uint8(visible * 255), "L")
    rgb = crop.convert("RGB")
    if theme == "dark":
        luminance = np.asarray(ImageOps.grayscale(rgb), dtype=np.float32)
        prepared = Image.fromarray(np.uint8(np.clip(luminance * alpha, 0, 255)), "L")
    else:
        white = Image.new("RGBA", crop.size, "white")
        white.alpha_composite(crop)
        prepared = ImageOps.grayscale(white.convert("RGB"))
    prepared = ImageOps.equalize(prepared, mask=mask)
    prepared = ImageEnhance.Contrast(prepared).enhance(1.35)
    prepared = prepared.filter(ImageFilter.UnsharpMask(radius=2, percent=175, threshold=1))
    values = np.asarray(prepared, dtype=np.float32) / 255.0
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
    dots &= visible
    portrait = np.column_stack(np.where(dots)[::-1]).astype(np.float32)
    rng = np.random.default_rng(314159)
    if len(portrait) > 18000:
        portrait = portrait[rng.choice(len(portrait), 18000, replace=False)]
    portrait += np.array([74, 154], dtype=np.float32)

    # Fade and drift 94 small bands of the portrait as the travelling pixels
    # form each logo, matching the dissolve in the supplied reference banner.
    gear_center = np.array([224.0, 324.0])
    band_ids = rng.integers(0, 94, size=len(portrait))
    static_paths = []
    key_times = ";".join(num(v / 14.2) for v in [0, 3.0, 4.3, 6.3, 7.6, 9.6, 10.9, 12.9, 14.2])
    for band in range(94):
        pts = portrait[band_ids == band]
        if not len(pts):
            continue
        delta = (gear_center - pts.mean(axis=0)) * .18 + rng.normal(0, 4, size=2)
        d = point_path(pts)
        static_paths.append(
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1" opacity=".94">'
            f'<animateTransform attributeName="transform" type="translate" begin="3.2s" '
            f'dur="14.2s" repeatCount="indefinite" calcMode="linear" keyTimes="{key_times}" '
            f'values="0 0;0 0;{num(delta[0])} {num(delta[1])};{num(delta[0])} {num(delta[1])};'
            '0 0;0 0;0 0;0 0;0 0"/>'
            f'<animate attributeName="opacity" begin="3.2s" dur="14.2s" repeatCount="indefinite" '
            f'keyTimes="{key_times}" values=".94;.94;0;0;0;0;0;0;.94"/></path>'
        )
    count = min(900, len(portrait))
    source = portrait[rng.choice(len(portrait), count, replace=False)]
    targets = []
    for kind in ("gear", "code", "star"):
        mask = Image.new("L", (400, 400), 0)
        draw = ImageDraw.Draw(mask)
        if kind == "gear":
            center = np.array([200.0, 200.0])
            outer = []
            for tooth in range(12):
                base = tooth * math.tau / 12
                for offset, radius in [(-.42, 150), (-.30, 178), (.30, 178), (.42, 150)]:
                    angle = base + offset * math.tau / 12
                    outer.append(tuple(center + radius * np.array([np.cos(angle), np.sin(angle)])))
            draw.polygon(outer, fill=255)
            draw.ellipse((70, 70, 330, 330), fill=255)
            draw.ellipse((128, 128, 272, 272), fill=0)
            draw.ellipse((174, 174, 226, 226), fill=255)
        elif kind == "code":
            draw.line([(112, 105), (58, 170), (112, 235)], fill=255, width=18, joint="curve")
            draw.line([(188, 105), (242, 170), (188, 235)], fill=255, width=18, joint="curve")
            draw.line([(165, 84), (135, 256)], fill=255, width=18)
        else:
            star = []
            for i in range(16):
                angle = -np.pi / 2 + i * np.pi / 8
                radius = 137 if i % 4 == 0 else (45 if i % 2 == 0 else 25)
                star.append((200 + np.cos(angle) * radius, 200 + np.sin(angle) * radius))
            draw.polygon(star, fill=255)
            nodes = [(82, 112), (322, 106), (326, 300), (88, 316)]
            for a, b in zip(nodes, nodes[1:] + nodes[:1]):
                draw.line([a, b], fill=255, width=12)
            for x, y in nodes:
                draw.ellipse((x - 19, y - 19, x + 19, y + 19), fill=255)
        cloud = np.column_stack(np.where(np.asarray(mask) > 0)[::-1]).astype(np.float32)
        # Match the reference banner's logo coordinates inside the portrait
        # frame. These are already banner-space origins, so don't subtract the
        # portrait frame origin a second time.
        cloud = np.column_stack((89 + cloud[:, 0] * .675, 188 + cloud[:, 1] * .675))
        chosen = cloud[rng.choice(len(cloud), count, replace=len(cloud) < count)]
        chosen = chosen[np.lexsort((chosen[:, 0], chosen[:, 1]))]
        targets.append(chosen)
    source = source[np.lexsort((source[:, 0], source[:, 1]))]
    frames = [source, source, targets[0], targets[0], targets[1], targets[1],
              targets[2], targets[2], source]
    opacity_values = "0;0;1;1;1;1;1;1;0"
    animated = []
    for i in range(count):
        positions = ";".join(f"{num(point[i, 0])} {num(point[i, 1])}" for point in frames)
        animated.append(
            f'<path d="M-.65-.65h1.3v1.3h-1.3z" fill="{color}">'
            f'<animateTransform attributeName="transform" type="translate" begin="3.2s" '
            f'dur="14.2s" repeatCount="indefinite" calcMode="linear" keyTimes="{key_times}" '
            f'values="{positions}"/>'
            f'<animate attributeName="opacity" begin="3.2s" dur="14.2s" repeatCount="indefinite" '
            f'calcMode="linear" keyTimes="{key_times}" values="{opacity_values}"/></path>'
        )
    return "".join(static_paths), "".join(animated)


if __name__ == "__main__":
    main()
