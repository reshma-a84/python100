import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color : ")

color = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_pos = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

x1 = -230
y1 = -100

for i in range(1, 8):
    tim = Turtle(shape="turtle")
    tim.color(color[i - 1])
    tim.pu()
    # tim.goto(x=x1, y=y_pos[i-1])
    tim.goto(x=x1, y=y1)
    y1 -= -30
    all_turtles.append(tim)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
