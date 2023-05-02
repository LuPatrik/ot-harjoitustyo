import random
def start_new_level(enemy_ship, game_values):
    """Funktio, joka vastaa uuden tason luomisesta.
    Args: 
        enemy_ship: Perii vihollisaluksen tiedot ja samalla funktion
        spawn_enemy, jonka avulla se lisää uuteen tasoon viholliset
        game_values: Perii pelin tason ja määrittää sen mukaan kuinka monta
        vihollisalusta lisätään tasoon"""
    print("Current level:", game_values.level)
    for _ in range(game_values.level + random.randint(1,5)):
        enemy_ship.spawn_enemy()
