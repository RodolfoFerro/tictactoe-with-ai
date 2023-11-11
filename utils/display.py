"""Display utilities."""

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

    text_header = font_header.render("Tic-Tac-Toe", True, color)
    text_paragraph = font_text.render("A.I. goes first.", True, color)

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
    screen.blit(
        text_header,
        (width // 2 - text_header.get_width() // 2,
         20 + text_header.get_height() // 2),
    )
    screen.blit(
        text_paragraph,
        (
            width // 2 - text_paragraph.get_width() // 2,
            80 + text_paragraph.get_height() // 2,
        ),
    )


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


def draw_game(screen, grid, color_a, color_b):
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
            if cell == "X":
                draw_cross(
                    screen,
                    (2 * j + 1) * width // 6,
                    (2 * i + 1) * width // 6 + 150,
                    color_a,
                )
            elif cell == "O":
                draw_circle(
                    screen,
                    (2 * j + 1) * width // 6,
                    (2 * i + 1) * width // 6 + 150,
                    color_b,
                )


def update_window(screen, text_header, text_paragraph, grid, white, black, red,
                  blue, win, winner):
    """Update the window."""

    screen.fill(white)
    display_text(screen, text_header, text_paragraph)
    draw_grid(screen, black)
    draw_game(screen, grid, red, blue)

    display_game_message(screen, win, winner, white, red, blue, black)


def display_game_message(screen, win, winner, white, color_a, color_b, black):
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
        if winner == "X":
            text = font.render("You lose!", True, white, color_a)
        else:
            text = font.render("You win!", True, white, color_b)
        screen.blit(
            text,
            (width // 2 - text.get_width() // 2,
             height // 2 - text.get_height() // 2),
        )

    if winner == "tie":
        # Display message
        font = pygame.font.SysFont(None, 48)
        text = font.render("Tie!", True, white, black)
        screen.blit(
            text,
            (width // 2 - text.get_width() // 2,
             height // 2 - text.get_height() // 2),
        )
