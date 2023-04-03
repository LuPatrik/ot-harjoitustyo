import pygame
import os

screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Fleet Zero")

class Spaceship:
    def __init__(self, x, y, speed, health):
        self.x = x
        self.y = y
        self.health = health
        self.speed = speed
        self.current_shot_cooldown = 0
        self.shot_cooldown = 350
        self.damage_immunity = 0

    def hit(self, damage):
        self.health -= damage
        self.damage_immunity = 20

    def damage_immunity_update(self):
        if self.damage_immunity > 0:
            self.damage_immunity -= 1

class Player_ship(Spaceship):
    def __init__(self, x, y, speed, health):
        super().__init__(x, y, speed, health)
        self.bullets = []
        self.image = pygame.image.load(os.path.join("assets", "striker.png"))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask = pygame.mask.from_surface(self.image)
        self.mask = pygame.mask.from_surface(self.image)
        
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Enemy_ship(Spaceship):
    def __init__(self, x, y, speed, health):
        super().__init__(x, y, speed, health)
        self.image = pygame.image.load(os.path.join("assets", "alien_striker.png"))
        self.image = pygame.transform.scale(self.image, (100,100))
        self.mask = pygame.mask.from_surface(self.image)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y += 2
def main():
    FPS =  60
    clock = pygame.time.Clock()
    running = True


    player_ship = Player_ship((screen_size[0]-52)/2, screen_size[1]-100, 4, 100)
    enemy_ship = Enemy_ship(((screen_size[0]-52)+300)/2, screen_size[1]-100, 4, 100)
    def refresh_screen():
        pygame.display.update()
        screen.fill((0,0,0))
        enemy_ship.draw(screen)
        player_ship.draw(screen)


    while running:
        clock.tick(FPS)
        refresh_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_ship.damage_immunity_update()

        if pygame.mask.from_surface(player_ship.image).overlap(pygame.mask.from_surface(enemy_ship.image), (int(enemy_ship.x - player_ship.x), int(enemy_ship.y - player_ship.y))):
            if player_ship.damage_immunity == 0:
                player_ship.hit(10)
                print("hit!!", player_ship.health)
                if player_ship.health == 0:
                    running = False
        

        
        if pygame.key.get_pressed()[pygame.K_UP] and player_ship.y + player_ship.speed > 0:
            player_ship.y -= player_ship.speed
        if pygame.key.get_pressed()[pygame.K_DOWN] and player_ship.y + player_ship.speed + 100 < screen_size[1]:
            player_ship.y += player_ship.speed
        if pygame.key.get_pressed()[pygame.K_LEFT] and player_ship.x - player_ship.speed > 0:
            player_ship.x -= player_ship.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT] and player_ship.x + player_ship.speed + 100 < screen_size[0]:
            player_ship.x += player_ship.speed
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

main()
