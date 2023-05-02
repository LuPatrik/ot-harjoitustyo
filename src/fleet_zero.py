import pygame
from player_ship import PlayerShip
from enemy_ship import EnemyShip
from player_movement import PlayerMovement
from game_values import GameValues
from collision_detection import CollisionDetection
from screen_refresh import refresh_screen
game_values = GameValues()
collision_detection = CollisionDetection()
screen_size = game_values.screen_size
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(game_values.name)
def main():
    clock = pygame.time.Clock()
    running = True
    player_ship = PlayerShip((screen_size[0]-52)/2, screen_size[1]-100, 4, 100)
    level = 1
    enemy_ship = EnemyShip(0, 0, 0, 0)
    player_movement = PlayerMovement
    def start_new_level():
        print("Current level:", level)
        for _ in range(level+4):
            enemy_ship.spawn_enemy()
    start_new_level()
    while running:
        clock.tick(game_values.fps)
        refresh_screen(screen, player_ship, enemy_ship)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_ship.damage_immunity_update()
        collision_detection.player_and_enemy_collision(player_ship,enemy_ship)
        collision_detection.bullet_and_enemy_collision(player_ship,enemy_ship)
        if player_ship.lives == 0:
            running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
        player_movement.player_movement(None,player_ship)
        if len(enemy_ship.enemies) == 0:
            level +=1
            start_new_level()
        for enemy in enemy_ship.enemies:
            enemy.move()
            if enemy.y_coord > game_values.screen_size[1]:
                player_ship.lives -=1
                print("enemy through! lives left:", player_ship.lives)
                enemy_ship.enemies.remove(enemy)
        player_ship.bullets = [bullet for bullet in player_ship.bullets if bullet.y_coord > -20]
if __name__ == "__main__":
    main()
