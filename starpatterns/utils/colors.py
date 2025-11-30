"""ANSI color formatting helpers."""

from typing import Optional

# Basic ANSI color codes
_COLOR_MAP = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}


def colorize(
    text: str,
    fg: Optional[str] = None,
    bg: Optional[str] = None,
    bold: bool = False,
    underline: bool = False,
) -> str:
    """
    Apply ANSI color codes to text.

    Args:
        text: String to format.
        fg: Foreground color name.
        bg: Background color name.
        bold: Enable bold style.
        underline: Enable underline style.
    """
    codes = []
    if fg:
        if fg not in _COLOR_MAP:
            raise ValueError(f"Unsupported foreground color: {fg}")
        codes.append(str(_COLOR_MAP[fg]))
    if bg:
        if bg not in _COLOR_MAP:
            raise ValueError(f"Unsupported background color: {bg}")
        codes.append(str(_COLOR_MAP[bg] + 10))  # Background codes offset by 10
    if bold:
        codes.append("1")
    if underline:
        codes.append("4")
    if not codes:
        return text
    prefix = "\033[" + ";".join(codes) + "m"
    suffix = "\033[0m"
    return f"{prefix}{text}{suffix}"


def rgb(text: str, r: int, g: int, b: int) -> str:
    """
    Apply true-color (24-bit) ANSI foreground to text.

    Args:
        text: String to format.
        r: Red channel (0-255).
        g: Green channel (0-255).
        b: Blue channel (0-255).
    """
    for channel, name in zip((r, g, b), "rgb"):
        if not (0 <= channel <= 255):
            raise ValueError(f"{name} must be between 0 and 255")
    prefix = f"\033[38;2;{r};{g};{b}m"
    suffix = "\033[0m"
    return f"{prefix}{text}{suffix}"
