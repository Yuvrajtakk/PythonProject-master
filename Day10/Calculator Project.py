
import art



from itertools import accumulate


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

operations ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
# print(operations["*"](n1= 5, n2= 3))
def calculator():
    print(art.logo)
    should_accumulate = True
    num1= float(input("What's the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        sym = input("Pick an operation: ")
        num2 =float(input("Whats the second number?:"))
        answer = operations[sym](num1, num2)
        print(f"{num1} {sym} {num2} = {answer}")

        choice = input(f"Type y for countinue calculating with {answer}, or type n for start with new calculaton :")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()