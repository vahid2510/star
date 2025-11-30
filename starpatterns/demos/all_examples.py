"""Full showcase script for the entire library, with emphasis on animations."""

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


def show_patterns() -> None:
    print("== Basic ==")
    print(triangle(4))
    print()
    print(square(4))
    print()
    print(diamond(5))

    print("\n== Advanced ==")
    print(hollow_square(5))
    print()
    print(cross(5))
    print()
    print(hourglass(7))

    print("\n== Fractal ==")
    print(sierpinski(order=3))


def show_colors() -> None:
    print("\n== Colors ==")
    print(colorize("Red text", fg="red"))
    print(colorize("Cyan bold underlined", fg="cyan", bold=True, underline=True))
    print(rgb("RGB example", 120, 80, 220))


def show_animations() -> None:
    print("\n== Animations ==")
    print("Wave:")
    wave_text("Animated wave", amplitude=4, speed=0.05, cycles=1)
    print("Spinner:")
    spinner("Working", duration=1.5, interval=0.1)
    print("Bouncing ball:")
    bouncing_ball(width=22, height=6, frames=45, delay=0.04, char="*")
    time.sleep(0.2)


def main() -> None:
    clear_terminal()
    show_patterns()
    show_colors()
    show_animations()


if __name__ == "__main__":
    main()
