import os
import pygame

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