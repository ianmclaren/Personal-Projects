import pygame, sys
import numpy as np
pygame.init()

#Setting important board characteristics
WIDTH = 450
HEIGHT = 450
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3

CIRCLE_RADIUS = 45
CIRCLE_WIDTH = 15

CROSS_WIDTH = 25
CROSS_SPACE = 40

#Creating colours for board
BACKGROUND_COLOUR = (181, 100, 227)
LINE_COLOUR = (153, 0, 153)
FIGURE_COLOUR = (255, 255, 255)

#Setting up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill( BACKGROUND_COLOUR )
pygame.display.set_caption("Tic-Tac-Toe")

#Setting up board functionality
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

#This draws the four lines to make up the grid
def draw_lines():
    pygame.draw.line( screen, LINE_COLOUR, (0, 150), (450, 150), LINE_WIDTH)
    pygame.draw.line( screen, LINE_COLOUR, (0, 300), (450, 300), LINE_WIDTH) 
    pygame.draw.line( screen, LINE_COLOUR, (150, 0), (150, 450), LINE_WIDTH)
    pygame.draw.line( screen, LINE_COLOUR, (300, 0), (300, 450), LINE_WIDTH)

#calling the function to draw the lines
draw_lines()

#Places the current player into the square
def mark_square(row, col, player):
    board[row][col] = player

#Checks if square is unpicked
def is_square_available(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, FIGURE_COLOUR, (col * 150 + CROSS_SPACE, row * 150 + 150 - CROSS_SPACE), (col * 150 + 150 - CROSS_SPACE, row * 150 + CROSS_SPACE), CROSS_WIDTH) 
                pygame.draw.line(screen, FIGURE_COLOUR, (col * 150 + CROSS_SPACE, row * 150 + CROSS_SPACE), (col * 150 + 150 - CROSS_SPACE, row * 150 + 150 - CROSS_SPACE), CROSS_WIDTH) 
            elif board[row][col] == 2:
                pygame.draw.circle(screen, FIGURE_COLOUR, (int(col * 150 + 75), int(row * 150 + 75)), CIRCLE_RADIUS, CIRCLE_WIDTH)



#Checks if board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if(is_square_available(row, col) == True):
                return False
    return True    

def check_win(player):
    #Vertical check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col)
            return True

    #Horizontal check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row)
            return True

    #Diagonal Descending check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal_winning_line()

    #Diagonal Ascending check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal_winning_line()

def draw_vertical_winning_line(col):
    positionX = col * 150 + 75

    pygame.draw.line(screen, FIGURE_COLOUR, (positionX, 15), (positionX, HEIGHT - 15), 15)

def draw_horizontal_winning_line(row):
    positionY = row * 150 + 75

    pygame.draw.line(screen, FIGURE_COLOUR, (15, positionY), (WIDTH - 15, positionY), 15)

def draw_asc_diagonal_winning_line():
    pygame.draw.line(screen, FIGURE_COLOUR, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_desc_diagonal_winning_line():
    pygame.draw.line(screen, FIGURE_COLOUR, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart_game():
    screen.fill(BACKGROUND_COLOUR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

player = 1
game_over = False

#mainloop for pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #If a player clicks the screen
        if event.type == pygame.MOUSEBUTTONDOWN:


            mouseX = event.pos[0] #Gives the x-coord of the click
            mouseY = event.pos[1] #Gives the y-coord of click
            
            #Rounds value down to be 0, 1, or 2
            clicked_row = int(mouseY // 150)
            clicked_col = int(mouseX // 150)

            if is_square_available(clicked_row, clicked_col) and not game_over:
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False

    pygame.display.update()




