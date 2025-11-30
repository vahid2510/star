"""Terminal animations with no external dependencies."""

from __future__ import annotations

import math
import random
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


def loading_bar(width: int = 30, duration: float = 2.0, char: str = "#") -> None:
    """
    Animate a horizontal progress bar.

    Args:
        width: Number of bar cells.
        duration: Total animation duration in seconds.
        char: Fill character for the bar.
    """
    if width <= 0:
        raise ValueError("width must be positive")
    if duration <= 0:
        raise ValueError("duration must be positive")
    if len(char) != 1:
        raise ValueError("char must be a single character")
    steps = width
    delay = duration / steps
    for i in range(steps + 1):
        filled = char * i
        empty = " " * (steps - i)
        percent = int((i / steps) * 100)
        sys.stdout.write(f"\r[{filled}{empty}] {percent:3d}%")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def typing_text(text: str, interval: float = 0.05, cursor: str = "|") -> None:
    """
    Type out text character-by-character.

    Args:
        text: Text to render.
        interval: Delay per character.
        cursor: Cursor indicator appended while typing.
    """
    if interval <= 0:
        raise ValueError("interval must be positive")
    for i in range(len(text) + 1):
        snippet = text[:i]
        trail = cursor if i < len(text) else " "
        sys.stdout.write("\r" + snippet + trail)
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write("\r" + text + "\n")
    sys.stdout.flush()


def blinking_text(text: str, blinks: int = 6, interval: float = 0.3) -> None:
    """
    Blink text on and off.

    Args:
        text: Text to blink.
        blinks: Number of on/off cycles.
        interval: Delay between states.
    """
    if blinks <= 0:
        raise ValueError("blinks must be positive")
    if interval <= 0:
        raise ValueError("interval must be positive")
    blank = " " * len(text)
    for _ in range(blinks):
        sys.stdout.write("\r" + text)
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write("\r" + blank)
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write("\r" + text + "\n")
    sys.stdout.flush()


def marquee(text: str, width: int = 30, cycles: int = 3, speed: float = 0.05) -> None:
    """
    Scroll text horizontally inside a window.

    Args:
        text: Text to scroll.
        width: Visible window width.
        cycles: Number of full scroll cycles.
        speed: Delay between frames.
    """
    if width <= 0:
        raise ValueError("width must be positive")
    if speed <= 0:
        raise ValueError("speed must be positive")
    padded = " " * width + text + " " * width
    steps = len(text) + width
    for _ in range(cycles):
        for i in range(steps):
            sys.stdout.write("\r" + padded[i : i + width])
            sys.stdout.flush()
            time.sleep(speed)
    sys.stdout.write("\r" + " " * width + "\r")
    sys.stdout.flush()


def bouncing_text(text: str, width: int = 30, frames: int = 60, delay: float = 0.05) -> None:
    """
    Bounce a piece of text left and right.

    Args:
        text: Text to move.
        width: Total line width.
        frames: Number of frames.
        delay: Delay between frames.
    """
    if width <= len(text):
        raise ValueError("width must be greater than text length")
    if frames <= 0 or delay <= 0:
        raise ValueError("frames and delay must be positive")
    pos = 0
    direction = 1
    max_pos = width - len(text)
    for _ in range(frames):
        sys.stdout.write("\r" + " " * pos + text + " " * (max_pos - pos))
        sys.stdout.flush()
        time.sleep(delay)
        pos += direction
        if pos <= 0 or pos >= max_pos:
            direction *= -1
    sys.stdout.write("\r" + text + "\n")
    sys.stdout.flush()


