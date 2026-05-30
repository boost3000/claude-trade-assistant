#!/usr/bin/env python3
"""Generate the boost3000 logo SVG.

The background candlestick chart is built from a continuous OHLC series
(open[i] == close[i-1]) so each candle's close aligns vertically with the
next candle's open, and bodies sit edge-to-edge with no horizontal gaps.
A strong upward drift keeps the chart trending "to the moon" while high
per-candle volatility (plus occasional spikes) keeps it lively.

Run from anywhere:  python3 assets/gen_logo.py
Writes:             assets/boost3000-logo.svg  (next to this script)
"""
import os
import random

random.seed(11)  # deterministic output

# ---- chart geometry -------------------------------------------------------
N = 48
X_LEFT, X_RIGHT = 5, 635          # full card width
PITCH = (X_RIGHT - X_LEFT) / N    # slot width; body fills it -> no h-gaps
Y_TOP, Y_BOT = 12, 152            # vertical band the chart occupies
GREEN, RED = "#22c55e", "#ef4444"

# ---- continuous OHLC walk: strong uptrend + high volatility ---------------
candles = []
op = 100.0
drift = 6.5                        # strong upward bias -> clearly to the moon
for i in range(N):
    change = drift + random.uniform(-19.0, 19.0)
    if random.random() < 0.28:     # frequent violent spike either way
        change += random.uniform(-24.0, 24.0)
    cl = op + change
    body = abs(cl - op)
    # long, uneven wicks proportional to the move -> dramatic candles
    hi = max(op, cl) + random.uniform(1.0, 5.0) + body * random.uniform(0.15, 1.0)
    lo = min(op, cl) - random.uniform(1.0, 5.0) - body * random.uniform(0.15, 1.0)
    candles.append((op, hi, lo, cl))
    op = cl                       # next candle opens exactly at this close

prices = [v for c in candles for v in c]
pmin, pmax = min(prices), max(prices)

def y(p):
    return Y_BOT - (p - pmin) / (pmax - pmin) * (Y_BOT - Y_TOP)

green, red = [], []
for i, (o, h, l, c) in enumerate(candles):
    cx = X_LEFT + (i + 0.5) * PITCH
    yo, yc, yh, yl = y(o), y(c), y(h), y(l)
    up = c >= o
    top, bot = min(yo, yc), max(yo, yc)
    bh = max(bot - top, 1.4)      # keep near-doji candles visible
    x = cx - PITCH / 2            # body width == pitch -> bodies touch
    wick = f'<line x1="{cx:.1f}" y1="{yh:.1f}" x2="{cx:.1f}" y2="{yl:.1f}" stroke-width="1.1"/>'
    body_rect = f'<rect x="{x:.1f}" y="{top:.1f}" width="{PITCH:.1f}" height="{bh:.1f}"/>'
    (green if up else red).append("      " + wick + body_rect)

candle_block = (
    '  <g clip-path="url(#cardClip)" opacity="0.22">\n'
    f'    <g stroke="{GREEN}" fill="{GREEN}">\n' + "\n".join(green) + "\n    </g>\n"
    f'    <g stroke="{RED}" fill="{RED}">\n' + "\n".join(red) + "\n    </g>\n"
    "  </g>"
)

# ---- assemble full SVG ----------------------------------------------------
template = r'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 180" width="640" height="180" role="img" aria-label="boost3000">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0f1b2d"/>
      <stop offset="1" stop-color="#080d15"/>
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#22d3ee"/>
      <stop offset="0.55" stop-color="#2dd4bf"/>
      <stop offset="1" stop-color="#4ade80"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1e3a5f"/>
      <stop offset="1" stop-color="#0c1a2c"/>
    </linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="1" stop-color="#bcc8d6"/>
    </linearGradient>
    <linearGradient id="flame" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#fde68a"/>
      <stop offset="0.5" stop-color="#fbbf24"/>
      <stop offset="1" stop-color="#f97316"/>
    </linearGradient>
    <radialGradient id="moon" cx="0.4" cy="0.4" r="0.75">
      <stop offset="0" stop-color="#f8fafc"/>
      <stop offset="1" stop-color="#cbd5e1"/>
    </radialGradient>
    <clipPath id="cardClip">
      <rect x="3" y="3" width="634" height="174" rx="26"/>
    </clipPath>
    <clipPath id="badgeClip">
      <rect x="96" y="26" width="128" height="128" rx="30"/>
    </clipPath>
    <filter id="glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="3.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- card -->
  <rect x="3" y="3" width="634" height="174" rx="26" fill="url(#bg)" stroke="url(#edge)" stroke-width="1.5"/>

  <!-- background candlestick chart, generated from a continuous OHLC series -->
