import os
import pygame
class Bullet:
    def __init__(self, x_coord, y_coord, speed):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.speed = speed
        image_location = os.path.join(os.path.dirname(__file__), "assets", "bullet.png")
        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.mask = pygame.mask.from_surface(self.image)
    def draw(self, screen):
        screen.blit(self.image, (self.x_coord, self.y_coord))
    def update(self):
        self.y_coord -= self.speed