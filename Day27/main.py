
from tkinter import *
import random

window = Tk()
window.title("my first GUI program")
window.minsize(width= 500, height=300)

#label

my_label = Label(text= "I am a label", font= ("arial", 24, "bold"))
my_label.pack()

my_label["text"] ="New text"
my_label.config(text="New text")

def button_clicked():
    moan = ["Ahhh💦", "ummhh🫦", "ohh😫","yeah😭😭"]
    moaning = random.choice(moan)
    my_label.config(text= moaning)
    print("Ahhh💦")

button = Button(text= "Fuck me", command= button_clicked)
button.pack()



window.mainloop()