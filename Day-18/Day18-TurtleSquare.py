# To draw a square 100/100

from turtle import Turtle, Screen

timmy = Turtle()

timmy.color("aquamarine3")
screen = Screen()

# i = 0
# while i < 4:
#     timmy.forward(100)
#     timmy.right(90)
#     i += 1

# or use for loop
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


screen.exitonclick()
