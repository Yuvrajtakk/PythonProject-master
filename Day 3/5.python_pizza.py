print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pay = 0
if size == "S":
    pay += 15
elif size == "M":
    pay += 20
elif size == "L":
    pay += 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni =="Y":
    if size == "S":
        pay += 2
    else :
        pay += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    pay += 1
print(f"Your final bill is: ${pay}.")