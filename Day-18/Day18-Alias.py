# Example where alias can be used. For Eg create an alias for Turtle as t and use it everywhere

import turtle as t
timmy = t.Turtle()

timmy.color("aquamarine3")
screen = t.Screen()

i = 0
while i < 4:
    timmy.forward(100)
    timmy.right(90)
    i += 1

screen.exitonclick()
