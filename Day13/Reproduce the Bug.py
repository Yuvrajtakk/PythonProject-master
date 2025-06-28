from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) :- error, not printing 1 and throw out of range error
# dice_num = randint(1, 5) :- no error, but logic error, 1 not occurring
dice_num = randint(0, 5)
print(dice_images[dice_num])
