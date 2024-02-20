def get_square_pattern(max_rows):
    value = ''

    for y in range(max_rows):
        for x in range(max_rows):
            value += "🐟"
            if x == (max_rows - 1):
                value += "\n"

    return value


def get_rect_pattern(max_rows, max_cols):
    value = ''
    for y in range(max_rows):
        for x in range(max_cols):
            value += "🐟"
            if x == (max_cols - 1):
                value += "\n"

    return value


def get_alternating_rect_pattern(max_rows, max_cols):
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


def get_brick_pattern(max_rows, max_cols, running_bond):
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


def get_checkered_pattern(max_rows, max_cols):
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


# TODO: MAKE LESS THAN 15
def get_right_arrow_pattern(max_cols):
    """Returns a pattern of 🐟 emojis in the shape of a right arrow.

    Arguments:
        max_cols: the max number of emojis in a line.

    Returns:
        str: Returns a string pattern of emojis.

    Examples:
        >>> print(get_right_arrow_pattern(3))
        🐟
        🐟🐟
        🐟🐟🐟
        🐟🐟
        🐟

        >>> print(get_rect_pattern(2))
        🐟
        🐟🐟
        🐟
    """
    final_string = ""
    num_of_elements = 1
    increasing = True
    num_of_repetitions = 1
    
    while num_of_elements > 0:
        line_string = ""
        
        for i in range(num_of_elements):
            line_string += "🐟"
        
        if num_of_repetitions > max_cols:
            increasing = False    
        num_of_repetitions += 1
        
        if increasing:
            num_of_elements += 1
        else:
            num_of_elements -= 1
            
        final_string += line_string + "\n"
        
    return final_string


def get_my_awesome_pattern():
    """Returns your own awesome procedural emoji pattern.

    Returns:
        str: Returns a string pattern of emojis.
    """
    # TODO: Implement your awesome procedural pattern.
    # Let loose your creativity!
    # You can choose whatever arguments makes sense for your pattern.
    # You pattern must change based on your arguments for it to be
    # procedural.
    # You must, use a combination of loops and conditional statements to
    # generate your pattern.
    # Each unique emoji should not repeat more than once in your code.
    # (It wouldn't be procedural otherwise. 😉)
    pass


def main():
    # Use this area to call functions as you code, so you can debug and test.
    # But remove all your debug code from here before submitting.

    # TODO: For the submission, modify the below code to print examples of
    # your pattern that best shows off the pattern.
    # Show a variety of patterns generated from different argument
    # inputs to the function. Don't just call your awesome pattern once.
    print(get_square_pattern(10))
    print(" ")
    print(get_rect_pattern(7, 9))
    print(" ")
    print(get_alternating_rect_pattern(3, 5))
    print(" ")
    print(get_brick_pattern(3, 5, True))
    print(" ")
    print(get_brick_pattern(6, 5, True))
    print(" ")
    print(get_brick_pattern(3, 5, False))
    print(" ")
    print(get_checkered_pattern(5, 6))
    print(" ")

    print(get_my_awesome_pattern())


# DO NOT modify this code
if __name__ == "__main__":
    main()
