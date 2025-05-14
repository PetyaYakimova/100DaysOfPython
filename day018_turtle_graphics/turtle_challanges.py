import turtle
from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
# Change appearance
# tim.shape("turtle")
# tim.color("red")

# Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw figures
# colors = ["red", "yellow", "green", "blue", "purple", "black", "grey", "teal"]
# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(360 / i)

# Draw random walk
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     turtle.colormode(255)
#     tim.pencolor(color)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# Draw a spirograph
tim.speed("fastest")
turtle.colormode(255)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.color(color)
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
