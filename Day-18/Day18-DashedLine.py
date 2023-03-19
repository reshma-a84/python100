import turtle as t

tim = t.Turtle()
screen = t.Screen()

for _ in range(15):
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()

screen.exitonclick()
