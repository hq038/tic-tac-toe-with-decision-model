"""Command-line interface for the application."""

from src.board import (
    BOARD_SIZE,
    Board,
    create_board,
    is_empty,
    is_full,
    place_mark,
    render_board,
    winner,
)
from src.decision import choose_move

PLAYERS = (("A", "X"), ("B", "O"))
AI_PLAYER = "B"


def parse_move(raw: str) -> tuple[int, int] | None:
    """Parse a '<column> <row>' move, returning None if it is invalid."""
    parts = raw.split()
    if len(parts) != 2:
        return None

    try:
        column, row = int(parts[0]), int(parts[1])
    except ValueError:
        return None

    if not (1 <= column <= BOARD_SIZE and 1 <= row <= BOARD_SIZE):
        return None

    return column, row


def prompt_move(board: Board, player_name: str) -> tuple[int, int]:
    """Prompt the player until an empty cell is chosen."""
    while True:
        move = parse_move(input(f"Player {player_name}, choose a cell (column row): "))
        if move is None:
            print("Invalid move. Enter a column and row from 1 to 3, e.g. '1 1'.")
            continue

        column, row = move
        if not is_empty(board, column, row):
            print("That cell is already taken. Choose another one.")
            continue

        return column, row


def main() -> int:
    """Run the application."""
    board = create_board()
    print(render_board(board))

    turn = 0
    while True:
        player_name, mark = PLAYERS[turn % len(PLAYERS)]

        if player_name == AI_PLAYER:
            move = choose_move(board, mark)
            if move is None:
                raise RuntimeError("The decision model did not return a move.")
        else:
            move = prompt_move(board, player_name)

        column, row = move
        place_mark(board, column, row, mark)
        print(render_board(board))

        winning_mark = winner(board)
        if winning_mark is not None:
            winner_name = next(name for name, player_mark in PLAYERS if player_mark == winning_mark)
            print(f"Player {winner_name} wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        turn += 1

    return 0
