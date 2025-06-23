print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
pay = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("child pay $5.")
        pay += 5
    elif age >= 12 and age < 18:
        print("teen pay $7.")
        pay += 7
    elif age >= 40 and age < 45:
        print("free")
    else :
        print("adult pay $10")
        pay += 10
    photo = (input("want photos in only $2(0 for no)"))
    if photo == 0:
        pay += 0
    else :
        pay += 2
    print(f"total: ${pay}")
else:
    print("Sorry you have to grow taller before you can ride.")
