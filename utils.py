import math

import pygame


def generate_text(color):
    """Generate text to display on the screen.
    
    Parameters
    ----------
    color : tuple
        The color of the text.
    """

    font_header = pygame.font.SysFont(None, 48)
    font_text = pygame.font.SysFont(None, 24)

    text_header = font_header.render('Tic-Tac-Toe', True, color)
    text_paragraph = font_text.render('A.I. goes first.', True, color)

    return text_header, text_paragraph


def display_text(screen, text_header, text_paragraph):
    """Display text on the screen.
    
    Parameters
    ----------
    screen : pygame.Surface
        The screen to draw on.
    text_header : pygame.Surface
        The header text to display.
    text_paragraph : pygame.Surface
        The paragraph text to display.
    """

    width = screen.get_width()
    screen.blit(text_header, (width // 2 - text_header.get_width() // 2,
                              20 + text_header.get_height() // 2))
    screen.blit(text_paragraph, (width // 2 - text_paragraph.get_width() // 2,
                                 80 + text_paragraph.get_height() // 2))


def draw_grid(screen, color):
    """Draw the grid on the screen.

    Parameters
    ----------
    screen : pygame.Surface
        The screen to draw on.
    color : tuple
        The color of the grid.
    """

    width, height = screen.get_size()
    pygame.draw.line(screen, color, (width // 3, 150), (width // 3, height), 5)
    pygame.draw.line(screen, color, (width // 3 * 2, 150),
                     (width // 3 * 2, height), 5)
    pygame.draw.line(screen, color, (0, height // 3 + 100),
                     (width, height // 3 + 100), 5)
    pygame.draw.line(screen, color, (0, height // 3 * 2 + 50),
                     (width, height // 3 * 2 + 50), 5)


def draw_cross(screen, x, y, color):
    """Draw a cross on the screen.

    Parameters
    ----------
    x : int
        The x coordinate of the cross.
    y : int
        The y coordinate of the cross.
    color : tuple
        The color of the cross.
    """

    pygame.draw.line(screen, color, (x - 50, y - 50), (x + 50, y + 50), 8)
    pygame.draw.line(screen, color, (x - 50, y + 50), (x + 50, y - 50), 8)


def draw_circle(screen, x, y, color):
    """Draw a circle on the screen.

    Parameters
    ----------
    x : int
        The x coordinate of the circle.
    y : int
        The y coordinate of the circle.
    color : tuple
        The color of the circle.
    """

    pygame.draw.circle(screen, color, (x, y), 50, 8)


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


def draw_game(screen, grid, color_A, color_B):
    """Draw the game on the screen.
    
    Parameters
    ----------
    screen : pygame.Surface
        The screen to draw on.
    grid : list
        The grid to draw.
    color_A : tuple
        The color of the first player.
    color_B : tuple
        The color of the second player.
    """

    width = screen.get_width()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'X':
                draw_cross(screen, (2 * j + 1) * width // 6,
                           (2 * i + 1) * width // 6 + 150, color_A)
            elif cell == 'O':
                draw_circle(screen, (2 * j + 1) * width // 6,
                            (2 * i + 1) * width // 6 + 150, color_B)


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
        if pos_x < width // 3: i = 0
        elif pos_x < width // 3 * 2: i = 1
        else: i = 2

        # Verify y position
        j = -1
        if 100 < pos_y < height // 3 + 100: j = 0
        elif 100 < pos_y < height // 3 * 2 + 50: j = 1
        elif 100 < pos_y: j = 2

        if j == -1: return updated_grid, False

        # Check if the position is available and draw the 'O'
        if updated_grid[j][i] is None:
            updated_grid[j][i] = 'O'

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
                updated_grid[i][j] = 'X'
                score = minimax(updated_grid, 0, 'O')
                updated_grid[i][j] = None

                if score < best_score:
                    best_score = score
                    best_move = (i, j)

    updated_grid[best_move[0]][best_move[1]] = 'X'

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
        return False, 'tie'

    return False, None


def display_game_message(screen, win, winner, white, color_A, color_B, black):
    """Display the game message.
    
    Parameters
    ----------
    screen : pygame.Surface
        The screen to draw on.
    """

    width, height = screen.get_size()

    if win:
        # Display message
        font = pygame.font.SysFont(None, 48)
        if winner == 'X':
            text = font.render('You lose!', True, white, color_A)
        else:
            text = font.render('You win!', True, white, color_B)
        screen.blit(text, (width // 2 - text.get_width() // 2,
                           height // 2 - text.get_height() // 2))
    if winner == 'tie':
        # Display message
        font = pygame.font.SysFont(None, 48)
        text = font.render('Tie!', True, white, black)
        screen.blit(text, (width // 2 - text.get_width() // 2,
                           height // 2 - text.get_height() // 2))


def minimax(grid, depth, player):
    # Base case
    win, winner = check_win(grid)
    if win:
        if winner == 'X': return -1
        if winner == 'O': return 1
    if winner == 'tie': return 0

    # Recursive case
    if player == 'X':
        best_score = math.inf

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell is None:
                    grid[i][j] = 'X'
                    score = minimax(grid, depth + 1, 'O')
                    grid[i][j] = None
                    best_score = min(score, best_score)

        return best_score
    else:
        best_score = -math.inf

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell is None:
                    grid[i][j] = 'O'
                    score = minimax(grid, depth + 1, 'X')
                    grid[i][j] = None
                    best_score = max(score, best_score)

        return best_score