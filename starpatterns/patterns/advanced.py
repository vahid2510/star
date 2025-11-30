"""Advanced ASCII patterns."""

from typing import List

from .basic import _validate_size


def hollow_square(size: int, border_char: str = "*") -> str:
    """
    Build a hollow square with a solid border.

    Args:
        size: Width/height of the square.
        border_char: Character used for the border.
    """
    _validate_size(size)
    if len(border_char) != 1:
        raise ValueError("border_char must be a single character")
    if size == 1:
        return border_char
    top_bottom = border_char * size
    middle = border_char + " " * (size - 2) + border_char
    lines = [top_bottom] + [middle for _ in range(size - 2)] + [top_bottom]
    return "\n".join(lines)


def cross(size: int, char: str = "*", fill: str = " ") -> str:
    """
    Build a centered cross. Size should be an odd integer for symmetry.

    Args:
        size: Width/height of the cross.
        char: Character used for the cross arms.
        fill: Background fill character.
    """
    _validate_size(size)
    if size % 2 == 0:
        raise ValueError("size must be odd for a symmetric cross")
    if len(char) != 1 or len(fill) != 1:
        raise ValueError("char and fill must be single characters")
    mid = size // 2
    lines: List[str] = []
    for row in range(size):
        line_chars: List[str] = []
        for col in range(size):
            if row == mid or col == mid:
                line_chars.append(char)
            else:
                line_chars.append(fill)
        lines.append("".join(line_chars))
    return "\n".join(lines)


def hourglass(size: int, char: str = "*") -> str:
    """
    Build an hourglass pattern.

    Args:
        size: Height/width of the hourglass (must be odd).
        char: Character used to draw the hourglass.
    """
    _validate_size(size)
    if size % 2 == 0:
        raise ValueError("size must be odd for a symmetric hourglass")
    if len(char) != 1:
        raise ValueError("char must be a single character")
    mid = size // 2
    lines: List[str] = []
    for i in range(size):
        offset = i if i <= mid else size - i - 1
        inner = char * (size - 2 * offset)
        lines.append(" " * offset + inner + " " * offset)
    return "\n".join(lines)
