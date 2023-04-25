import pygame
from player_ship import PlayerShip
from enemy_ship import EnemyShip
import random
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Fleet Zero")
def main():
    fps =  60
    clock = pygame.time.Clock()
    running = True
    player_ship = PlayerShip((screen_size[0]-52)/2, screen_size[1]-100, 4, 100)
    level = 1
    enemy_ship = EnemyShip(0, 0, 0, 0)
    def spawn_enemy():
        x_coord = random.randint(0, screen_size[0] - 100)
        y_coord = random.randint(-800, -100)
        speed = 1
        health = 100
        new_enemy_ship = EnemyShip(x_coord, y_coord, speed, health)
        enemy_ship.enemies.append(new_enemy_ship)
    def start_new_level():
        print("Current level: ", level)
        for i in range(level+4):
            spawn_enemy()
    def refresh_screen():
        pygame.display.update()
        screen.fill((0,0,0))
        for bullet in player_ship.bullets:
            bullet.draw(screen)
        for enemy in enemy_ship.enemies:
            enemy.draw(screen)
        player_ship.draw(screen)
    start_new_level()
    while running:
        clock.tick(fps)
        refresh_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_ship.damage_immunity_update()
        for enemy in enemy_ship.enemies:
            if pygame.mask.from_surface(player_ship.image).overlap(
                pygame.mask.from_surface(enemy.image),
                (int(enemy.x_coord-player_ship.x_coord),
                int(enemy.y_coord-player_ship.y_coord))
            ):
                if player_ship.damage_immunity == 0:
                    player_ship.hit(10)
                    print("hit!!", player_ship.health)
                if player_ship.health == 0:
                    running = False
        if pygame.key.get_pressed()[pygame.K_UP] and player_ship.y_coord + player_ship.speed > 0:
            player_ship.y_coord -= player_ship.speed
        if (pygame.key.get_pressed()[pygame.K_DOWN] and player_ship.y_coord
            + player_ship.speed + 100 < screen_size[1]):
            player_ship.y_coord += player_ship.speed
        if (pygame.key.get_pressed()[pygame.K_LEFT] and
            player_ship.x_coord - player_ship.speed > 0):
            player_ship.x_coord -= player_ship.speed
        if (pygame.key.get_pressed()[pygame.K_RIGHT] and
            player_ship.x_coord + player_ship.speed + 100 < screen_size[0]):
            player_ship.x_coord += player_ship.speed
        if ((pygame.key.get_pressed()[pygame.K_x] or
            pygame.key.get_pressed()[pygame.K_SPACE]) and not turbo):
            player_ship.shoot()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            player_ship.speed = 8
            turbo = True
        else:
            player_ship.speed = 4
            turbo = False
        for bullet in player_ship.bullets:
            enemy_hit = False
            for enemy in enemy_ship.enemies:
                if (pygame.mask.from_surface(bullet.image).
                    overlap(pygame.mask.from_surface(enemy.image),
                    (int(enemy.x_coord - bullet.x_coord),
                     int(enemy.y_coord - bullet.y_coord)))):
                    enemy.hit(20)
                    if enemy.health <= 0:
                        enemy_ship.enemies.remove(enemy)
                        player_ship.enemy_destroyed(10)
                        print("score: ", player_ship.score)
                    if len(enemy_ship.enemies) == 0:
                        level+=1
                        start_new_level()
                    print("enemy hit!!", enemy.health)
                    player_ship.bullets.remove(bullet)
                    enemy_hit = True
                    break
                if enemy_hit:
                    break
            bullet.update()
        for enemy in enemy_ship.enemies:
            enemy.move()
        player_ship.bullets = [bullet for bullet in player_ship.bullets if bullet.y_coord > -20]
main()