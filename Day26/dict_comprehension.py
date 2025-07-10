# Dictionary comprehension

# syntax -> new_dict ={new_key :new_value for value item in list }
# syntax -> new_dict ={new_key :new_value for (key, value) in dict.item() }
# syntax -> new_dict ={new_key :new_value for (key, value) in dict.item() if test}

languages = ['English', 'Mandarin', 'Chinese', 'Hindi', 'Spanish', 'French']
import random
lang_score ={lang :random.randint(1,100) for lang in languages }
best_language ={lang :value for (lang, value) in lang_score.items() if value > 35}