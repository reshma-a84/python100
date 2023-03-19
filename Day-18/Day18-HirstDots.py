import colorgram

# rgb_colors = []
# colors = colorgram.extract('dots.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# The above code is used to extract the colours from the image file. Below is the list of colours that were picked from the image. I have deleted a few of them as they are nearly white
# [(211, 153, 62), (39, 86, 174), (102, 160, 210), (230, 199, 55), (181, 60, 100), (149, 19, 60), (199, 114, 157), (142, 181, 10), (190, 72, 38), (51, 110, 95), (65, 53, 41), (12, 66, 136), (56, 51, 68), (190, 75, 98), (66, 42, 59), (93, 99, 172), (150, 174, 168), (222, 173, 192), (174, 187, 219), (183, 98, 83), (228, 176, 167), (73, 64, 51), (78, 57, 53), (178, 196, 203), (102, 141, 134), (174, 202, 194)]

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
screen = turtle_module.Screen()

turtle_module.colormode(255)

color_list = [(211, 153, 62), (39, 86, 174), (102, 160, 210), (230, 199, 55), (181, 60, 100), (149, 19, 60), (199, 114, 157), (142, 181, 10), (190, 72, 38), (51, 110, 95), (65, 53, 41), (12, 66, 136), (56, 51, 68), (190, 75, 98), (66, 42, 59), (93, 99, 172), (150, 174, 168), (222, 173, 192), (174, 187, 219), (183, 98, 83), (228, 176, 167), (73, 64, 51), (78, 57, 53), (178, 196, 203), (102, 141, 134), (174, 202, 194)]
tim.pu()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101
tim.speed("fastest")


for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:

        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen.exitonclick()
