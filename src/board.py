"""ASCII rendering for the tic-tac-toe board."""

BOARD_SIZE = 3
EMPTY_CELL = "   "
ROW_DIVIDER = "---+---+---"


def render_empty_board() -> str:
    """Return the empty 3x3 board as ASCII art."""
    cell_row = "|".join([EMPTY_CELL] * BOARD_SIZE)

    lines = []
    for row_index in range(BOARD_SIZE):
        lines.append(cell_row)
        if row_index < BOARD_SIZE - 1:
            lines.append(ROW_DIVIDER)

    return "\n".join(lines)
