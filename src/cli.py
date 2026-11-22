"""Command-line interface for the application."""

import argparse
from collections.abc import Sequence

from src import __version__
from src.board import render_empty_board

PROG = "tic-tac-toe"


def main(argv: Sequence[str] | None = None) -> int:
    """Run the application."""
    parser = argparse.ArgumentParser(
        prog=PROG,
        description="Tic-tac-toe game with an AI opponent.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.parse_args(argv)

    print(render_empty_board())
    return 0
