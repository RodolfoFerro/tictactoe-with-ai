import sys

import pygame
from pygame.locals import QUIT

from utils import generate_text
from utils import display_text
from utils import draw_grid
from utils import draw_game
from utils import check_win
from utils import get_ai_move
from utils import get_user_move
from utils import display_game_message

# Setup
width = 480
height = 640
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic-Tac-Toe')

# Colors, text & grid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (66, 135, 245)
RED = (245, 66, 93)

text_header, text_paragraph = generate_text(BLACK)
grid = [[None, None, None], [None, None, None], [None, None, None]]

# AI goes first
win = False
grid = get_ai_move(grid)

# Main loop
while True:
    screen.fill(WHITE)
    display_text(screen, text_header, text_paragraph)
    draw_grid(screen, BLACK)
    draw_game(screen, grid, RED, BLUE)

    win, winner = check_win(grid)
    display_game_message(screen, win, winner, WHITE, RED, BLUE, BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid, valid_click = get_user_move(screen, grid)
            if valid_click:
                grid = get_ai_move(grid)

    pygame.display.update()
