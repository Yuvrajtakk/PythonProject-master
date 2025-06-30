from turtle import Turtle, Screen
meow =Turtle()
meow.shape("turtle")
meow.color("blue")
# meow_the_kachua.right(90)
# meow_the_kachua.forward(100)
# meow_the_kachua.right(90)
# meow_the_kachua.forward(100)
# meow_the_kachua.right(90)
# meow_the_kachua.forward(100)
# meow_the_kachua.right(90)
# meow_the_kachua.forward(100)

for _ in range(4):
    meow.right(90)
    meow.forward(100)
screen = Screen()
screen.exitonclick()

