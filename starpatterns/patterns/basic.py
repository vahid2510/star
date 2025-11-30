"""Basic ASCII patterns."""

from typing import List


def _validate_size(size: int) -> int:
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be positive")
    return size


def triangle(height: int, char: str = "*") -> str:
    """
    Build a left-aligned triangle.

    Args:
        height: Number of rows in the triangle.
        char: Single character used to draw the triangle.
    """
    _validate_size(height)
    if len(char) != 1:
        raise ValueError("char must be a single character")
    lines: List[str] = []
    for i in range(1, height + 1):
        lines.append(char * i)
    return "\n".join(lines)


def square(size: int, char: str = "*") -> str:
    """
    Build a filled square.

    Args:
        size: Width and height of the square.
        char: Single character used to draw the square.
    """
    _validate_size(size)
    if len(char) != 1:
        raise ValueError("char must be a single character")
    line = char * size
    return "\n".join(line for _ in range(size))


def diamond(size: int, char: str = "*") -> str:
    """
    Build a centered diamond. Size must be an odd integer.

    Args:
        size: Width/height of the diamond (must be odd).
        char: Single character used to draw the diamond.
    """
    _validate_size(size)
    if size % 2 == 0:
        raise ValueError("size must be odd for a symmetric diamond")
    if len(char) != 1:
        raise ValueError("char must be a single character")

    mid = size // 2
    lines: List[str] = []
    for i in range(size):
        distance = abs(mid - i)
        fill = char * (size - 2 * distance)
        lines.append(" " * distance + fill + " " * distance)
    return "\n".join(lines)
