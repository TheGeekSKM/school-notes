import sys
import time
import os
from termcolor import colored


def typewriter(sentence, type_delay):
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)
    time.sleep(1)


os.system("cls")

color = input("Enter color -> ")
adjective = input("Enter an adjective -> ")
time_input = input("Enter a time of day -> ")
adjective2 = input("Enter another adjective -> ")
place = input("Enter the name of a place -> ")
food = input("Enter the name of some food -> ")
food2 = input("Enter the name of another type of food -> ")
verb = input("Enter a verb -> ")
noun = input("Enter a noun -> ")
number_input = input("Enter a number -> ")

os.system("cls")

typewriter(f"Bats are so cool! They are {colored(color, 'red')}, \
{colored(adjective, 'red')} animals which have wings. \
They like to fly around at {colored(time_input, 'red')} \
which makes some people scared of them. \
But bats are {colored(adjective2, 'red')}, \
and they don't want to hurt people. \
I have a pet bat that lives in {colored(place, 'red')}. \
I like to feed him {colored(food, 'red')} and {colored(food2, 'red')}. \
He likes to {colored(verb, 'red')}. \
I am his favorite person, but he also likes {colored(noun, 'red')}. \
I want to convince my parents to get me \
{colored(number_input, 'red')} more bats.", 0.1)
