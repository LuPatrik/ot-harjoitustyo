import pygame
from player_ship import PlayerShip
from enemy_ship import EnemyShip
class CollisionDetection:
    def __init__(self) -> None:
        self.player_ship = PlayerShip(0,0,0,0)
        self.enemy_ship = EnemyShip(0,0,0,0)
    def player_and_enemy_collision(self, player_ship, enemy_ship):
        for enemy in enemy_ship.enemies:
            if pygame.mask.from_surface(player_ship.image).overlap(
                pygame.mask.from_surface(enemy.image),
                (int(enemy.x_coord-player_ship.x_coord),
                int(enemy.y_coord-player_ship.y_coord))
            ):
                if player_ship.damage_immunity == 0:
                    player_ship.hit(10)
                    print("hit!!", player_ship.health)
                if player_ship.health <= 0:
                    player_ship.lives -= 1
                    player_ship.health = 100
                    print("lives left:", player_ship.lives)
    def bullet_and_enemy_collision(self, player_ship, enemy_ship):
        for bullet in player_ship.bullets:
            enemy_hit = False
            for enemy in enemy_ship.enemies:
                if (pygame.mask.from_surface(bullet.image).
                    overlap(pygame.mask.from_surface(enemy.image),
                    (int(enemy.x_coord - bullet.x_coord),
                     int(enemy.y_coord - bullet.y_coord)))):
                    enemy.hit(20)
                    enemy_hit = True
                    print("enemy hit!!", enemy.health)
                    player_ship.bullets.remove(bullet)
                if enemy.health <= 0:
                    enemy_ship.enemies.remove(enemy)
                    player_ship.enemy_destroyed(10)
                    print("score: ", player_ship.score)
                if enemy_hit:
                    break
            bullet.update()