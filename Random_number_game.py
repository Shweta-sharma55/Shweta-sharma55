# number game
import random


def get_check_input():
    choice = int(input(f"Please Choose number :"))
    # Add input Filtering Logic here
    return choice


def game():
    player_name = input("Please Enter your name : ")
    player_list = [player_name, "Computer"]
    player_choice = " "
    Computer_choice = " "

    player_turn = random.choice(player_list)
    print(f"{player_turn} will go first  ")
    if player_turn == player_name:
        player_choice = get_check_input()
        print(player_choice)
    else:
        Computer_choice = random.randint(0, 9)

    if player_choice == " ":
        player_choice = get_check_input()
    if Computer_choice == " ":
        Computer_choice = random.randint(0, 9)

    if (player_choice > Computer_choice):
        print(
            f"{player_name} choose {player_choice} and computer choose {Computer_choice} \n >>>>{player_name} win<<<<<<")
    elif (Computer_choice == player_choice):
        print(
            f"{player_choice} choose {player_choice} and computer choose {Computer_choice} \n >>>>Tie<<<<<<")
    else:
        print(
            f"{player_choice} choose {player_choice} and computer choose {Computer_choice} \n >>>>Computer win<<<<<<")

    print("play Again ???")
    play_again = input("Play again Y/N :").lower()
    if play_again == "y":
        game()
    else:
        print("Good Bye")


if __name__ == "__main__":
    game()
