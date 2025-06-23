print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("what is your age?"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age < 13:
        print("pay $7")
    else :
        print("lol! pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
