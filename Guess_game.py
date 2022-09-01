def first_player():  # to decide who will go first
    import random
    player_lst = ["X", "O"]
    turn = random.choice(player_lst)
    return turn


def player_guess(player_chance, max_chances=2):  # player guessing the number
    turn = player_chance
    max_chances = max_chances
    number_to_guess = 10  # it can be random if requied use random function
    count = 0  # to track number of guess
    win = False  # to check player won
    if count <= max_chances:
        for i in range(max_chances):
            guess = int(input(f"player {turn} Guess the number.  "))
            if guess != number_to_guess:
                count += 1
                print(count)
                print(
                    f"That's not the number, player {turn}.  You have {max_chances-count} chances remaining.")
            else:
                print("You guessed it right.")
                win = True
    else:
        print(f"All {max_chances} chances exhausted.")
    return win


def replay():
    play_game = input("Do you want to play again. Yes or NO  ").lower()
    if play_game == "yes":
        game()  # calling main game function agin as user wanted to play
    else:
        print("See you again!!")


def game():
    turn = first_player()
    print(turn + "  will go first.")
    first_player_win = player_guess(turn)
    print(first_player_win)
    if first_player_win == True:
        print(f"{turn } won the game !better luck player other player ")
    else:
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

        second_player_win = player_guess(turn)
        if second_player_win == True:
            print(f"player {turn} win!!")
        else:
            print("Both Players Didn't guess correct number it's a TIE !!")
    replay()


if __name__ == "__main__":
    player_1_choice = input(
        "Player_1 please choose a symbol to start 'X' or 'O':").lower()
    if player_1_choice == "x":
        print("Player_2 your symbol is  'O'")
    else:
        print('Player_2 your symbol is "X"')
    game()
