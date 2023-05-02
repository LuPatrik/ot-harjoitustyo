import pygame
def refresh_screen(screen, player_ship, enemy_ship):
    pygame.display.update()
    screen.fill((0,0,0))
    for bullet in player_ship.bullets:
        bullet.draw(screen)
    for enemy in enemy_ship.enemies:
        enemy.draw(screen)
    player_ship.draw(screen)
