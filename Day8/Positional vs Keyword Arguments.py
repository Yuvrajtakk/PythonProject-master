#Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")
def calculate_love_score(name1, name2):
    word = name1 + name2
    count1 = 0
    count2 = 0
    i = len(word)
    for j in range(0, i):
        if word[j] == "t" or word[j] == "r" or word[j] == "u" or word[j] == "e":
            count1 += 1
        if word[j] == "l" or word[j] == "o" or word[j] == "v" or word[j] == "e":
            count2 += 1
    print(f"{count1}{count2}")


calculate_love_score("Kanye West", "Kim Kardashian")

# method 2
# def calculate_love_score(name1, name2):
#     word = (name1 + name2).lower()
#     count1 = 0
#     count2 = 0
#     for letter in word:
#         if letter in "true":
#             count1 += 1
#         if letter in "love":
#             count2 += 1
#     love_score = int(str(count1) + str(count2))
#     print(love_score)
#
# # Test it
# calculate_love_score("Kanye West", "Kim Kardashian")

# method 3
# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
#
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
#
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
#
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")

