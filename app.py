"""Tic Tac Toe Game Script."""

import sys

import pygame
from pygame.locals import QUIT

from utils.config import load_config
from utils.config import parse_config
from utils.setup import load_window_params
from utils.setup import load_colors
from utils.setup import build_window
from utils.setup import setup_game
from utils.display import update_window
from utils.minimax import check_win
from utils.minimax import get_ai_move
from utils.minimax import get_user_move
from utils.display import display_game_message


def run_game(config_file="config.ini"):
    """Main function.

    Runs the game from configuration file.

    Parameters
    ----------
    config_file : str
        The path to the configuration file.
    """

    # Load configuration
    config = load_config(config_file)
    config = parse_config(config)
    black, white, red, blue = load_colors(config)
    title = load_window_params(config)

    # Setup pygame window
    screen, text_header, text_paragraph = build_window(title, black)

    # Setup game
    grid, win, winner = setup_game()

    # AI goes first?
    grid = get_ai_move(grid)

    # Main loop
    while True:
        update_window(screen, text_header, text_paragraph, grid, white, black,
                      red, blue, win, winner)

        # Event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                grid, valid_click = get_user_move(screen, grid)

                # Check if game is over
                win, winner = check_win(grid)

                if winner:
                    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                    valid_click = False

                # If game is not over, get AI move
                if valid_click:
                    grid = get_ai_move(grid)

                    # Check if game is over
                    win, winner = check_win(grid)
                    if winner:
                        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)

        pygame.display.update()


if __name__ == "__main__":
    run_game()
