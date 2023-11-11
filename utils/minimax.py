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

    # TODO: Generate strategy to find an available cell
    # Must return a pair of coordinates (x, y)

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

    # TODO: Implement minimax algorithm to get the best move
    # Hint: Use the minimax function over all available cells to
    # determine the best move for the AI

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

    # TODO: Check if the game is a tie
    # Hint: The only possible way is having all occupied cells but no win

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

    # TODO: Check rows

    # TODO: Check columns

    # TODO: Check diagonals

    # TODO: Check tie

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

    # TODO: Check base case
    # Hint: Check if the game is a won, a lose or a tie
    # Report value 1, -1 or 0 respectively

    # TODO: Recursive case
    # Hint: Start with "X" and maximize, then minimize for "O"
    # Do not forget to return the cells to their original values
    if player == "X":
        pass
    else:
        pass
