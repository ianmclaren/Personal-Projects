import numpy as np

def CreateBoard():
    board = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
    return board


def DisplayBoard(board):
    #Declaring variables
    bottom_line = "--------------------"
    number_line = "| 1 2 3 4 5 6 7 |"

    #Printing board
    for x in board:
        print("| ", end="")
        for y in x:
            print(y, end="")
            print(" ", end="")
        print("| ")    
    print(bottom_line)
    print(number_line)

def TakeTurn(player, board):
    
    while(1):
        #Printing prompt
        input_number = input("Player " + str(player) + " please type a number from 1-7 and press enter: ")
        print(input_number)

        #Checking if number is between 1 & 7
        if(int(input_number) > 7 or int(input_number) < 1):
            print("Please enter a valid column")
        else:
            break

    col = int(input_number) - 1
    
    #Placing piece and checking if person won
    PlacePiece(col, player, board)
    if(CheckWin(player, board) == True):
        RestartGame(board)
    

def PlacePiece(col, player, board):
    #Goes through column, starting at bottom, to find first empty spot and places player number there
    for y in range(5, -1, -1):
        if(board[y, col] == 0):
            board[y, col] = player
            DisplayBoard(board)
            return
        
    #If it gets here, the column was full
    print("Please pick a column with an empty slot")


def CheckWin(player, board):
    #Checking all the horizontals
    if CheckHoriz(player, board) == True or CheckVert(player, board) == True or CheckDiag(player, board) == True:
        print("Player " + str(player) + " Wins!!!")
        return True
    else:
        return False


def CheckHoriz(player, board):
    #for each column (Only the first 4 columns can start a horizontal win)
    for col in range(4):
        for row in range(6):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
    return False

def CheckVert(player, board):
    #for each column (Only the first 4 columns can start a horizontal win)
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    return False

def CheckDiag(player, board):
    #Starting with diagonals going down-left
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3]:
                return True
    #Now checking diagonals going down-right
    for row in range(3):
        for col in range(6, 2, -1):
            if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3]:
                return True
    return False

def StartGame(board):
    #First printing of board (empty)
    DisplayBoard(board);
    player = 1
    
    #Player's turns
    for turn_number in range(42):
        TakeTurn(player, board)
        if player is 1:
            player = 2
        elif player is 2:
            player = 1

def RestartGame(board):
    print("Good job! Let's play again!")
    board = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
    StartGame(board)

def main():
    
    #Creating the board
    board = CreateBoard();
    StartGame(board)
    


if __name__ == "__main__":
    main()
