"""Terminal helpers for clearing and cursor control."""

import os
import sys


def clear_terminal() -> None:
    """Clear the terminal screen on Windows and Unix-like systems."""
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)


def move_cursor_home() -> None:
    """
    Move the cursor to the top-left corner without clearing the screen.
    Useful for redrawing animations without flicker.
    """
    sys.stdout.write("\033[H")
    sys.stdout.flush()
