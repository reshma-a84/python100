from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    new_text = ip_box.get()
    # my_label.config(text="Button got clicked")
    my_label.config(text=new_text)

button = Button(text="Click me", command=button_clicked)
# button.pack(side="bottom")
button.pack()

ip_box = Entry()
ip_box.pack()
ip_box.get()



window.mainloop()