def pulse_text(text: str, min_spaces: int = 0, max_spaces: int = 6, cycles: int = 6, delay: float = 0.06) -> None:
    """
    Pulse text in and out by adding indentation.

    Args:
        text: Text to pulse.
        min_spaces: Minimum indentation.
        max_spaces: Maximum indentation.
        cycles: Number of expand/contract cycles.
        delay: Delay between frames.
    """
    if min_spaces < 0 or max_spaces < min_spaces:
        raise ValueError("spaces must be non-negative and max >= min")
    if cycles <= 0 or delay <= 0:
        raise ValueError("cycles and delay must be positive")
    offsets = list(range(min_spaces, max_spaces + 1)) + list(range(max_spaces - 1, min_spaces, -1))
    for _ in range(cycles):
        for offset in offsets:
            sys.stdout.write("\r" + " " * offset + text)
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\r" + text + "\n")
    sys.stdout.flush()


def snake_line(width: int = 30, length: int = 8, frames: int = 100, delay: float = 0.04, head: str = "O", body: str = "o") -> None:
    """
    Draw a one-line snake that slithers horizontally.

    Args:
        width: Total line width.
        length: Snake length.
        frames: Number of frames.
        delay: Delay between frames.
        head: Head character.
        body: Body character.
    """
    if width <= length:
        raise ValueError("width must be greater than length")
    if len(head) != 1 or len(body) != 1:
        raise ValueError("head and body must be single characters")
    positions = list(range(length))
    direction = 1
    for _ in range(frames):
        line = [" "] * width
        for idx, pos in enumerate(positions):
            line[pos] = head if idx == length - 1 else body
        sys.stdout.write("\r" + "".join(line))
        sys.stdout.flush()
        time.sleep(delay)
        # advance
        if positions[-1] >= width - 1:
            direction = -1
        elif positions[0] <= 0:
            direction = 1
        positions = [p + direction for p in positions]
    sys.stdout.write("\n")
    sys.stdout.flush()


def progress_dots(text: str = "Loading", dots: int = 3, cycles: int = 5, delay: float = 0.3) -> None:
    """Animate trailing dots after a message."""
    if dots <= 0 or cycles <= 0 or delay <= 0:
        raise ValueError("dots, cycles, and delay must be positive")
    for _ in range(cycles):
        for i in range(dots + 1):
            sys.stdout.write("\r" + text + "." * i + " " * (dots - i))
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\r" + text + "." * dots + "\n")
    sys.stdout.flush()


def countdown(seconds: int = 5) -> None:
    """Simple countdown timer."""
    if seconds < 0:
        raise ValueError("seconds must be non-negative")
    for remaining in range(seconds, -1, -1):
        sys.stdout.write(f"\r{remaining:2d} seconds")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rGo!        \n")
    sys.stdout.flush()


