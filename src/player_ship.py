import os
import pygame
from bullet import Bullet
from spaceship import Spaceship
class PlayerShip(Spaceship):
    """Luokka, joka vastaa pelaajan ohjaamasta aluksesta.
            Attributes:
                x_coord: Määrittää aluksen sijainnin x akselilla.
                y_coord: Määrittää aluksen sijainnin y akselilla.
                speed: Määrittää aluksen nopeuden
                health: Määrittää aluksen elämäpisteet"""
    def __init__(self, x_coord, y_coord, speed, health):
        """Luokan konstruktori. Perii Spaceship luokalta tietoja.
            Args:
                x_coord: Määrittää aluksen sijainnin x akselilla.
                y_coord: Määrittää aluksen sijainnin y akselilla.
                speed: Määrittää aluksen nopeuden
                health: Määrittää aluksen elämäpisteet
            
            Näiden lisäksi konstruktori asettaa kuvan pelaajan alukselle, 
            aloituspisteet, ammukset ja lisäelämät"""
        super().__init__(x_coord, y_coord, speed, health)
        self.image=pygame.image.load(os.path.join(os.path.dirname(__file__),"assets","striker.png"))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.bullet = Bullet(self.x_coord + self.image.get_width()/2 -5, self.y_coord, 12)
        self.score = 0
        self.bullets = []
        self.lives = 3
    def draw(self, screen):
        """Funktio, joka piirtää pelaaja-aluksen kuvan ruudulle. Piirtää kuvan sinne, minne
            aluksen koordinaatit osoittavat.
            Args:
                screen: Määrittää ruudun, johon pelaajan alus piirretään
            """
        screen.blit(self.image, (self.x_coord, self.y_coord))
    def shoot(self):
        """Funktio, joka hoitaa pelaajan ampumisen. Ottaa nykyisen ajan muistiin. Miinustaa nykyisestä
        ajasta tämän hetkisen ampumisen viilentymisajan ja jos se on pienempi kuin aluksen ampumisnopeus,
        ei tapahdu mitään. Jos se on suurempi kuin aluksen ampumisnopeus,
        uusi ampuminen voidaan suorittaa. Tällöin asetetaan uusi tämän hetkinen ampumisen viilentymisaika
        ja lisätään luotilistaan uusi luoti muistiin."""
        current_time = pygame.time.get_ticks()
        if current_time - self.current_shot_cooldown > self.shot_cooldown:
            self.current_shot_cooldown = current_time
            new_bullet = Bullet(self.x_coord + self.image.get_width()/2 -5, self.y_coord, 12)
            self.bullets.append(new_bullet)
    def enemy_destroyed(self, score):
        """Vastaa pisteistä, jotka pelaaja saa, kun tuhoaa vihollisaluksen.
            Args:
                score: Lisää tämän määrän pisteitä pelaajan yhteispisteisiin."""
        self.score += score
    def bullet_list_updater(self):
        """Poistaa luotilistasta kaikki luodit, jotka pääsevät peliruudun ylälaidasta pois näkyvistä."""
        self.bullets = [bullet for bullet in self.bullets if bullet.y_coord > -20]
