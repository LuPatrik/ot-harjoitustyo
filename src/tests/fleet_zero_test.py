import unittest
from fleet_zero import Player_ship

class TestFleetZero(unittest.TestCase):
    def test_does_test_work(self):
        self.assertEqual("here", "here")

    def test_does_player_take_correct_amount_of_damage(self):
        
        self.ship = Player_ship(1,1,1,100)
        self.ship.hit(20)
        self.assertEqual(self.ship.health , 80)

    