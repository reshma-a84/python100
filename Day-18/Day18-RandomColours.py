# Random Colours using Tuples ( Value of tuples cant be changed). It is different from list.
# eg my_list = [1,2,3,4]
#    my_list[3] = 5
#    print(my_list)  => Output will be [1,2,3,5]  and if you do the same with Tuple

# eg my_tuple = (1,2,3,4)
#    my_tuple[3] = 5
#    print(my_tuple) => It will throw an error "TypeError: 'tuple' object does not support item assignment"

import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


t.colormode(255)
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()
