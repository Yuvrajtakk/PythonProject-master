numbers =  [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
# new_list.append(add_1)

#list comprehension
# new_list = [new_item for item in list] -> syntax
new_list = [n+1 for n in numbers]

name = "yuvraj"
new_name = [letter for letter in name]

range_list = [numb * 2 for numb in range(1,5)]

# conditional list comprehension
# syntax - > new_list = [new_item for item in list if test]
languages = ['English', 'Mandarin', 'Chinese', 'Hindi', 'Spanish', 'French']
selective_lang = [language for language in languages if len(language) < 6]
uppercase = [lang.upper() for lang in languages if len(languages) < 7]
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)