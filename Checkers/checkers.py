import pygame
import numpy as np

pygame.init()

# Globals
BOARD_SIZE = 640
SQUARE_SIZE = BOARD_SIZE / 8
ROWS = 8
COLUMNS = 8

# Colours
BACKGROUND_COLOUR = (66, 66, 255)
SQUARE_COLOUR = (0, 0, 0)
PLAYER_ONE_COLOUR = (255, 66, 66)
PLAYER_TWO_COLOUR = (255, 255, 66)

# Setting up pygame display
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
screen.fill(BACKGROUND_COLOUR)
pygame.display.set_caption("Checkers")

board = np.zeros((ROWS, COLUMNS))

# Display the squares of the board
def display_board():
    for row in range(ROWS):
        for col in range(COLUMNS):
            # Draw a square over the background colour in an alternating pattern
            if (row + col) % 2 == 0: 
                pygame.draw.rect(screen, SQUARE_COLOUR, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
display_board()
pygame.display.update()