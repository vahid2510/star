# Usage Guide

This document describes every public function in the `starpatterns` package.

## Installation

```bash
pip install starpatterns
```

## Package Entry Point

`starpatterns/__init__.py` re-exports the most common utilities:
- `triangle`, `square`, `diamond`
- `hollow_square`, `cross`, `hourglass`
- `sierpinski`
- `wave_text`, `bouncing_ball`, `spinner`
- `colorize`, `rgb`
- `clear_terminal`

Importing via `from starpatterns import triangle` pulls directly from these aliases.

## Basic Patterns (`starpatterns.patterns.basic`)

### `triangle(height: int, char: str = "*") -> str`
Creates a left-aligned triangle. `height` must be positive; `char` must be a single character.

### `square(size: int, char: str = "*") -> str`
Creates a filled square with equal width and height. `size` must be positive; `char` must be a single character.

### `diamond(size: int, char: str = "*") -> str`
Creates a centered diamond. `size` must be odd and positive; `char` must be a single character.

## Advanced Patterns (`starpatterns.patterns.advanced`)

### `hollow_square(size: int, border_char: str = "*") -> str`
Creates a square outline. `size` must be positive; `border_char` must be a single character.

### `cross(size: int, char: str = "*", fill: str = " ") -> str`
Creates a plus-shaped cross. `size` must be an odd positive integer. Both `char` and `fill` must be single characters.

### `hourglass(size: int, char: str = "*") -> str`
Creates an hourglass figure. `size` must be odd and positive; `char` must be a single character.

## Fractal Patterns (`starpatterns.patterns.fractal`)

### `sierpinski(order: int, char: str = "*") -> str`
Generates a Sierpinski triangle at the given recursion `order` (0 or greater) using the provided drawing character.

## Animations (`starpatterns.patterns.animation`)

All animations render frames directly to the terminal and return `None`.

### `wave_text(text: str, amplitude: int = 2, speed: float = 0.08, cycles: int = 2) -> None`
Animates the text along a horizontal sine wave. `amplitude` controls indentation; `speed` controls frame delay; `cycles` sets how many sine waves to render.

### `bouncing_ball(width: int = 20, height: int = 5, frames: int = 80, delay: float = 0.05, char: str = "o") -> None`
Animates a single character bouncing within a rectangular field. `width`/`height` set the bounds; `frames` controls total steps; `delay` sets the pause between frames; `char` picks the ball symbol.

### `spinner(text: str = "Loading", duration: float = 2.0, interval: float = 0.1) -> None`
Displays a classic CLI spinner beside the provided text. `duration` sets total runtime; `interval` sets the frame rate.

## Utilities (`starpatterns.utils`)

### `clear_terminal() -> None`
Clears the terminal screen using `cls` on Windows and `clear` elsewhere.

### `move_cursor_home() -> None`
Moves the cursor to the top-left corner without clearing the screen. Handy for redrawing animations.

### `colorize(text: str, fg: Optional[str] = None, bg: Optional[str] = None, bold: bool = False, underline: bool = False) -> str`
Wraps text with ANSI styling codes. Valid colors: `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`.

### `rgb(text: str, r: int, g: int, b: int) -> str`
Applies 24-bit color to text using RGB values in the 0–255 range.

## Demos (`starpatterns.demos.examples`)

- `starpatterns.demos.examples.run_all()` clears the terminal, چاپ الگوها و رنگ‌ها و همه انیمیشن‌ها را اجرا می‌کند.
- `starpatterns.demos.all_examples.main()` یک دمو جامع‌تر است که روی انیمیشن‌ها تاکید دارد.

Run the demo directly:

```bash
python -m starpatterns.demos.examples
# یا
python -m starpatterns.demos.all_examples
```
