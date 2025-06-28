game_level = 3
enimies = ["dev","danav","inshan"]
def create_enemy():
    new_enemy = ""
    if game_level < 6:
        new_enemy = enimies[1]

    print(new_enemy)
