"""Minimax algorithm for the game of Tic-Tac-Toe."""

import math

import pygame


def find_available(grid):
    """Find the first available cell in the grid.

    Parameters
    ----------
    grid : list
        The grid to search.

    Returns
    -------
    tuple
        The coordinates of the first available cell.
    """

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell is None:
                return i, j

    return None


def get_user_move(screen, grid):
    """Get the move from the user.

    Parameters
    ----------
    screen : pygame.Surface
        The screen to draw on.
    grid : list
        The grid to draw.

    Returns
    -------
    updated_grid : list
        The updated grid.
    """

    width, height = screen.get_size()
    updated_grid = grid.copy()

    pos_x, pos_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        # Verify x position
        if pos_x < width // 3:
            i = 0
        elif pos_x < (width // 3) * 2:
            i = 1
        else:
            i = 2

        # Verify y position
        j = -1
        if 100 < pos_y < (height // 3) + 100:
            j = 0
        elif 100 < pos_y < (height // 3) * 2 + 50:
            j = 1
        elif 100 < pos_y:
            j = 2

        if j == -1:
            return updated_grid, False

        # Check if the position is available and draw the 'O'
        if updated_grid[j][i] is None:
            updated_grid[j][i] = "O"

    return updated_grid, True


def get_ai_move(grid):
    """Get the move from the A.I.

    Parameters
    ----------
    grid : list
        The grid to draw.

    Returns
    -------
    updated_grid : list
        The updated grid.
    """

    updated_grid = grid.copy()

    best_score = math.inf
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell is None:
                updated_grid[i][j] = "X"
                score = minimax(updated_grid, 0, "O")
                updated_grid[i][j] = None

                if score < best_score:
                    best_score = score
                    best_move = (i, j)

    updated_grid[best_move[0]][best_move[1]] = "X"

    return updated_grid


def check_tie(grid):
    """Check if the game is a tie.

    Parameters
    ----------
    grid : list
        The grid to draw.

    Returns
    -------
    bool
        True if the game is a tie, False otherwise.
    """

    for row in grid:
        for cell in row:
            if cell is None:
                return False

    return True


def check_win(grid):
    """Check if the game is won.

    Parameters
    ----------
    grid : list
        The grid to draw.

    Returns
    -------
    bool
        True if the game is won, False otherwise.
    player : str or None or 'tie'
        The player who won the game.
    """

    # Check rows
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return True, row[0]

    # Check columns
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] is not None:
            return True, grid[0][i]

    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] is not None:
        return True, grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] is not None:
        return True, grid[0][2]

    # Check tie
    if check_tie(grid):
        return False, "tie"

    return False, None


def minimax(grid, depth, player):
    """The minimax algorithm.

    Parameters
    ----------
    grid : list
        The grid to draw.
    depth : int
        The depth of the search.
    player : str
        The player to check.

    Returns
    -------
    int
        The score of the move.
    """

    # Base case
    win, winner = check_win(grid)
    if win:
        if winner == "X":
            return -1
        if winner == "O":
            return 1
    if winner == "tie":
        return 0

    # Recursive case
    if player == "X":
        best_score = math.inf

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell is None:
                    grid[i][j] = "X"
                    score = minimax(grid, depth + 1, "O")
                    grid[i][j] = None
                    best_score = min(score, best_score)

        return best_score
    else:
        best_score = -math.inf

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell is None:
                    grid[i][j] = "O"
                    score = minimax(grid, depth + 1, "X")
                    grid[i][j] = None
                    best_score = max(score, best_score)

        return best_score
