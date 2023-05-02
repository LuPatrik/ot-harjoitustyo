import pygame
from player_ship import PlayerShip
class PlayerActions(PlayerShip):
    """Vastaa pelaajan antamien näppäinpainallusten suorittamisesta.
        Perii PlayerShip luokan tiedot.
            Attributes:
                x_coord: Määrittää aluksen sijainnin x-akselilla.
                y_coord: Määrittää aluksen sijainnin y-akselilla.
                speed: Määrittää pelaajan nopeuden
                health: Määrittää pelaajan elämäpisteet"""
    def __init__(self, x_coord, y_coord, speed, health):
        """Luokan konstruktori.
            Args:
                x_coord: Määrittää aluksen sijainnin x-akselilla.
                y_coord: Määrittää aluksen sijainnin y-akselilla.
                speed: Määrittää pelaajan nopeuden
                health: Määrittää pelaajan elämäpisteet"""
        super().__init__(x_coord, y_coord, speed, health)
        self.x_coord=x_coord
        self.y_coord=y_coord
        self.speed=speed
    def player_actions(self, player_ship):
        """Funktio, joka suorittaa pelaajan antamat näppäinpainallukset.
            Args:
                player_ship: Perii pelaaja-aluksen tiedot
            Vasemman shiftin painaminen laittaa turbon päälle, jolloin pelaaja-aluksen
            nopeus on 8.
            Nuolinäppäimet liikuttavat pelaajaa, jos pelaaja ei ole karkaamassa ulos peliruudusta.
            X:n tai välilyönnin painaminen ampuu. Jos turbo on päällä, ampuminen ei onnistu."""
        screen_size = (800,800)
        turbo = False
        if pygame.key.get_pressed()[pygame.K_LSHIFT]:
            player_ship.speed = 8
            turbo = True
        if pygame.key.get_pressed()[pygame.K_UP] and player_ship.y_coord + player_ship.speed > 0:
            player_ship.y_coord -= player_ship.speed
        if (pygame.key.get_pressed()[pygame.K_DOWN] and player_ship.y_coord
            + player_ship.speed + 100 < screen_size[1]):
            player_ship.y_coord += player_ship.speed
        if (pygame.key.get_pressed()[pygame.K_LEFT] and
            player_ship.x_coord - player_ship.speed > 0):
            player_ship.x_coord -= player_ship.speed
        if (pygame.key.get_pressed()[pygame.K_RIGHT] and
            player_ship.x_coord + player_ship.speed + 100 < screen_size[0]):
            player_ship.x_coord += player_ship.speed
        if ((pygame.key.get_pressed()[pygame.K_x] or
            pygame.key.get_pressed()[pygame.K_SPACE]) and not turbo):
            player_ship.shoot()
        else:
            player_ship.speed = 4
            turbo = False
