#!/usr/bin/env python3
"""WCAG 2.x contrast checker.

Usage:
  python scripts/contrast.py "#1a1a1a" "#f5f2ea"
  python scripts/contrast.py "#1a1a1a" "#f5f2ea" "#8a8a8a" "#ffffff"   # several fg bg pairs

Each pair is (foreground, background). Prints the ratio and pass/fail for
normal text (4.5), large text (3.0) and UI components (3.0).
Accepts #rgb, #rrggbb with or without '#'. Opaque colors only.
"""
import sys


def parse(hex_color: str):
    h = hex_color.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Invalid color: {hex_color!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def channel(c: int) -> float:
    s = c / 255
    return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4


def luminance(rgb) -> float:
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: str, bg: str) -> float:
    l1, l2 = luminance(parse(fg)), luminance(parse(bg))
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def main(argv):
    args = argv[1:]
    if len(args) < 2 or len(args) % 2:
        print(__doc__)
        return 2
    worst = 99.0
    for fg, bg in zip(args[::2], args[1::2]):
        r = ratio(fg, bg)
        worst = min(worst, r)
        print(
            f"{fg} on {bg}: {r:.2f}:1  "
            f"text {'PASS' if r >= 4.5 else 'FAIL'}  "
            f"large {'PASS' if r >= 3 else 'FAIL'}  "
            f"UI {'PASS' if r >= 3 else 'FAIL'}"
        )
    return 0 if worst >= 4.5 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
