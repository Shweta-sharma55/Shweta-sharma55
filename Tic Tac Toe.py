#Tick Tok Toe game ###
# Take position from player and place respective marker in choosen position
#   If position is filled already ask for position again
# Display board after every move
# Check for winner each move after 5 positions are filled

import random

boardDB = {'7': ' ', '8': ' ', '9': ' ',
           '4': ' ', '5': ' ', '6': ' ',
           '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in boardDB:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    player_lst = ["player_1", "player_2"]
    go_first = random.choice(player_lst)
    print(f'{go_first} will start First and has marker "X" ')

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(boardDB)
        print("It's your turn," + turn + ". Move to which place?")

        move = input()

        if boardDB[move] == ' ':
            boardDB[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if boardDB['7'] == boardDB['8'] == boardDB['9'] != ' ':
                printBoard(boardDB)
                print("\nGame Over.\n")
                print(f" **** player {turn} won. ****")
                break
            elif boardDB['4'] == boardDB['5'] == boardDB['6'] != ' ':
                printBoard(boardDB)
                print("\nGame Over.\n")
                print(f" ****   player {turn} won. ****")
                break
            elif boardDB['1'] == boardDB['2'] == boardDB['3'] != ' ':
                printBoard(boardDB)
                print("\nGame Over.\n")
                print(f" ****   player {turn} won. ****")
                break
            elif boardDB['1'] == boardDB['4'] == boardDB['7'] != ' ':
                printBoard(boardDB)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif boardDB['2'] == boardDB['5'] == boardDB['8'] != ' ':
                printBoard(boardDB)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif boardDB['3'] == boardDB['6'] == boardDB['9'] != ' ':
                printBoard(boardDB)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif boardDB['7'] == boardDB['5'] == boardDB['3'] != ' ':
                printBoard(boardDB)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif boardDB['1'] == boardDB['5'] == boardDB['9'] != ' ':
                printBoard(boardDB)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do want to play Again?(y/n)").lower()
    if restart == "y":
        for key in board_keys:
            boardDB[key] = " "

        game()
    else:
        print("Thanks ! Good bye!!")


if __name__ == "__main__":
    game()
