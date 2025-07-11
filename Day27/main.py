import tkinter

window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width= 500, height=300)

#label

my_label =tkinter.label(text= "I am a label", font= ("arial", 24, "bold"))
my_label.pack()