import pygame, sys
import numpy as np
pygame.init()

#Setting board characteristics
WIDTH = 560
HEIGHT = 480
ROWS = 6
COLS = 7

CIRCLE_RADIUS = 30

#Creating colours
BACKGROUND_COLOUR = (66, 66, 255)
PLAYER_ONE_COLOUR = (255, 66, 66)
PLAYER_TWO_COLOUR = (255, 255, 66)
WIN_COLOUR = (255, 255, 255)
EMPTY_COLOUR = (0, 0, 0)

#Setting up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill( BACKGROUND_COLOUR )
pygame.display.set_caption("Connect-4")

board = np.zeros( (ROWS, COLS) )

def display_board():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                #make empty circle
                pygame.draw.circle(screen, EMPTY_COLOUR, (int(col * 80 + 40), int(row * 80 + 40)), CIRCLE_RADIUS, 0)
            elif board[row][col] == 1:
                #make red circle
                pygame.draw.circle(screen, PLAYER_ONE_COLOUR, (int(col * 80 + 40), int(row * 80 + 40)), CIRCLE_RADIUS, 0)
            elif board[row][col] == 2:
                #make yellow circle
                pygame.draw.circle(screen, PLAYER_TWO_COLOUR, (int(col * 80 + 40), int(row * 80 + 40)), CIRCLE_RADIUS, 0)
            elif board[row][col] == 3:
                #make white circle to show win
                pygame.draw.circle(screen, WIN_COLOUR, (int(col * 80 + 40), int(row * 80 + 40)), CIRCLE_RADIUS, 0)
display_board()

def is_col_full(col):
    if board[0][col] == 0:
        return False
    else:
        return True

def place_piece(col, player):
    for y in range(5, -1, -1):
        if(board[y][col] == 0):
            board[y][col] = player
            return

def check_win(player):
    if check_horiz(player, board) == True or check_vert(player, board) == True or check_diag(player, board) == True:
        return True
    else:
        return False


def check_horiz(player, board):
    #for each column (Only the first 4 columns can start a horizontal win)
    for col in range(4):
        for row in range(6):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                startpoint = (col * 80 + 40, row * 80 + 40)
                endpoint = ((col + 3) * 80 + 40, row * 80 + 40)
                draw_winning_line(startpoint, endpoint, player)
                return True
    return False

def check_vert(player, board):
    #for each column (Only the first 4 columns can start a horizontal win)
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                startpoint = (col * 80 + 40, row * 80 + 40)
                endpoint = (col * 80 + 40, (row + 3) * 80 + 40)
                draw_winning_line(startpoint, endpoint, player)
                return True
    return False

def check_diag(player, board):
    #Starting with diagonals going down-left
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                startpoint = (col * 80 + 40, row * 80 + 40)
                endpoint = ((col + 3) * 80 + 40, (row + 3) * 80 + 40)
                draw_winning_line(startpoint, endpoint, player)
                return True
    #Now checking diagonals going down-right
    for row in range(3):
        for col in range(6, 2, -1):
            if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
                startpoint = (col * 80 + 40, row * 80 + 40)
                endpoint = ((col - 3) * 80 + 40, (row + 3) * 80 + 40)
                draw_winning_line(startpoint, endpoint, player)
                return True
    return False

def draw_winning_line(startpoint, endpoint, player):
    winningColour = BACKGROUND_COLOUR
    if(player == 1):
        winningColour = PLAYER_ONE_COLOUR
    elif(player == 2):
        winningColour = PLAYER_TWO_COLOUR
    pygame.draw.line(screen, winningColour, startpoint, endpoint, 15)

def restart_game():
    screen.fill(BACKGROUND_COLOUR)
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col] = 0
    display_board()
    player = 1
    return

gameover = False
player = 1
#Main loop for pygame
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #Will use X coordinate of click to figure out which column was selected
            mouseX = event.pos[0]
            clicked_col = int(mouseX // 80)

            if not is_col_full(clicked_col) and not gameover:
                if player == 1:
                    place_piece(clicked_col, 1)
                    if check_win(player):
                        gameover = True
                    player = 2
                elif player == 2:
                    place_piece(clicked_col, 2)
                    if check_win(player):
                        gameover = True
                    player = 1

                display_board()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                gameover = False
        
    pygame.display.update()