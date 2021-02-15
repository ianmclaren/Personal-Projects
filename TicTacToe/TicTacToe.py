#This is creating the board:
board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]




#Declaring variables:

#turn_tracker keeps track of who's turn it is
turn_tracker = 1
valid_square = 0
final_result = 0


#There's a maximum of 9 turns, so we only need to repeat this process 9 times
for turn in range(9):

    #printing the board in its current state
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = "")
            print(" ", end = "")
        print("")

    #Printing message based on who's turn it is and taking input
    while(True):
        if(turn_tracker == 1):
            chosen_square = input("Player 1, please type an available number and press enter: ")
        elif(turn_tracker == 2):
            chosen_square = input("Player 2, please type an available number and press enter:")

        #Error handling for if input is X or O
        if(chosen_square == "X" or chosen_square == "O"):
            print("Please select a valid number")
            continue


        #Scanning through board to find matching number
        for i in range(3):
            for j in range(3):
                if(board[i][j] == chosen_square):
                    #Changing number to the player's symbol
                    if(turn_tracker == 1):
                        board[i][j] = "X"
                    elif(turn_tracker == 2):
                        board[i][j] = "O"
                    else:
                        print("Error, invalid turn tracker")
                    
                    #setting input to valid
                    valid_square = 1

                    #checking to see if someone won - will update with better way in future
                    

        #Returning to the start of the loop, as the input was not an available number
        if(valid_square == 0):
            print("Please select a valid number") 
            continue

        #If input was valid, break out of while loop
        break
                
                

    #Check to see if someone has won  - should come up with a batter way
    #Top row
    if(board[0][0] == board[0][1] == board[0][2]):
        if(turn_tracker == 1):
            final_result = 1
        elif(turn_tracker == 2):
            final_result = 2
        break
    #Middle row
    if(board[1][0] == board[1][1] == board[1][2]):
        if(turn_tracker == 1):
            final_result = 1
        elif(turn_tracker == 2):
            final_result = 2
        break
    #Bottom row
    if(board[2][0] == board[2][1] == board[2][2]):
        if(turn_tracker == 1):
            final_result = 1
        elif(turn_tracker == 2):
            final_result = 2
        break
    #Left column
    if(board[0][0] == board[1][0] == board[2][0]):
        if(turn_tracker == 1):
            final_result = 1
        elif(turn_tracker == 2):
            final_result = 2
        break
    #Middle column
    if(board[0][1] == board[1][1] == board[2][1]):
        if(turn_tracker == 1):
            final_result = 1
        elif(turn_tracker == 2):
            final_result = 2
        break
    #Right column
    if(board[0][2] == board[1][2] == board[2][2]):
        if(turn_tracker == 1):
            final_result = 1
        elif(turn_tracker == 2):
            final_result = 2
        break
    #Diagonal going right-down
    if(board[0][0] == board[1][1] == board[2][2]):
        if(turn_tracker == 1):
            final_result = 1
        elif(turn_tracker == 2):
            final_result = 2
        break
    #Diagonal going left-down
    if(board[2][0] == board[1][1] == board[2][0]):
        if(turn_tracker == 1):
            final_result = 1
        elif(turn_tracker == 2):
            final_result = 2
        break
        
    

    #Switching who's turn it is
    if(turn_tracker == 1):
        turn_tracker = 2
    elif(turn_tracker == 2):
        turn_tracker = 1

    #resetting valid_square
    valid_square = 0



#Printing the final board
for i in range(3):
        for j in range(3):
            print(board[i][j], end = "")
            print(" ", end = "")
        print("")

#Printing the final result
if(final_result == 0):
    print("Its a Tie! Try Again?")
elif(final_result == 1):
    print("Player 1 Wins!")
elif(final_result == 2):
    print("Player 2 Wins!")

