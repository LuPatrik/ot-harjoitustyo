from spaceship import Spaceship
import pygame
import os
class Enemy_ship(Spaceship):
    def __init__(self, x, y, speed, health):
        super().__init__(x, y, speed, health)
        self.image = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "alien_striker.png"))
        self.image = pygame.transform.scale(self.image, (100,100))
        self.mask = pygame.mask.from_surface(self.image)
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y += self.speed