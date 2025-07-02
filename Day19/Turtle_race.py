import random
from turtle import Turtle,Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!🥳🎉")

            else:
                print(f"You've Lost! The {winning_color} is the winner!😫🤡")





 #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


# speed =[0,1,3,6,8,10]
# random.shuffle(color)
# # random.shuffle(speed)
#
# meow = Turtle(shape= "turtle")
# meow.color(color[0])
# meow.penup()
# meow.goto(-225,11)
#
#
# tweety = Turtle(shape= "turtle")
# tweety.color(color[1])
# tweety.penup()
# tweety.goto(-225,-11)
#
#
# tim = Turtle(shape= "turtle")
# tim.color(color[2])
# tim.penup()
# tim.goto(-225,33)
#
#
# sugar = Turtle(shape= "turtle")
# sugar.color(color[3])
# sugar.penup()
# sugar.goto(-225,-33)
#
#
# tommy = Turtle(shape= "turtle")
# tommy.color(color[4])
# tommy.penup()
# tommy.goto(-225,55)
#
#
# tod = Turtle(shape= "turtle")
# tod.color(color[5])
# tod.penup()
# tod.goto(-225,-55)
#
#
# # meow.speed(speed[0])
# # meow.forward(300)
# # tod.speed(speed[5])
# # tod.forward(300)
# # tommy.speed(speed[4])
# # tommy.forward(300)
# # sugar.speed(speed[3])
# # sugar.forward(300)
# # tweety.speed(speed[1])
# # tweety.forward(300)
# # tim.speed(speed[2])
# # tim.forward(300)
#
# for _ in range(75):
#
#     meow.forward(random.randint(0,10))
#     tim.forward(random.randint(0,10))
#     tweety.forward(random.randint(0,10))
#     sugar.forward(random.randint(0,10))
#     tommy.forward(random.randint(0,10))
#     tod.forward(random.randint(0,10))

screen.exitonclick()