def ripple_line(width: int = 40, frames: int = 80, delay: float = 0.04, char: str = "*") -> None:
    """
    Create a horizontal ripple using a sine wave.

    Args:
        width: Line width.
        frames: Number of frames.
        delay: Delay between frames.
        char: Character used for the wave.
    """
    if width <= 0 or frames <= 0 or delay <= 0:
        raise ValueError("width, frames, and delay must be positive")
    for i in range(frames):
        offset = int((math.sin(i / 4.0) + 1) * (width / 4))
        sys.stdout.write("\r" + " " * offset + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def bar_wave(width: int = 30, frames: int = 80, delay: float = 0.05, char: str = "|") -> None:
    """Animate multiple bars moving like an equalizer."""
    if width <= 0 or frames <= 0 or delay <= 0:
        raise ValueError("width, frames, and delay must be positive")
    for i in range(frames):
        bars = []
        for x in range(width):
            height = int((math.sin((i + x) / 6.0) + 1) * 3) + 1
            bars.append(char * height)
        sys.stdout.write("\r" + " ".join(bars))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def matrix_rain(width: int = 40, height: int = 12, frames: int = 80, delay: float = 0.05) -> None:
    """
    Simulate a matrix rain effect.

    Args:
        width: Number of columns.
        height: Number of rows.
        frames: Number of frames.
        delay: Delay between frames.
    """
    if width <= 0 or height <= 0 or frames <= 0 or delay <= 0:
        raise ValueError("width, height, frames, and delay must be positive")
    heads = [random.randint(-height, 0) for _ in range(width)]
    chars = "0123456789ABCDEF"
    print("\n" * (height - 1))
    for _ in range(frames):
        grid = [[" " for _ in range(width)] for _ in range(height)]
        for col in range(width):
            head = heads[col]
            if 0 <= head < height:
                grid[head][col] = random.choice(chars)
            if 0 <= head - 1 < height:
                grid[head - 1][col] = "."
            heads[col] += 1
            if heads[col] > height + random.randint(2, 6):
                heads[col] = random.randint(-height, 0)
        move_cursor_home()
        sys.stdout.write("\n".join("".join(row) for row in grid))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def equalizer(bars: int = 16, height: int = 8, frames: int = 80, delay: float = 0.05, char: str = "#") -> None:
    """Random bar equalizer animation."""
    if bars <= 0 or height <= 0 or frames <= 0 or delay <= 0:
        raise ValueError("bars, height, frames, and delay must be positive")
    print("\n" * (height - 1))
    for _ in range(frames):
        bar_heights = [random.randint(1, height) for _ in range(bars)]
        lines = []
        for row in range(height, 0, -1):
            line = []
            for h in bar_heights:
                line.append(char if h >= row else " ")
            lines.append(" ".join(line))
        move_cursor_home()
        sys.stdout.write("\n".join(lines))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def fireworks(bursts: int = 4, size: int = 12, delay: float = 0.12, char: str = "*") -> None:
    """
    Radial fireworks bursts.

    Args:
        bursts: Number of bursts.
        size: Canvas size (square).
        delay: Delay between frames.
        char: Character used for sparkles.
    """
    if bursts <= 0 or size <= 2 or delay <= 0:
        raise ValueError("bursts must be positive, size > 2, delay positive")
    if len(char) != 1:
        raise ValueError("char must be a single character")
    center = size // 2
    print("\n" * (size - 1))
    for _ in range(bursts):
        for radius in range(1, center + 1):
            lines = []
            for row in range(size):
                line_chars = []
                for col in range(size):
                    dist = abs(row - center) + abs(col - center)
                    if dist == radius:
                        line_chars.append(char)
                    elif dist == radius - 1:
                        line_chars.append(".")
                    else:
                        line_chars.append(" ")
                lines.append("".join(line_chars))
            move_cursor_home()
            sys.stdout.write("\n".join(lines))
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def twinkle_stars(width: int = 40, height: int = 8, frames: int = 80, delay: float = 0.07, density: float = 0.15) -> None:
    """Starfield twinkling effect."""
    if width <= 0 or height <= 0 or frames <= 0 or delay <= 0:
        raise ValueError("width, height, frames, and delay must be positive")
    if not (0 <= density <= 1):
        raise ValueError("density must be between 0 and 1")
    print("\n" * (height - 1))
    for _ in range(frames):
        lines = []
        for _ in range(height):
            line_chars = []
            for _ in range(width):
                if random.random() < density:
                    line_chars.append(random.choice([".", "*", "+"]))
                else:
                    line_chars.append(" ")
            lines.append("".join(line_chars))
        move_cursor_home()
        sys.stdout.write("\n".join(lines))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def dna_helix(frames: int = 80, delay: float = 0.06) -> None:
    """Animate a simple ASCII DNA helix."""
    pattern = [
        ("  A   T  ", " /     \\ "),
        ("   A T   ", "  /   \\  "),
        ("    X    ", "   / \\   "),
        ("   T A   ", "  \\   /  "),
        ("  T   A  ", " \\     / "),
        ("   T A   ", "  \\   /  "),
        ("    X    ", "   \\ /   "),
        ("   A T   ", "  /   \\  "),
    ]
    if frames <= 0 or delay <= 0:
        raise ValueError("frames and delay must be positive")
    for i in range(frames):
        top, bottom = pattern[i % len(pattern)]
        sys.stdout.write("\r" + top + "\n" + bottom)
        sys.stdout.flush()
        time.sleep(delay)
        move_cursor_home()
    sys.stdout.write("\n")
    sys.stdout.flush()


def shooting_star(width: int = 40, height: int = 10, frames: int = 60, delay: float = 0.05, char: str = "*") -> None:
    """Diagonal shooting star animation."""
    if width <= 0 or height <= 0 or frames <= 0 or delay <= 0:
        raise ValueError("width, height, frames, and delay must be positive")
    print("\n" * (height - 1))
    for i in range(frames):
        x = min(width - 1, i)
        y = min(height - 1, i // 2)
        lines = []
        for row in range(height):
            line_chars = []
            for col in range(width):
                if (col, row) == (x, y):
                    line_chars.append(char)
                elif (col, row) == (x - 1, y - 1):
                    line_chars.append(".")
                elif (col, row) == (x - 2, y - 2):
                    line_chars.append(".")
                else:
                    line_chars.append(" ")
            lines.append("".join(line_chars))
        move_cursor_home()
        sys.stdout.write("\n".join(lines))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def rising_bar(width: int = 20, height: int = 8, frames: int = 60, delay: float = 0.05, char: str = "#") -> None:
    """Bar that rises and falls inside a frame."""
    if width <= 0 or height <= 0 or frames <= 0 or delay <= 0:
        raise ValueError("width, height, frames, and delay must be positive")
    print("\n" * (height - 1))
    for i in range(frames):
        level = int((math.sin(i / 6.0) + 1) * (height / 2))
        lines = []
        for row in range(height):
            if height - row <= level:
                lines.append(char * width)
            else:
                lines.append(" " * width)
        move_cursor_home()
        sys.stdout.write("\n".join(lines))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def orbit(radius: int = 6, frames: int = 100, delay: float = 0.05) -> None:
    """Orbiting dot around a center point."""
    diameter = radius * 2 + 1
    print("\n" * (diameter - 1))
    for i in range(frames):
        angle = (i / frames) * 2 * math.pi
        x = int(radius + radius * math.cos(angle))
        y = int(radius + radius * math.sin(angle))
        lines = []
        for row in range(diameter):
            line_chars = []
            for col in range(diameter):
                if (col, row) == (x, y):
                    line_chars.append("o")
                elif (col, row) == (radius, radius):
                    line_chars.append("+")
                else:
                    line_chars.append(" ")
            lines.append("".join(line_chars))
        move_cursor_home()
        sys.stdout.write("\n".join(lines))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def falling_sand(width: int = 30, height: int = 10, frames: int = 80, delay: float = 0.05, density: float = 0.2) -> None:
    """Simple falling sand simulation."""
    if not (0 <= density <= 1):
        raise ValueError("density must be between 0 and 1")
    if width <= 0 or height <= 0 or frames <= 0 or delay <= 0:
        raise ValueError("width, height, frames, and delay must be positive")
    grid = [[" " for _ in range(width)] for _ in range(height)]
    print("\n" * (height - 1))
    for _ in range(frames):
        # spawn new particles at the top row
        for col in range(width):
            if random.random() < density:
                grid[0][col] = "."
        # update falling
        for row in range(height - 2, -1, -1):
            for col in range(width):
                if grid[row][col] != " " and grid[row + 1][col] == " ":
                    grid[row + 1][col] = grid[row][col]
                    grid[row][col] = " "
        move_cursor_home()
        sys.stdout.write("\n".join("".join(line) for line in grid))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


def carousel(text: str = "Loading", frames: int = 80, delay: float = 0.08) -> None:
    """Rotating line characters beside text."""
    if frames <= 0 or delay <= 0:
        raise ValueError("frames and delay must be positive")
    frames_cycle = cycle(["-", "\\", "|", "/"])
    for _ in range(frames):
        sys.stdout.write("\r" + next(frames_cycle) + " " + text)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\r" + "[done] " + text + "   \n")
    sys.stdout.flush()
