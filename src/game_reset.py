def game_reset(player_ship, game_values, enemy_ship, menu):
    player_ship.x_coord = 0+(800-52)/2
    player_ship.y_coord = 800-100
    player_ship.lives = 3
    player_ship.health = 100
    player_ship.score = 0
    player_ship.bullets= []
    game_values.level = 0
    enemy_ship.enemies = []
    menu.menu_running = True
    menu.run_main_menu()
