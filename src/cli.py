"""Command-line interface for the application."""

from src.board import BOARD_SIZE, create_board, is_empty, place_mark, render_board


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


def main() -> int:
    """Run the application."""
    board = create_board()
    print(render_board(board))

    while True:
        move = parse_move(input("Player A, choose a cell (column row): "))
        if move is None:
            print("Invalid move. Enter a column and row from 1 to 3, e.g. '1 1'.")
            continue

        column, row = move
        if not is_empty(board, column, row):
            print("That cell is already taken. Choose another one.")
            continue

        place_mark(board, column, row, "X")
        break

    print(render_board(board))
    return 0
