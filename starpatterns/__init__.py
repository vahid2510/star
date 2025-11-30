"""
starpatterns package entrypoint.

Provides convenient imports for patterns, fractals, animations, and utilities.
"""

from importlib.metadata import version, PackageNotFoundError

from .patterns.basic import triangle, square, diamond
from .patterns.advanced import hollow_square, cross, hourglass
from .patterns.fractal import sierpinski
from .patterns.animation import (
    bar_wave,
    bouncing_ball,
    bouncing_text,
    carousel,
    blinking_text,
    countdown,
    dna_helix,
    equalizer,
    falling_sand,
    fireworks,
    loading_bar,
    marquee,
    matrix_rain,
    orbit,
    progress_dots,
    pulse_text,
    rising_bar,
    ripple_line,
    shooting_star,
    snake_line,
    spinner,
    twinkle_stars,
    typing_text,
    wave_text,
)
from .utils.colors import colorize, rgb
from .utils.terminal import clear_terminal

try:
    __version__ = version("starpatterns")
except PackageNotFoundError:  # Local, editable installs
    __version__ = "0.0.0"

__all__ = [
    "triangle",
    "square",
    "diamond",
    "hollow_square",
    "cross",
    "hourglass",
    "sierpinski",
    "wave_text",
    "bouncing_ball",
    "spinner",
    "loading_bar",
    "typing_text",
    "blinking_text",
    "marquee",
    "bouncing_text",
    "pulse_text",
    "snake_line",
    "progress_dots",
    "countdown",
    "ripple_line",
    "bar_wave",
    "matrix_rain",
    "equalizer",
    "fireworks",
    "twinkle_stars",
    "dna_helix",
    "shooting_star",
    "rising_bar",
    "orbit",
    "falling_sand",
    "carousel",
    "colorize",
    "rgb",
    "clear_terminal",
]
