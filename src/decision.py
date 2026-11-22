"""OpenRouter-backed decision model for tic-tac-toe moves.

Set ``OPENROUTER_API_KEY`` (or ``TYPESAFE_API_KEY``) before playing.
"""

import os

from typesafe_sdk import Choice, TypeSafeClient

from src.board import BOARD_SIZE, Board, is_empty

BASE_URL = "https://openrouter.ai/api"
MODEL = "jev-latest"


def create_client() -> TypeSafeClient:
    """Return a TypeSafe client configured for OpenRouter's decision models."""
    return TypeSafeClient(
        api_key=os.environ.get("OPENROUTER_API_KEY") or None,
        base_url=BASE_URL,
        model=MODEL,
    )


def _cell_kind(column: int, row: int) -> str:
    """Describe a cell position as a hint for the decision model."""
    if column == 2 and row == 2:
        return "center"
    if column in (1, BOARD_SIZE) and row in (1, BOARD_SIZE):
        return "corner"
    return "side"


def choose_move(board: Board, mark: str) -> tuple[int, int] | None:
    """Ask the decision model for the 1-based cell to play, or None if full."""
    empty_cells = [
        (column, row)
        for row in range(1, BOARD_SIZE + 1)
        for column in range(1, BOARD_SIZE + 1)
        if is_empty(board, column, row)
    ]
    if not empty_cells:
        return None

    opponent = "O" if mark == "X" else "X"
    instructions = (
        f"You are playing tic-tac-toe as {mark} against {opponent}. "
        "Cells are addressed as '<column> <row>', both 1-based. "
        "The board is a list of rows from top to bottom, and each row lists cells "
        "from left to right. Choose the strongest legal move. "
        f"First, if {mark} can complete three in a row now, take that winning cell. "
        f"Otherwise, if {opponent} can complete three in a row on their next turn, "
        "block that cell. "
        "Otherwise prefer the center, then corners, then sides. "
        f"Avoid any move that lets {opponent} create two winning threats (a fork) at once. "
        "Among safe moves, prefer the one that creates the most winning threats for you."
    )

    with create_client() as client:
        response = client.system_one(
            state={
                "board": board,
                "you": mark,
                "opponent": opponent,
                "empty_cells": [f"{column} {row}" for column, row in empty_cells],
            },
            questions={
                "move": Choice(
                    instructions=instructions,
                    criteria={
                        f"{column} {row}": _cell_kind(column, row) for column, row in empty_cells
                    },
                )
            },
        )

    column_text, row_text = response.choices["move"].choice.split()
    return int(column_text), int(row_text)
