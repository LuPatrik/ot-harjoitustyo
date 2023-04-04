import unittest
import pygame
import os
from fleet_zero import Player_ship

class TestFleetZero(unittest.TestCase):
    def test_does_test_work(self):
        self.assertEqual("here", "here")

    def test_does_player_take_dmg(self):
        
        self.ship = Player_ship(1,1,1,100)
        self.image = pygame.image.load(os.path.join("src","assets", "striker.png"))
        self.ship.hit(20)
        self.assertEqual(self.ship.health , 80)

    