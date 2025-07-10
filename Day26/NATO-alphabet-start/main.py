# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}


import pandas

# Step 1: Read CSV and create dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Step 2: Get user input
user_word = input("Enter a word: ")

# Step 3: Convert to phonetic codes
phonetic_list = [nato_dict[letter] for letter in user_word.upper()]

print(phonetic_list)

# Example usage:
# If user enters "hello", output will be:
# ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']

