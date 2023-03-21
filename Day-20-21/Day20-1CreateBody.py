from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_postions = [(0, 0), (-20, 0), (-40, 0)]   #Tuples

for position in starting_postions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

screen.exitonclick()
