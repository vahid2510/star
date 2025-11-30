"""Full showcase script for the entire library, with emphasis on animations."""

import time

from starpatterns import (
    bouncing_ball,
    clear_terminal,
    colorize,
    cross,
    diamond,
    loading_bar,
    marquee,
    hollow_square,
    hourglass,
    matrix_rain,
    snake_line,
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
    spinner("Working", duration=1.2, interval=0.08)
    print("Loading bar:")
    loading_bar(width=25, duration=1.2, char="#")
    print("Marquee:")
    marquee("Scrolling text showcase", width=28, cycles=1, speed=0.04)
    print("Snake line:")
    snake_line(width=32, length=10, frames=60, delay=0.03, head="O", body="o")
    print("Matrix rain (short preview):")
    matrix_rain(width=24, height=8, frames=40, delay=0.04)
    print("Bouncing ball:")
    bouncing_ball(width=22, height=6, frames=35, delay=0.04, char="*")
    time.sleep(0.2)


def main() -> None:
    clear_terminal()
    show_patterns()
    show_colors()
    show_animations()


if __name__ == "__main__":
    main()
