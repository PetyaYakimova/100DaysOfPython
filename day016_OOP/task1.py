import another_module

print(another_module.another_variable)

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
# Use methods from the object
timmy.shape("turtle")
timmy.color("DarkOrchid2")
timmy.forward(100)

my_screen = Screen()
# Use attributes of the object
print(my_screen.canvheight)
my_screen.exitonclick()
