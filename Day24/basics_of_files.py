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

# f1 = open("file1.txt" , "r")
# contents_1= f1.readlines()
# f2 = open("file2.txt" , "r")
# contents_2= f2.readlines()
#
# cleaned_1 = [int(line.strip()) for line in contents_1]
# cleaned_2 = [int(line.strip()) for line in contents_2]
# # refined_1 =[num for num in contents_1 if ]
# result = [num for num in cleaned_1 if num in cleaned_2]
#
# print(result)

with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

print(result)