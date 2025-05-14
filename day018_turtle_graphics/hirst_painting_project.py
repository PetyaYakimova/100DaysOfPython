import turtle
from turtle import Turtle
from turtle import Screen
import random
import colorgram

rgb_colors = []


def extract_colors():
    colors = colorgram.extract("hirst-image.jpg", 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)


def get_random_color():
    return random.choice(rgb_colors)


tim = Turtle()

tim.speed("fastest")
turtle.colormode(255)
extract_colors()

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, get_random_color())
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = Screen()
screen.exitonclick()
