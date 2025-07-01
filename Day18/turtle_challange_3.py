import random
from turtle import Turtle, Screen
meow =Turtle()

colors = ["dark green","blue", "light sea green","magenta","red", "maroon", "yellow","cyan" ]
for side in range(3,11):
    meow.color(random.choice(colors))
    for _ in range(side):
        # col_index = side - 3
        # meow.color(colors[col_index])
        meow.forward(100)
        degree = 360/side
        meow.right(degree)
        # meow.forward(50)

# cleaner methode
def draw_shape(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        meow.forward(100)
        meow.right(angle)

for shape_side_n in range(3,11):
    meow.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()