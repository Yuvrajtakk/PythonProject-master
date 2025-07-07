# D:\code\PythonProject-master\PythonProject-master\Day20-21-SnakeGame\data.txt

# I want to access File which is not in Relative Path.
# access file from D:\code

with open(r"D:\code\sample.txt") as file:
    content = file.read()
    print(content)

with open("C:/Users/Lenovo/OneDrive/Documents/test.txt") as file:

    content = file.read()
    print(content)