import random
import os
from termcolor import colored


def title_display():
    os.system("cls")
    os.system("color 0F")
    print("_  _ _  _ ____ ____ _  _ ____ _  _ ___ ")
    print("|_/  |\ | |  | |    |_/  |  | |  |  |  ")
    print("| \_ | \| |__| |___ | \_ |__| |__|  |  ")
    print("")
    print("By Sai Mangipudi")
    print("")


def round_display(current_round, total_rounds):
    print(f"\nRound: {current_round} of {total_rounds}")


def score_display(player_score, c_score):
    print(f"\n Player Score -> {player_score} and \
Computer Score -> {c_score}\n")


def ask_for_rounds():
    t_rounds = int(input("[GAME] How many rounds would you like to play? -> "))
    c_round = 0
    return t_rounds, c_round


def variable_setup():
    player_score = 0
    computer_score = 0
    t_rounds, c_rounds = ask_for_rounds()

    return player_score, computer_score, t_rounds, c_rounds


def roll_dice(dice_num, dice_sides):
    total = 0
    for i in range(dice_num):
        total += random.randrange(1, dice_sides + 1)

    return total


def gather_roll_input():
    user_input = input("Press Enter to Roll Dice ->")
    if user_input == '':
        return

    user_input = user_input.lower()
    if user_input[0] == 'q':
        exit()


def gather_input_roll(phrase):
    user_input = input(phrase + " -> ")
    if user_input == '':
        return

    user_input = user_input.lower()
    if user_input[0] == 'q':
        exit()


def determine_rolls(player_score, com_score):
    gather_roll_input()

    player_roll = roll_dice(2, 6)
    print(f"\n You rolled a total of {player_roll}")

    computer_roll = roll_dice(2, 6)
    print(f"\n The Computer rolled a total of {computer_roll}")

    return validate_scores(player_roll, player_score, computer_roll, com_score)


def validate_scores(player_roll, player_score, computer_roll, computer_score):
    if player_roll == 7:
        print(colored("\n[KNOCKOUT] YOUR SCORE \
HATH BEEN DELETED, PEASENT!!!", 'red'))
        player_score = 0
    else:
        player_score += player_roll

    if computer_roll == 7:
        print(colored("\n[KNOCKOUT] THE COMPUTER'S \
SCORE HATH BEEN DELETED!!!", 'green'))
        computer_score = 0
    else:
        computer_score += computer_roll

    score_display(player_score, computer_score)
    return player_score, computer_score


def determine_winner(player_score, computer_score):
    os.system("cls")
    if player_score > computer_score:
        os.system("color 0a")
        print("YOU WON!!!!")
    else:
        os.system("color 0c")
        print("YOU LOST!!!")

    print(f"You had a total score of {player_score}!")
    print(f"The Computer had a total score of {computer_score}!")


if __name__ == "__main__":
    title_display()
    player_score, com_score, total_rounds, current_round = variable_setup()

    while current_round < total_rounds:
        round_display(current_round, total_rounds)
        player_score, com_score = determine_rolls(player_score, com_score)
        current_round = current_round + 1

    gather_input_roll("Press Enter to see the winner")
    determine_winner(player_score, com_score)
