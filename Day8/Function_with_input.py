# def greet():
#     print("wallah habibi")
#     print("bhagwan ka dia sbkuch h")
#     print("hello kutte")
#
# greet()

# Function that allow for input
def greet(name, location) :
    print(f"hello {name} from {location} ")
name1 = input("enter the name")
location1 = input("enter the location ")
greet(name1, location1)
greet(location1, name1) #positional argument
greet(name= "yuvraj", location="jodhpur")#keyword argument