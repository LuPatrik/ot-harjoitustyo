import os
import pygame
from bullet import Bullet
from spaceship import Spaceship
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
