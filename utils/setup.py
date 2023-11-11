"""Setup module for the game."""

import pygame

from utils.display import generate_text


def load_window_params(parsed_config):
    """Load the window parameters from configuration file.

    Parameters
    ----------
    parsed_config : dict
        A dictionary of parsed configuration values.

    Returns
    -------
    title : str
        The title of the window.
    """

    title = parsed_config["window"]["title"]

    return title


def load_colors(parsed_config):
    """Load the colors from configuration file.

    Parameters
    ----------
    parsed_config : dict
        A dictionary of parsed configuration values.

    Returns
    -------
    black : tuple
        The black color.
    white : tuple
        The white color.
    red : tuple
        The red color.
    blue : tuple
        The blue color.
    """

    red = parsed_config["colors"]["red"]
    blue = parsed_config["colors"]["blue"]
    white = parsed_config["colors"]["white"]
    black = parsed_config["colors"]["black"]

    return black, white, red, blue


def build_window(title, black):
    """Build the window."""

    # Setup pygame window
    pygame.init()
    screen = pygame.display.set_mode((480, 640))
    pygame.display.set_caption(title)

    # Colors, text & grid
    text_header, text_paragraph = generate_text(black)

    return screen, text_header, text_paragraph


def setup_game():
    """Setup the game.

    Returns
    -------
    grid : list
        The grid to draw.
    win : bool
        True if the game is won, False otherwise. In setup mode, always False.
    """

    # Setup game
    grid = [[None, None, None], [None, None, None], [None, None, None]]
    win = False
    winner = None

    return grid, win, winner
