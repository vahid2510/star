"""Terminal animations."""

from __future__ import annotations

import math
import sys
import time
from itertools import cycle

from ..utils.terminal import move_cursor_home


def wave_text(text: str, amplitude: int = 2, speed: float = 0.08, cycles: int = 2) -> None:
    """
    Animate text moving in a horizontal sine wave.

    Args:
        text: Text to animate.
        amplitude: Maximum indentation in spaces.
        speed: Delay between frames in seconds.
        cycles: Number of full sine cycles to render.
    """
    if amplitude < 0:
        raise ValueError("amplitude must be non-negative")
    if speed <= 0:
        raise ValueError("speed must be positive")
    frames = int(cycles * 2 * math.pi * 4) or 1
    for i in range(frames):
        offset = int(amplitude * (1 + math.sin(i / 4.0)))
        sys.stdout.write("\r" + " " * offset + text)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write("\r" + text + "\n")
    sys.stdout.flush()


def bouncing_ball(width: int = 20, height: int = 5, frames: int = 80, delay: float = 0.05, char: str = "o") -> None:
    """
    Animate a single bouncing ball within a rectangular field.

    Args:
        width: Width of the field.
        height: Height of the field.
        frames: Number of frames to render.
        delay: Delay between frames in seconds.
        char: Character used for the ball.
    """
    if width < 2 or height < 2:
        raise ValueError("width and height must be at least 2")
    if len(char) != 1:
        raise ValueError("char must be a single character")
    x, y = 0, 0
    dx, dy = 1, 1
    # Prepare drawing surface height so cursor stays within bounds.
    print("\n" * (height - 1))
    for _ in range(frames):
        grid_lines = []
        for row in range(height):
            line_chars = []
            for col in range(width):
                line_chars.append(char if (col, row) == (x, y) else " ")
            grid_lines.append("".join(line_chars))
        move_cursor_home()
        sys.stdout.write("\n".join(grid_lines))
        sys.stdout.flush()
        time.sleep(delay)

        x += dx
        y += dy
        if x <= 0 or x >= width - 1:
            dx *= -1
        if y <= 0 or y >= height - 1:
            dy *= -1
    sys.stdout.write("\n")
    sys.stdout.flush()


def spinner(text: str = "Loading", duration: float = 2.0, interval: float = 0.1) -> None:
    """
    Animate a classic command-line spinner.

    Args:
        text: Text to render beside the spinner.
        duration: Total time to animate in seconds.
        interval: Delay between frames in seconds.
    """
    if duration <= 0:
        raise ValueError("duration must be positive")
    if interval <= 0:
        raise ValueError("interval must be positive")
    spin_frames = cycle("|/-\\")
    end_time = time.time() + duration
    while time.time() < end_time:
        frame = next(spin_frames)
        sys.stdout.write(f"\r{frame} {text}")
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write("\r[done] " + text + " " * 3 + "\n")
    sys.stdout.flush()
