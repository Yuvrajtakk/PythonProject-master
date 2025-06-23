import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# option 1
random_number = random.randint(0,4)
print(friends[int(random_number)])
# OPTION 2
print(random.choice(friends))