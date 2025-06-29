# from turtle import Turtle,Screen
# meow = Turtle()
# print(meow)
# meow.shape("turtle")
# meow.color("LightCyan3")
# meow.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",["Pikachu","squirtle","charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)
