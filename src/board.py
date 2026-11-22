"""ASCII rendering for the tic-tac-toe board."""

BOARD_ROWS = 3
BOARD_COLUMNS = 3


def render_empty_board() -> str:
    """Return the empty 3x3 board as ASCII art."""
    divider = "+" + "---+" * BOARD_COLUMNS
    cell_row = "|" + "   |" * BOARD_COLUMNS

    lines = [divider]
    for _ in range(BOARD_ROWS):
        lines.append(cell_row)
        lines.append(divider)

    return "\n".join(lines)
