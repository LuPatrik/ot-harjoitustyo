import os
import random
import pygame
from spaceship import Spaceship
class EnemyShip(Spaceship):
    """Luokka, joka vastaa vihollisaluksista. Perii Spaceship luokan tiedot."""
    def __init__(self, x_coord, y_coord, speed, health):
        """Luokan konstruktori.
            Args:
                x_coord: Määrittää aluksen sijainnin x-akselilla.
                y_coord: Määrittää aluksen sijainnin y-akselilla.
                speed: Määrittää aluksen nopeuden
                health: Määrittää aluksen elämäpisteet
            Näiden lisäksi konstruktori määrittää vihollisaluksen kuvatiedoston
            ja tyhjän listan, johon kaikki vihollisalukset voidaan tallettaa muistiin."""
        super().__init__(x_coord, y_coord, speed, health)
        image_location = os.path.join(os.path.dirname(__file__), "assets", "alien_striker.png")
        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, (100,100))
        self.enemies = []
    def draw(self, screen):
        """Funktio, joka piirtää vihollisaluksen kuvan ruudulle. Piirtää kuvan sinne, minne
            aluksen koordinaatit osoittavat.
            Args:
                screen: Määrittää ruudun, johon pelaajan alus piirretään
            """
        screen.blit(self.image, (self.x_coord, self.y_coord))
    def move(self):
        "Siirtää vihollisaluksen sen nopeuden verran etenemään ruudulla"
        self.y_coord += self.speed
    def spawn_enemy(self):
        """Luo uuden vihollisen satunnaisesti valitulle alueelle, 
        joka on x-akselin 0-700 ja y-akselin -800 - -100 alueella.
        Vihollisealukset luodaan enintään -100 y-akselilla, koska muuten
        ne voivat ilmestyä tyhjästä peliruudulle."""
        x_coord = random.randint(0, 700)
        y_coord = random.randint(-800, -100)
        speed = 1
        health = 100
        new_enemy_ship = EnemyShip(x_coord, y_coord, speed, health)
        self.enemies.append(new_enemy_ship)
    def enemies_advance(self):
        """Siirtää kaikkia vihollisaluslistan vihollialuksia eteenpäin oman nopeutensa verran."""
        for enemy in self.enemies:
            enemy.move()
