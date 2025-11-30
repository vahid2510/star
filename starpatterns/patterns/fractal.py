"""Fractal patterns such as the Sierpinski triangle."""

from typing import List


def sierpinski(order: int, char: str = "*") -> str:
    """
    Generate a Sierpinski triangle using recursive expansion.

    Args:
        order: Recursion depth (0 yields a single character).
        char: Character used to render the triangle.
    """
    if not isinstance(order, int):
        raise TypeError("order must be an integer")
    if order < 0:
        raise ValueError("order must be non-negative")
    if len(char) != 1:
        raise ValueError("char must be a single character")

    lines: List[str] = [char]
    # Each iteration doubles the width and height while inserting spacing.
    for level in range(order):
        spacing = " " * (2 ** level)
        top = [spacing + line + spacing for line in lines]
        bottom = [line + " " + line for line in lines]
        lines = top + bottom
    return "\n".join(lines)
