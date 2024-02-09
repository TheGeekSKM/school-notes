import turtle
import random


def quick_setup():  # a custom function.
    new_screen = turtle.Screen()
    new_screen.title("Abstraction")
    new_screen.setup(width=800, height=600)
    new_pen = turtle.Turtle()
    return new_screen, new_pen


def randomize_pen_color(pen):
    color = (random.random(), random.random(), random.random())
    pen.color(color)


def draw_start(pen):
    for i in range(5):
        pen.forward(100)
        pen.right(144)


if __name__ == "__main__":
    screen, my_pen = quick_setup()
    randomize_pen_color(my_pen)
    draw_start(my_pen)
    screen.exitonclick()
