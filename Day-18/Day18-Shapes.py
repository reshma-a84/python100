import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()

num_sides = 5

colors = ["silver", "blue", "LightSeaGreen", "Aquamarine", "Olive", "SaddleBrown", "Salmon", "MediumVioletRed",
          "DarkSlateBlue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_range in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_range)

screen.exitonclick()
