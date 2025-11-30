"""Command-line entrypoint for `python -m starpatterns`."""

from .demos.examples import run_all


def main() -> None:
    """Run the interactive showcase."""
    run_all()


if __name__ == "__main__":
    main()
