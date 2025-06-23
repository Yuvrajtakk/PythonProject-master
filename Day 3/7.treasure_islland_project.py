print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input("you are at crossroad, where do you want to go? type 'left or 'right'\n")
if choice == "left":
    choice2 = input("you came to a lake \ndo you want to wait for a boat? type 'wait' or 'swim'\n")
    if choice2 == "wait":
        choice3 = input("you arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue. which colour do you choose?\n")
        if choice3 == "red":
            print("game over. you are burned by fire")
        elif choice3 == "yellow":
            print("you found the treasure. you win!")
        elif choice3 == "blue":
            print("game over. you enter a room of beasts")
        else:
            print("you chose a door that doesn't exist. game over")

    else :
        print("attacked by trout. game over")
else :
    print("you fall into a hole. game over")