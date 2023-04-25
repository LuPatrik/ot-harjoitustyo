import unittest
from fleet_zero import PlayerShip
from fleet_zero import EnemyShip
import fleet_zero
class TestFleetZero(unittest.TestCase):
    def test_does_player_take_correct_amount_of_damage(self):
        self.ship = PlayerShip(1,1,1,100)
        self.ship.hit(20)
        self.assertEqual(self.ship.health , 80)
    def test_does_enemy_take_correct_amount_of_damage(self):
        self.ship = EnemyShip(1,1,1,100)
        self.ship.hit(20)
        self.assertEqual(self.ship.health, 80)
    def test_does_destroying_an_enemy_give_points(self):
        self.ship = PlayerShip(1,1,1,100)
        self.ship.enemy_destroyed(10)
        self.assertEqual(self.ship.score, 10)
