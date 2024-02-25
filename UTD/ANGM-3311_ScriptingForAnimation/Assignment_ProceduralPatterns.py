import random


def get_square_pattern(max_rows=1):
    value = ''

    for y in range(max_rows):
        for x in range(max_rows):
            value += "🐟"
            if x == (max_rows - 1):
                value += "\n"

    return value


def get_rect_pattern(max_rows=1, max_cols=1):
    value = ''
    for y in range(max_rows):
        for x in range(max_cols):
            value += "🐟"
            if x == (max_cols - 1):
                value += "\n"

    return value


def get_alternating_rect_pattern(max_rows=1, max_cols=1):
    value = ''

    for y in range(max_rows):
        useable_string = ""
        if y % 2 == 0:
            useable_string = "🐟"
        else:
            useable_string = "🦈"

        for x in range(max_cols):
            value += useable_string
            if x == (max_cols - 1):
                value += "\n"

    return value


def validate_running_bond(max_rows, y, running_bond, line_string):
    if max_rows % 2 == 0 and running_bond:
        if y % 2 == 0:
            line_string += " "
            # print("test")
    elif not (max_rows % 2 == 0) and running_bond:
        if not (y % 2 == 0):
            line_string += " "
            # print("test")
    return line_string


def get_brick_pattern(max_rows=1, max_cols=1, running_bond=False):
    final_string = ""

    for y in range(max_rows):
        x_string = ""

        x_string = validate_running_bond(max_rows, y, running_bond, x_string)

        for x in range(max_cols):
            x_string += "🧱"

        final_string += x_string + "\n"

    return final_string


def initialize_variables():
    final_string = ""
    emojis = ["💎", "👑"]
    useable_char = emojis[0]
    return final_string, emojis, useable_char


def determine_useable_char(useable_char, y, emojis):
    if y % 2 == 0:
        useable_char = emojis[0]
    else:
        useable_char = emojis[1]

    return useable_char


def get_checkered_pattern(max_rows=1, max_cols=1):
    final_string, emojis, useable_char = initialize_variables()

    for y in range(max_rows):
        line_string = ""

        useable_char = determine_useable_char(useable_char, y, emojis)

        for x in range(max_cols):
            line_string += useable_char
            if useable_char == emojis[0]:
                useable_char = emojis[1]
            else:
                useable_char = emojis[0]

        final_string += line_string + "\n"

    return final_string


def loop(final_string, num_of_elements, increasing, num_of_repetitions, mc):
    while num_of_elements > 0:
        line_string = ""

        for i in range(num_of_elements):
            line_string += "🐟"

        if num_of_repetitions > mc:
            increasing = False
        num_of_repetitions += 1

        if increasing:
            num_of_elements += 1
        else:
            num_of_elements -= 1

        final_string += line_string + "\n"

    return final_string


def get_right_arrow_pattern(max_cols):
    final = ""

    if not isinstance(max_cols, int):
        raise TypeError("max_cols must be an integer")

    if max_cols == 0:
        return ""

    num_of_elements = 1
    inc = True
    num_repeat = 2

    final = loop(final, num_of_elements, inc, num_repeat, max_cols)
    return final


def set_variables(array, randomized=False):
    if randomized:
        f, b, d, c, s = array
    else:
        selected_elements = random.sample(array, len(array))
        f, b, d, c, s = selected_elements

    return f, b, d, c, s


def get_my_awesome_pattern(square_size=10, randomized=False):
    array = ["🐟", "🧱", "💎", "👑", "🦈"]
    f, b, d, c, s = set_variables(array, randomized)

    final = f * square_size + "\n"
    final += f + b * (square_size - 2) + f + "\n"
    final += f + b + d * (square_size - 4) + b + f + "\n"
    final += f + b + d + c * (square_size - 6) + d + b + f + "\n"
    final += f + b + d + c + s * (square_size - 8) + c + d + b + f + "\n"
    final += f + b + d + c * (square_size - 6) + d + b + f + "\n"
    final += f + b + d * (square_size - 4) + b + f + "\n"
    final += f + b * (square_size - 2) + f + "\n"
    final += f * square_size + "\n"

    return final


def main():
    # Use this area to call functions as you code, so you can debug and test.
    # But remove all your debug code from here before submitting.

    # TODO: For the submission, modify the below code to print examples of
    # your pattern that best shows off the pattern.
    # Show a variety of patterns generated from different argument
    # inputs to the function. Don't just call your awesome pattern once.

    print(get_my_awesome_pattern())
    print(get_my_awesome_pattern(12, True))
    print(get_my_awesome_pattern(15, True))
    print(get_my_awesome_pattern(20, False))


# DO NOT modify this code
if __name__ == "__main__":
    main()
