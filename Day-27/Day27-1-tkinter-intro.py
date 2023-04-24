import tkinter
import turtle

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="this is a label", font=("Arial", 24, "bold", "italic"))
my_label.pack(side="left")

tim = turtle.Turtle()
tim.write("Hello there")

#textbox






window.mainloop() # This line should always be at the end of the program to keep the window running

