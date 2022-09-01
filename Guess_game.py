def first_player():  # to decide who will go first
    import random
    player_lst = ["player1", "player2"]
    goes_first = random.choice(player_lst)
    return goes_first


def player_choice():  # for player to decide his mark(X or Y)
    choice = " "
    print(choice)
    while choice not in ["X", "Y"]:
        choice = input("Choose X or Y  ").capitalize()  # fixed here
        print(choice)
    return choice


def player_guess(player_name):  # player guessing the number
    player = player_name
    max_chances = 2
    number_to_guess = 10  # it can be random if requied use random function
    count = 0  # to track number of guess
    win = False  # to check player won
    if count < max_chances:
        guess = int(input("Guess the number.  "))
        if guess != number_to_guess:
            count += 1
            print(
                f"That's not the number, {player}.  You have {max_chances-count} chances remaining.")
            player_guess(player)
        else:
            print("You guessed it right.")
            win = True

    if count == max_chances:
        print(f"All {max_chances} chances exhausted.")
    return win


def replay():
    play_game = input("Do you want to play again. Yes or NO  ").lower()
    if play_game == "yes":
        game()  # calling main game function agin as user wanted to play
    else:
        print("See you again!!")


def game():
    # core game operations here

    firstplayer = first_player()
    print(firstplayer + "  will go first.")

   # pending final logic


if __name__ == "__main__":
    game()
