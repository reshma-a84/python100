# grid and pack should not be mixed together. Use Grid as it is more flexible

from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


def button_clicked():
    print("I got clicked")
    new_text = ip_box.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

ip_box = Entry(width=10)
print(ip_box.get())
ip_box.grid(column=3, row=2)

window.mainloop()
