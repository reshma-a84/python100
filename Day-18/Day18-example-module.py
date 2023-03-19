import turtle
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("aquamarine3")
timmy_the_turtle.shapesize(2, 2, 12)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
turtle.delay(2)

screen = Screen()
# screen.delay(20)
screen.exitonclick()
