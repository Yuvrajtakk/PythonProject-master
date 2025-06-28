
# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.") :- not proper Indentation
#   print("You can drive at age {age}.") :- age will not print cause its not fstring
#   print(f"You can drive at age {age}.") :- what if user filled the age in words like twelve then it will throw "ValueError: invalid literal for int() with base 10" error

try:
    age = int(input("How old are you?"))
except ValueError:
    print("you have typed in a an invalid number. Please try again with a numerical response such as 15.")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

