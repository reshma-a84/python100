# Random walk with Named Colours

import turtle as t
import random

colors = ["silver", "blue", "LightSeaGreen", "Aquamarine", "Olive", "SaddleBrown", "Salmon", "MediumVioletRed",
          "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "LightSeaGreen",
                                                                               "DarkSlateBlue"]
directions = [0, 90, 180, 270]

tim = t.Turtle()
screen = t.Screen()
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()
