# number game
import random
import maskpass #pip install maskpass

def get_check_input(name):
    choice = int(maskpass.askpass(prompt=f"{name } Choose a number in range 0-9 : ",mask= "*"))
    # Add input Filtering Logic here
    return choice


def game():
    player_1_name = input("player_1 Please Enter your name : ")
    player_2_name = input("player_2 Please Enter your name : ")

    player_list = [player_2_name,player_1_name]
    player_1_choice = " "
    player_2_choice = " "

    player_turn = random.choice(player_list)
    print(f"{player_turn} will go first  ")
    if player_turn == player_1_name:
        player_1_choice = get_check_input(player_1_name)
        print(player_1_choice)
    else:
        player_2_choice = get_check_input(player_2_name)
        print(player_2_choice)

    if player_1_choice == " ":
        player_1_choice = get_check_input(player_1_name)
    if player_2_choice == " ":
        player_2_choice = get_check_input(player_2_name)

    if (player_1_choice > player_2_choice):
        print(
            f"{player_1_name} choose {player_1_choice} and {player_2_name} choose {player_2_choice} \n >>>>{player_1_name} win<<<<<<")
    elif (player_2_choice == player_1_choice):
        print(
            f"{player_1_name} choose {player_1_choice} and {player_2_name} choose {player_2_choice} \n >>>> Game TIe<<<<<<")
    else:
        print(
            f"{player_1_name} choose {player_1_choice} and {player_2_name} choose {player_2_choice} \n >>>>{player_2_name} win<<<<<<")

    print("play Again ???")
    play_again = input("Play again Y/N :").lower()
    if play_again == "y":
        game()
    else:
        print("Good Bye")


if __name__ == "__main__":
    game()
