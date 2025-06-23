letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []
# let = ""
# num = ""
# sym = ""
import random
# for char in range(0,nr_numbers):
#     num = random.choice(numbers)
#     password += num
# for char in range(0,nr_symbols):
#     sym = random.choice(symbols)
#     password += sym
# for char in range(0,nr_letters):
#     let = random.choice(letters)
#     password += let

# level easy
# print(password)
# level hard
# lenght = nr_letters+ nr_numbers + nr_symbols
# code= [let, num, sym]
# for char in range(0,lenght):
#     pin = random.choice(code)
#     code += pin
# print(code)
for char in range(0,nr_numbers):
    password.append(random.choice(numbers))

for char in range(0,nr_symbols):
    password.append(random.choice(symbols))

for char in range(0,nr_letters):
    password.append(random.choice(letters))

print(password)
random.shuffle(password)
print(password)
code = ""
for char in password:
    code += char
print(code)