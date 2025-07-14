from tkinter import *
import random

window = Tk()
window.title("my first GUI program")
window.minsize(width= 500, height=300)

#label

my_label = Label(text= "I am a label", font= ("arial", 24, "bold"))
my_label.pack()