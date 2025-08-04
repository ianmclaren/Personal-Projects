import pygame
import numpy as np

pygame.init()

# BOARD

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
board = [[1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [2, 0, 2, 0, 2, 0, 2, 0],
         [0, 2, 0, 2, 0, 2, 0, 2]]

# Display the squares of the board
def display_board():
    for row in range(ROWS):
        for col in range(COLUMNS):
            # Draw a square over the background colour in an alternating pattern
            if (row + col) % 2 == 0: 
                pygame.draw.rect(screen, SQUARE_COLOUR, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[col][row] == 1:
                pygame.draw.circle(screen, PLAYER_ONE_COLOUR, (((row + 0.5) * SQUARE_SIZE), ((col + 0.5) * SQUARE_SIZE)), SQUARE_SIZE / 3)
            if board[col][row] == 2:
                pygame.draw.circle(screen, PLAYER_TWO_COLOUR, (((row + 0.5) * SQUARE_SIZE), ((col + 0.5) * SQUARE_SIZE)), SQUARE_SIZE / 3)
display_board()
pygame.display.update()

# GAME
PLAYER_TURN = 1

# Switch the player turn
def end_turn():
    global PLAYER_TURN
    if PLAYER_TURN is 1:
        PLAYER_TURN = 2
    elif PLAYER_TURN is 2:
        PLAYER_TURN = 1

run = True
#Main game loop
while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #User clicks square
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = np.floor(np.array(pos) / SQUARE_SIZE).astype(int)
                print(f"Column: {col}, Row: {row}")

                #TODO:Verification
                if board[col][row] == PLAYER_TURN:
                    print("Valid move")
                    continue
                else:
                    print("Not a piece")
                

    #print(PLAYER_TURN)
    end_turn()

