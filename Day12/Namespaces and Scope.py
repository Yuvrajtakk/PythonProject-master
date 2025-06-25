enemies =1 #global scope

def increases_enemies():
    enemies =2 #local scope/ local variable
    print(f"enemies inside the function: {enemies}")

increases_enemies()
print(f"enemies outside the function: {enemies}")


def drink_potion():
    potion_strenght = 2
    print(potion_strenght)

drink_potion()
# print(potion_strenght) error - localscope
