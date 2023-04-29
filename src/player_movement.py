import player_ship
import pygame
class PlayerMovement:
    def player_movement(player_ship):
        screen_size = (800,800)
        turbo = False
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            player_ship.speed = 8
            turbo = True
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
        else:
            player_ship.speed = 4
            turbo = False      
