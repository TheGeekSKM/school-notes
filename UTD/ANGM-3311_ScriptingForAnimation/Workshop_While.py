import os
from termcolor import colored

os.system("cls")
counter = 1

print(colored("\nWhile Loop Print:", "green"))
while (counter < 4):
    print(colored(counter, "green"))
    counter += 1

print(" ")
print(" ")
print(colored("For Loop Print:", "green"))

for i in range(1, 4):
    print(colored(i, "green"))

print(" ")
print(" ")
print(" ")
os.system("color 0a")
print("User Input Loop")

end = False
while (not end):
    user_input = input("Enter a response -> ")
    if user_input != "":
        user_input = user_input.lower()
        if user_input[0] == "q":
            end = True

print(" ")
print(" ")
print(" ")
print("While True")
while True:
    user_input = input("bungus -> ")
    if user_input != "":
        user_input = user_input.lower()
        if user_input[0] == "q":
            break
        
os.system("cls")
final = ""
for y in range(10):
    for x in range(10):
        final += f"({x}, {y}),  "
    final += "\n"
print(final)

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")


final = ""
for y in range(10):
    for x in range(10):
        if x % 2 == 0 and y % 2 == 0:
            final += colored(f"({x}, {y}),  ", "red")
        else:
            final += f"({x}, {y}),  "

    final += "\n"
print(final)

inp = input("Press enter to continue -> ")

os.system("cls")


def get_triangles(size):
    final = ""
    for y in range(size):
        final += ("💥" * (y + 1)) + "\n"
    return final


def get_right_arrow(size):
    final = ""
    for y in range(size):
        final += ("💥" * (y + 1)) + "\n"
    for y in range(size - 1):
        final += ("💥" * ((size - 1) - y)) + "\n"
    return final


print(get_triangles(int(input("gimme a number, dummy -> "))))
print(get_right_arrow(int(input("gimme another number, dummy -> "))))


# ask for input
# for loop through the input
# num of space = total input - (row + 1) 
# print emoji
# num of space = total input - (row + 1)
    
def get_pyramid(size):
    final = ""
    for row in range(size):
        final += " " * (size - (row + 1))
        final += "💥" * (row + 1)
        final += "\n"
    return final


print(get_pyramid(int(input("gimmer another number again, dummy -> "))))


def get_alternating_faces(size):
    final = ""
    emoji1 = "😀"
    emoji2 = "😊"

    for row in range(size):
        if row % 2 == 0:
            final += emoji1 * (size)
        else:
            final += emoji2 * (size)
        final += "\n"

    return final


print(get_alternating_faces(int(input("ANOTHER NUMBER!!! -> "))))