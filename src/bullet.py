import os
import pygame
class Bullet:
    "Vastaa luotien tiedoista"
    def __init__(self, x_coord, y_coord, speed):
        """Luokan konstruktori
            Args: 
                x_coord: määrittää aloituskohdan x-akselilla
                y_coord: määrittää aloituskohdan y-akselilla
                speed: määrittää luodin kulkunopeuden
            Näiden lisäksi konstruktori määrittää kuvatiedoston luodille.
            """
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.speed = speed
        image_location = os.path.join(os.path.dirname(__file__), "assets", "bullet.png")
        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.mask = pygame.mask.from_surface(self.image)
    def draw(self, screen):
        """Piirtää luodin ruudulle x_coord ja y_coord mukaan.
            Args:
                screen: Määrittää ruudun, johon luoti piirretään"""
        screen.blit(self.image, (self.x_coord, self.y_coord))
    def update(self):
        "Siirtää luotia eteenpäin sen nopeuden verran."
        self.y_coord -= self.speed
