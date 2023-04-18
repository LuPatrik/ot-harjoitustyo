import unittest
from fleet_zero import PlayerShip
from fleet_zero import EnemyShip

class TestFleetZero(unittest.TestCase):
    def test_does_player_take_correct_amount_of_damage(self):
        self.ship = PlayerShip(1,1,1,100)
        self.ship.hit(20)
        self.assertEqual(self.ship.health , 80)
    def test_does_enemy_take_correct_amount_of_damage(self):
        self.ship = EnemyShip(1,1,1,100)
        self.ship.hit(20)
        self.assertEqual(self.ship.health, 80)
