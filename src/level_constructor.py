import random
def start_new_level(enemy_ship, game_values):
    print("Current level:", game_values.level)
    for _ in range(game_values.level + random.randint(1,5)):
        enemy_ship.spawn_enemy()
