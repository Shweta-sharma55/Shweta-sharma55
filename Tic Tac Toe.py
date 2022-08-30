#Tick Tok Toe game ###
#1.take position from player and place respective marker in choosen position 
#   if position is filled already ask for position again 
#display board after evry move 
#check for winner each move 

#using BoardDB 
BoardDB = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

keys = []

for key in BoardDB:
    keys.append(key)


def printBoard(board):
    """This function Prints Tick Tok Toe board when called"""

    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X' #player_1 choice
    count = 0


    for i in range(10):
        printBoard(BoardDB)
        print(f">>>>>>>>>Player {turn} Move to Which Place <<<<<<<<<")

        move = input()        

        if BoardDB[move] == ' ':#checking if it is valid move
            BoardDB[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if BoardDB['7'] == BoardDB['8'] == BoardDB['9'] != ' ': 
                printBoard(BoardDB)
                print("\nGame Over.\n")                
                print(f">>>>>>>>>Player {turn} Win<<<<<<<<<")                
                break
            elif BoardDB['4'] == BoardDB['5'] == BoardDB['6'] != ' ': 
                printBoard(BoardDB)
                print("\nGame Over.\n")                
                print(f">>>>>>>>>Player {turn} Win<<<<<<<<<")
                break
            elif BoardDB['1'] == BoardDB['2'] == BoardDB['3'] != ' ':
                printBoard(BoardDB)
                print("\nGame Over.\n")                
                print(f">>>>>>>>>Player {turn} Win<<<<<<<<<")
                break
            elif BoardDB['1'] == BoardDB['4'] == BoardDB['7'] != ' ':
                printBoard(BoardDB)
                print("\nGame Over.\n")                
                print(f">>>>>>>>>Player {turn} Win<<<<<<<<<")
                break
            elif BoardDB['2'] == BoardDB['5'] == BoardDB['8'] != ' ':
                printBoard(BoardDB)
                print("\nGame Over.\n")                
                print(f">>>>>>>>>Player {turn} Win<<<<<<<<<")
                break
            elif BoardDB['3'] == BoardDB['6'] == BoardDB['9'] != ' ':
                printBoard(BoardDB)
                print("\nGame Over.\n")                
                print(f">>>>>>>>>Player {turn} Win<<<<<<<<<")
                break 
            elif BoardDB['7'] == BoardDB['5'] == BoardDB['3'] != ' ':
                printBoard(BoardDB)
                print("\nGame Over.\n")                
                print(f">>>>>>>>>Player {turn} Win<<<<<<<<<")
                break
            elif BoardDB['1'] == BoardDB['5'] == BoardDB['9'] != ' ': 
                printBoard(BoardDB)
                print("\nGame Over.\n")                
                print(f">>>>>>>>>Player {turn} Win<<<<<<<<<")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)").lower()
    if restart == "y":  
        for key in keys:
            BoardDB[key] = " "

        game()
    else :
        print("Good bYe !!")

if __name__ == "__main__":
    game()
