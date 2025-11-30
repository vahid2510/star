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

All animations render frames directly to the terminal and return `None`. Sample parameters are tuned for quick previews—feel free to adjust `frames`, `delay`, or `duration`.

- `wave_text(text, amplitude=2, speed=0.08, cycles=2)`: Sine-wave horizontal motion.
- `bouncing_ball(width=20, height=5, frames=80, delay=0.05, char="o")`: 2D bouncing ball.
- `spinner(text="Loading", duration=2.0, interval=0.1)`: Classic spinner.
- `loading_bar(width=30, duration=2.0, char="#")`: Filling progress bar.
- `typing_text(text, interval=0.05, cursor="|")`: Typewriter effect.
- `blinking_text(text, blinks=6, interval=0.3)`: Blink on/off.
- `marquee(text, width=30, cycles=3, speed=0.05)`: Scrolling ticker window.
- `bouncing_text(text, width=30, frames=60, delay=0.05)`: Left/right bounce on one line.
- `pulse_text(text, min_spaces=0, max_spaces=6, cycles=6, delay=0.06)`: In/out pulsing via indentation.
- `snake_line(width=30, length=8, frames=100, delay=0.04, head="O", body="o")`: One-line snake.
- `progress_dots(text="Loading", dots=3, cycles=5, delay=0.3)`: Growing trailing dots.
- `countdown(seconds=5)`: Simple countdown timer.
- `ripple_line(width=40, frames=80, delay=0.04, char="*")`: Moving ripple on one line.
- `bar_wave(width=30, frames=80, delay=0.05, char="|")`: Equalizer-like moving bars on one line.
- `matrix_rain(width=40, height=12, frames=80, delay=0.05)`: Matrix-style falling glyphs.
- `equalizer(bars=16, height=8, frames=80, delay=0.05, char="#")`: Multi-line audio bars.
- `fireworks(bursts=4, size=12, delay=0.12, char="*")`: Radial fireworks bursts.
- `twinkle_stars(width=40, height=8, frames=80, delay=0.07, density=0.15)`: Twinkling starfield.
- `dna_helix(frames=80, delay=0.06)`: ASCII helix loop.
- `shooting_star(width=40, height=10, frames=60, delay=0.05, char="*")`: Diagonal shooting star with tail.
- `rising_bar(width=20, height=8, frames=60, delay=0.05, char="#")`: Rising/falling fill.
- `orbit(radius=6, frames=100, delay=0.05)`: Orbiting dot around a center.
- `falling_sand(width=30, height=10, frames=80, delay=0.05, density=0.2)`: Minimal sand simulation.
- `carousel(text="Loading", frames=80, delay=0.08)`: Rotating line beside text.

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