__CANDLES__

  <!-- top sheen -->
  <rect x="3" y="3" width="634" height="58" rx="26" fill="#ffffff" opacity="0.03"/>

  <!-- badge -->
  <rect x="96" y="26" width="128" height="128" rx="30" fill="#0a1320" stroke="url(#accent)" stroke-width="1.5"/>

  <!-- space scene (origin at badge centre, scaled up to fill the larger badge) -->
  <g clip-path="url(#badgeClip)">
    <g transform="translate(160,90) scale(1.23)">
      <!-- stars, spread evenly across the badge -->
      <circle cx="-42" cy="-36" r="1.5" fill="#e2e8f0" opacity="0.85"/>
      <circle cx="-6"  cy="-42" r="1.2" fill="#e2e8f0" opacity="0.8"/>
      <circle cx="18"  cy="-34" r="1.1" fill="#e2e8f0" opacity="0.7"/>
      <circle cx="46"  cy="-42" r="1.2" fill="#e2e8f0" opacity="0.6"/>
      <circle cx="-48" cy="-6"  r="1.4" fill="#e2e8f0" opacity="0.75"/>
      <circle cx="-28" cy="-12" r="1.1" fill="#e2e8f0" opacity="0.6"/>
      <circle cx="16"  cy="-2"  r="1.2" fill="#e2e8f0" opacity="0.7"/>
      <circle cx="48"  cy="0"   r="1.3" fill="#e2e8f0" opacity="0.65"/>
      <circle cx="50"  cy="-18" r="1.1" fill="#e2e8f0" opacity="0.55"/>
      <circle cx="-20" cy="40"  r="1.3" fill="#e2e8f0" opacity="0.6"/>
      <circle cx="6"   cy="30"  r="1.1" fill="#e2e8f0" opacity="0.6"/>
      <circle cx="22"  cy="20"  r="1.0" fill="#e2e8f0" opacity="0.5"/>
      <circle cx="44"  cy="20"  r="1.2" fill="#e2e8f0" opacity="0.55"/>
      <path d="M-30,-44 l1.6,4 4,1.6 -4,1.6 -1.6,4 -1.6,-4 -4,-1.6 4,-1.6 Z" fill="#fde68a" opacity="0.9"/>
      <path d="M38,30 l1.3,3.2 3.2,1.3 -3.2,1.3 -1.3,3.2 -1.3,-3.2 -3.2,-1.3 3.2,-1.3 Z" fill="#fde68a" opacity="0.8"/>

      <!-- moon (darker craters) -->
      <circle cx="30" cy="-30" r="14" fill="url(#moon)"/>
      <circle cx="33" cy="-34" r="2.6" fill="#7e8ba0" opacity="0.85"/>
      <circle cx="25" cy="-27" r="2" fill="#7e8ba0" opacity="0.8"/>
      <circle cx="34" cy="-24" r="1.6" fill="#7e8ba0" opacity="0.8"/>

      <!-- exhaust puffs (trailing lower-left) -->
      <circle cx="-34" cy="33" r="3.2" fill="#fbbf24" opacity="0.35"/>
      <circle cx="-41" cy="40" r="2.2" fill="#fbbf24" opacity="0.22"/>
      <circle cx="-47" cy="46" r="1.4" fill="#fbbf24" opacity="0.15"/>

      <!-- rocket: drawn nose-up, tilted 45 to aim up-right at the moon -->
      <g transform="translate(-8,6) rotate(45)">
        <g filter="url(#glow)">
          <path d="M-7,17 Q-9,31 0,41 Q9,31 7,17 Z" fill="url(#flame)"/>
          <path d="M-3.5,18 Q-4,27 0,34 Q4,27 3.5,18 Z" fill="#fff7ed"/>
        </g>
        <path d="M-10,4 L-21,19 L-10,14 Z" fill="#2dd4bf"/>
        <path d="M10,4 L21,19 L10,14 Z" fill="#22d3ee"/>
        <path d="M-10,-12 L10,-12 L10,12 Q10,16 6,17 L-6,17 Q-10,16 -10,12 Z" fill="url(#body)"/>
        <path d="M0,-30 C5,-24 10,-19 10,-12 L-10,-12 C-10,-19 -5,-24 0,-30 Z" fill="url(#accent)"/>
        <!-- rising-chart screen painted on the hull -->
        <rect x="-7" y="-5" width="14" height="13" rx="3" fill="#0f1b2d"/>
        <polyline points="-4,5 -1,1 2,3 5,-3" fill="none" stroke="url(#accent)"
                  stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M5,-3 l-2.6,0 M5,-3 l0,2.6" fill="none" stroke="url(#accent)" stroke-width="1.6" stroke-linecap="round"/>
      </g>
    </g>
  </g>

  <!-- wordmark -->
  <text x="250" y="110" font-family="'Segoe UI', Helvetica, Arial, sans-serif"
        font-size="58" font-weight="800" letter-spacing="-1">
    <tspan fill="#f1f5f9">boost</tspan><tspan fill="url(#accent)">3000</tspan>
  </text>
</svg>
'''

svg = template.replace("__CANDLES__", candle_block)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "boost3000-logo.svg")
with open(out, "w") as f:
    f.write(svg)
print(f"wrote {out} with {N} candles ({len(green)} green, {len(red)} red), pitch={PITCH:.1f}")
