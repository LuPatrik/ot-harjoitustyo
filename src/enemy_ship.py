import os
import pygame
from spaceship import Spaceship
class EnemyShip(Spaceship):
    def __init__(self, x_coord, y_coord, speed, health):
        super().__init__(x_coord, y_coord, speed, health)
        image_location = os.path.join(os.path.dirname(__file__), "assets", "alien_striker.png")
        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.mask = pygame.mask.from_surface(self.image)
        self.enemies = []
    def draw(self, screen):
        screen.blit(self.image, (self.x_coord, self.y_coord))
    def move(self):
        self.y_coord += self.speed