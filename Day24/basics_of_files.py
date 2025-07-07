# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()
# my name is Yuvraj

with open("my_file.txt" , mode= "w" ) as my_file :
    my_file.write("new text")

# new text

with open("my_file.txt" , mode= "a" ) as my_file :
    my_file.write("\nMy name is Yuvraj")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# new text
# My name is Yuvraj

# Before :no my_file exists
with open("new_file.txt" , mode= "a" ) as my_file :
    my_file.write("\nMy name is Yuvraj")

# After: automatically new file created