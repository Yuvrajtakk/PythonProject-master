print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
total=bill+bill*tip/100
print(round(total,2))
people = int(input("How many people to split the bill? "))
per_person= total/people
print(round(per_person,2))
print(f"Each person should pay ${per_person}")