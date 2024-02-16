import random
import art
import os


def gather_user_input():
    str_input = ''
    first_char = ''

    while (not (validate_input(first_char))):
        str_input = input("[Computer] Make your move, filthy casual -> ")
        str_input = str_input.lower()
        first_char = str_input[0]

    return first_char


def validate_input(str_input):
    if str_input == 'r' or str_input == 's' or str_input == 'p':
        return True
    elif str_input == 'q':
        quit_game()

    return False


def generate_computer_input():
    computer_guess = random.randrange(1, 4)
    if computer_guess == 1:
        return 'r'
    if computer_guess == 2:
        return 'p'
    if computer_guess == 3:
        return 's'


def comparison_logic(user_input, computer_input):
    # 0 = tie, 1 = user win, -1 = computer win
    if user_input == computer_input:
        return 0
    if user_input == 'r' and computer_input == 's':
        return 1
    if user_input == 's' and computer_input == 'p':
        return 1
    if user_input == 'p' and computer_input == 'r':
        return 1
    return -1


def computer_input_to_string(computer_input):
    if computer_input == 'r':
        return "Rock"
    if computer_input == 'p':
        return "Paper"
    if computer_input == 's':
        return "Scissors"


def round_logic(user_input, computer_input, current_round, scores):

    result = comparison_logic(user_input, computer_input)

    if result == 0:
        print(f"Tie! I got {computer_input_to_string(computer_input)} too!")
    elif result == 1:
        print(f"You won! I got {computer_input_to_string(computer_input)}!")
        scores[0] += 1
        current_round += 1
    else:
        print(f"You lose! I got {computer_input_to_string(computer_input)}!")
        scores[1] += 1
        current_round += 1

    return current_round, scores


def setup_game():
    print(" ")
    total_rounds = int(input("How many rounds would you like to play? -> "))
    current_round = 0
    scores = [0, 0]
    return total_rounds, current_round, scores


def title_game():
    os.system('cls')
    art.tprint("Rock Paper Scissors Game")
    print("By Sai")


def determine_winner(scores):
    if scores[0] > scores[1]:
        return "Player"
    elif scores[0] < scores[1]:
        return "Computer"
    else:
        return "Tie"


def display_winner(scores):
    winner = determine_winner(scores)
    print(f"Final Scores: Player -> {scores[0]} : {scores[1]} <- Computer")

    if winner == "Tie":
        value = f"It's a tie! The scores are {scores[0]} to {scores[1]}!"
        art.tprint(value)
    else:
        value = f"{winner} wins with a score of {scores[0]} to {scores[1]}!"
        art.tprint(value)


def quit_game():
    print("Thanks for playing!")
    exit(0)


if __name__ == '__main__':
    title_game()
    total_rounds, c_round, scores = setup_game()
    os.system('cls')

    while (c_round < total_rounds):
        print(f"Round {c_round} - Current Scores[Player -> {scores[0]} \
: {scores[1]} <- Computer]")
        u_input = gather_user_input()
        c_input = generate_computer_input()
        c_round, scores = round_logic(u_input, c_input, c_round, scores)
        input("Press Enter to continue...")
        os.system('cls')

    os.system('color 0a')
    display_winner(scores)
