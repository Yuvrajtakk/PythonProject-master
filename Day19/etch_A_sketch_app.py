from turtle import Turtle,Screen

meow = Turtle()
screen = Screen()

def forward_moves():
    meow.forward(10)

def backward_moves():
    meow.backward(10)

def clockwise_moves():
    meow.right(10)
def counter_clockwise_moves():
    meow.left(10)
def clear_screen():
    meow.clear()
    meow.penup()
    meow.home()
    meow.pendown()
screen.listen()
screen.onkey(forward_moves,"w")
screen.onkey(backward_moves,"s")
screen.onkey(clockwise_moves,"d")
screen.onkey(counter_clockwise_moves,"a")
screen.onkey(clear_screen,"c")
screen.exitonclick()