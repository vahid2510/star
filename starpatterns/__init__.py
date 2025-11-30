"""
starpatterns package entrypoint.

Provides convenient imports for patterns, fractals, animations, and utilities.
"""

from importlib.metadata import version, PackageNotFoundError

from .patterns.basic import triangle, square, diamond
from .patterns.advanced import hollow_square, cross, hourglass
from .patterns.fractal import sierpinski
from .patterns.animation import wave_text, bouncing_ball, spinner
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
    "colorize",
    "rgb",
    "clear_terminal",
]
