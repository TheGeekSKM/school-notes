import turtle
import colorsys


def quick_setup():  # a custom function.
    new_screen = turtle.Screen()
    new_screen.title("Lab_GenerativeArt")
    new_screen.setup(width=800, height=600)
    new_pen = turtle.Turtle()
    turtle.goto(0, 0)
    turtle.bgcolor('black')
    turtle.speed(0)
    turtle.pensize(5)
    return new_screen, new_pen


def draw_random_art(pen):
    hue = 0.0
    for i in range(300):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        pen.pencolor(color)
        hue += 0.005
        pen.right(i)
        pen.circle(50, i)
        pen.forward(i)
        pen.left(91)


if __name__ == "__main__":
    screen, my_pen = quick_setup()
    draw_random_art(my_pen)
