import os
from termcolor import colored

os.system("cls")

# gathering input
user_input = input("Please enter a time (HH:MM:SS) -> ")
frame_rate = float(input("Please enter a framerate -> "))

# splitting the input into hours, minutes, and seconds
hours = float(user_input[:2])
minutes = float(user_input[3:5])
seconds = float(user_input[6:])

# calculate total seconds and multiply with number of frames
total_seconds = seconds + (minutes * 60) + ((hours * 60) * 60)
output = int(total_seconds * frame_rate)

# print output
output_string = f"{output:,}"
print(f"Your total frame count -> {colored(output_string, 'green')}")
