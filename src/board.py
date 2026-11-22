"""Board state and ASCII rendering for tic-tac-toe."""

BOARD_SIZE = 3
EMPTY_CELL = " "
ROW_DIVIDER = "---+---+---"

Board = list[list[str]]


def create_board() -> Board:
    """Return an empty 3x3 board."""
    return [[EMPTY_CELL] * BOARD_SIZE for _ in range(BOARD_SIZE)]


def is_empty(board: Board, column: int, row: int) -> bool:
    """Return whether the 1-based cell is empty."""
    return board[row - 1][column - 1] == EMPTY_CELL


def place_mark(board: Board, column: int, row: int, mark: str) -> None:
    """Place a mark on the 1-based cell."""
    board[row - 1][column - 1] = mark


def render_board(board: Board) -> str:
    """Return the board as ASCII art."""
    lines = []
    for row_index, row in enumerate(board):
        lines.append("|".join(f" {cell} " for cell in row))
        if row_index < len(board) - 1:
            lines.append(ROW_DIVIDER)

    return "\n".join(lines)
