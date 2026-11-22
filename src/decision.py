"""OpenRouter-backed decision model for tic-tac-toe moves.

This module is ready to use but is not wired into the game loop yet.
Set ``OPENROUTER_API_KEY`` (or ``TYPESAFE_API_KEY``) before calling it.
"""

import os

from typesafe_sdk import Choice, TypeSafeClient

from src.board import BOARD_SIZE, Board, is_empty, render_board

BASE_URL = "https://openrouter.ai/api"
MODEL = "jev-latest"


def create_client() -> TypeSafeClient:
    """Return a TypeSafe client configured for OpenRouter's decision models."""
    return TypeSafeClient(
        api_key=os.environ.get("OPENROUTER_API_KEY") or None,
        base_url=BASE_URL,
        model=MODEL,
    )


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

    with create_client() as client:
        response = client.system_one(
            state=f"Player {mark} is to move.\n{render_board(board)}",
            questions={
                "move": Choice(
                    instructions=f"Which empty cell should player {mark} play?",
                    criteria={f"{column} {row}": None for column, row in empty_cells},
                )
            },
        )

    column_text, row_text = response.choices["move"].choice.split()
    return int(column_text), int(row_text)
