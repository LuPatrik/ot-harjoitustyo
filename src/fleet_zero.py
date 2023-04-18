import pygame
import os

screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Fleet Zero")

class Spaceship:
    def __init__(self, x, y, speed, health):
        self.x = x
        self.y = y
        self.base_speed = speed
        self.health = health
        self.speed = speed
        self.current_shot_cooldown = 0
        self.shot_cooldown = 200
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
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "striker.png"))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask = pygame.mask.from_surface(self.image)
        self.mask = pygame.mask.from_surface(self.image)
        
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.current_shot_cooldown > self.shot_cooldown:
            self.current_shot_cooldown = current_time
            self.new_bullet = Bullet(self.x + self.image.get_width()/2 -5, self.y, 12)
            self.bullets.append(self.new_bullet)
class Bullet:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "bullet.png"))
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.y -= self.speed

class Enemy_ship(Spaceship):
    def __init__(self, x, y, speed, health):
        super().__init__(x, y, speed, health)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "alien_striker.png"))
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
    enemy_ship = Enemy_ship(((screen_size[0]-52)+300)/2, 50, 4, 100)
    def refresh_screen():
        pygame.display.update()
        screen.fill((0,0,0))
        for bullet in player_ship.bullets:
            bullet.draw(screen)
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


        if pygame.key.get_pressed()[pygame.K_x] or pygame.key.get_pressed()[pygame.K_SPACE]:
            player_ship.shoot()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
        for bullet in player_ship.bullets:
            bullet.update()
            
        player_ship.bullets = [bullet for bullet in player_ship.bullets if bullet.y > 0]

main()
