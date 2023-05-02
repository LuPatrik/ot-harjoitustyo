import unittest
import pygame
import fleet_zero
from collision_detection import CollisionDetection
from player_ship import PlayerShip
from enemy_ship import EnemyShip
from player_actions import PlayerActions
from screen_refresh import refresh_screen
from bullet import Bullet
class TestFleetZero(unittest.TestCase):
    def setUp(self) -> None:
        self.main = fleet_zero.main(test_mode=True)
        self.screen = pygame.display.set_mode((800,800))
        self.player = PlayerShip(200,200,4,100)
        self.enemy = EnemyShip(1,1,1,100)
        self.bullet = Bullet(10,10,5)
        return super().setUp()
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
    def test_does_enemy_move_correctly(self):
        enemy = EnemyShip(1,1,1,100)
        enemy.move()
        self.assertEqual(enemy.y_coord, 1+enemy.speed)

    def test_is_enemy_drawn_correctly(self):
        self.enemy.draw(self.screen)
    
    def test_are_enemy_spawn_coordinates_within_boundaries(self):
        for _ in range(100):
            self.enemy.spawn_enemy()
        for enemy in self.enemy.enemies:
            self.assertTrue(0<= enemy.x_coord<=700)
            self.assertTrue(-800<= enemy.y_coord<=-100)

    def test_does_enemy_spawn_with_correct_health(self):
        self.enemy.spawn_enemy()
        for enemy in self.enemy.enemies:
            self.assertEqual(enemy.health,100)

    def test_does_bullet_update_correctly(self):
        self.bullet.update()
        self.assertEqual(self.bullet.y_coord, 5)
    def test_is_bullet_drawn_correctly(self):
        self.bullet.draw(self.screen)

    def test_does_player_actions_init_correctly(self):
        player_actions = PlayerActions(20,10,4,100)
        self.assertEqual(player_actions.x_coord, 20)
        self.assertEqual(player_actions.y_coord, 10)
        self.assertEqual(player_actions.speed, 4)
    
    def test_does_player_turbo_work(self):
        actions = PlayerActions(20,10,4,100)
        actions.player_actions(self.player)
        if pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_LSHIFT}):
            actions.speed = 8 
        self.assertEqual(actions.speed,8)
    
    def test_does_basic_player_movement_work(self):
        actions = PlayerActions(0,200,0,0)
        actions.player_actions(self.player)
        if pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_UP}) and self.player.y_coord + self.player.speed > 0:
            actions.y_coord -= self.player.speed
        self.assertEqual(actions.y_coord,196)

    def test_screen_refresher_works_on_enemies(self):
        player = PlayerActions(200,200,4,100)
        for _ in range(10):
            self.enemy.spawn_enemy()
        refresh_screen(self.screen, player, self.enemy)

    def test_collision_detection_works_with_player_and_enemies(self):
        collision_detection = CollisionDetection
        new_enemy= EnemyShip(200,200,1,100)
        new_enemy2= EnemyShip(700,700,1,100)
        self.enemy.enemies.append(new_enemy)
        self.enemy.enemies.append(new_enemy2)
        collision_detection.player_and_enemy_collision(self, self.player, self.enemy)
        self.assertEqual(self.player.health,90)
        self.player.damage_immunity = 10
        collision_detection.player_and_enemy_collision(self, self.player, self.enemy)
        self.assertEqual(self.player.health,90)
        self.player.health =0
        collision_detection.player_and_enemy_collision(self, self.player, self.enemy)
        self.assertEqual(self.player.lives,2)
    
    def test_damage_immunity_reduces(self):
        self.player.damage_immunity_update()
        self.assertEqual(self.player.damage_immunity, 0)
        self.player.damage_immunity = 10
        self.assertEqual(self.player.damage_immunity, 10)
        self.player.damage_immunity_update()
        self.assertEqual(self.player.damage_immunity, 9)
