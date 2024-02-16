import turtle
import random


def quick_setup():  # a custom function.
    new_screen = turtle.Screen()
    new_screen.title("Abstraction")
    new_screen.setup(width=1920, height=1080)
    new_pen = turtle.Turtle()
    turtle.bgcolor('black')
    return new_screen, new_pen


def randomize_pen_color(pen):
    color = (random.random(), random.random(), random.random())
    pen.color(color)


def draw_star(pen, large_size):
    pen.right(random.randrange(0, 360))

    if large_size == 1:
        for i in range(5):
            pen.forward(200)
            pen.right(144)
    else:
        for i in range(5):
            pen.forward(50)
            pen.right(144)


def get_random_pos(width, height):
    pos_x = random.randrange((-width / 2) + 200, (width / 2) - 200)
    pos_y = random.randrange((-height / 2) + 200, (height / 2) - 200)
    return pos_x, pos_y


if __name__ == "__main__":
    screen, my_pen = quick_setup()
    randomize_pen_color(my_pen)
    for i in range(int(input("Num Stars -> "))):
        my_pen.penup()
        my_pen.goto(get_random_pos(1920, 1080))
        my_pen.pendown()
        randomize_pen_color(my_pen)
        draw_star(my_pen, random.randrange(0, 2))
    screen.exitonclick()
