enemies = 3

def increase_enemies():
    # enemies += 1 trying to change global by local
    global enemies #but not recommend to do this, esa log kehte hai. hum to karenge
    enemies += 1
    print(enemies)

increase_enemies()
print(enemies)

# return fuction is also better method to do this