import pygame
from player_ship import PlayerShip
from enemy_ship import EnemyShip
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Fleet Zero")
def main():
    fps =  60
    clock = pygame.time.Clock()
    running = True
    player_ship = PlayerShip((screen_size[0]-52)/2, screen_size[1]-100, 4, 100)
    enemy_ship = EnemyShip(((screen_size[0]-52)+300)/2, 50, 1, 100)
    def refresh_screen():
        pygame.display.update()
        screen.fill((0,0,0))
        for bullet in player_ship.bullets:
            bullet.draw(screen)
        enemy_ship.draw(screen)
        player_ship.draw(screen)
    while running:
        clock.tick(fps)
        refresh_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_ship.damage_immunity_update()
        if pygame.mask.from_surface(player_ship.image).overlap(
            pygame.mask.from_surface(enemy_ship.image),
            (int(enemy_ship.x_coord-player_ship.x_coord),
            int(enemy_ship.y_coord-player_ship.y_coord))
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
        if pygame.key.get_pressed()[pygame.K_x] or pygame.key.get_pressed()[pygame.K_SPACE]:
            player_ship.shoot()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
        for bullet in player_ship.bullets:
            if (pygame.mask.from_surface(bullet.image).
                overlap(pygame.mask.from_surface(enemy_ship.image),
                (int(enemy_ship.x_coord - bullet.x_coord),
                 int(enemy_ship.y_coord - bullet.y_coord)))):
                enemy_ship.hit(10)
                player_ship.bullets.remove(bullet)
                print("enemy hit!!", enemy_ship.health)
            bullet.update()
        enemy_ship.move()
        player_ship.bullets = [bullet for bullet in player_ship.bullets if bullet.y_coord > 0]
main()
