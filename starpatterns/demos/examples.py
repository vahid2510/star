"""Interactive demo showcasing all library features."""

import time

from starpatterns import (
    bouncing_ball,
    clear_terminal,
    colorize,
    cross,
    diamond,
    hollow_square,
    hourglass,
    rgb,
    sierpinski,
    spinner,
    square,
    triangle,
    wave_text,
)


def demo_patterns() -> None:
    print("=== Basic Patterns ===")
    print(triangle(4))
    print()
    print(square(4))
    print()
    print(diamond(5))
    print("\n=== Advanced Patterns ===")
    print(hollow_square(5))
    print()
    print(cross(5))
    print()
    print(hourglass(7))
    print("\n=== Fractal Pattern ===")
    print(sierpinski(order=3))


def demo_colors() -> None:
    print("\n=== Colors ===")
    print(colorize("Red text", fg="red"))
    print(colorize("Green on blue bold", fg="green", bg="blue", bold=True))
    print(rgb("RGB magenta-ish", 200, 50, 200))


def demo_animations() -> None:
    print("\n=== Animations ===")
    print("Wave text:")
    wave_text("Hello, wave!", amplitude=3, speed=0.05, cycles=1)
    print("Spinner:")
    spinner("Processing", duration=1.5, interval=0.12)
    print("Bouncing ball:")
    bouncing_ball(width=20, height=6, frames=40, delay=0.04, char="*")
    time.sleep(0.2)


def run_all() -> None:
    clear_terminal()
    demo_patterns()
    demo_colors()
    demo_animations()


if __name__ == "__main__":
    run_all()
