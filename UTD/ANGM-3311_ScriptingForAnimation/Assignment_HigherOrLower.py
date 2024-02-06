import random


def roll_dice(sides, dice_count):
    total_num = 0
    for i in range(dice_count):
        total_num += random.randrange(1, sides + 1)

    return total_num


def ask_for_guess():
    guess = 0
    while (not (validate_guess(guess))):
        guess = int(input("Guess a number(2-12) -> "))

    return int(guess)


def validate_guess(guess):
    if guess < 2 or guess > 12:
        return False
    else:
        return True


def hint_higher_lower(guess, secret_roll):
    if guess > secret_roll:
        return "Lower"
    else:
        return "Higher"


def main():
    secret_roll = roll_dice(sides=6, dice_count=2)
    num_guesses = 3
    current_guess = 0
    won = False

    while current_guess < num_guesses:
        guess = ask_for_guess()

        if guess == secret_roll:
            won = True
            print(f"You win! The secret dice roll is {secret_roll}.")
            break
        else:
            print(hint_higher_lower(guess, secret_roll))
            current_guess += 1

    if not won:
        print(f"You lose! The secret dice roll is {secret_roll}.")


if __name__ == "__main__":
    main()
