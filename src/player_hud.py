import os
import pygame
from game_values import GameValues
game_values = GameValues()
current_directory = os.path.dirname(__file__)
FONT_FILENAME = "PressStart2P-Regular.ttf"
font_path = os.path.join(current_directory, FONT_FILENAME)
def draw_player_lives(screen, player):
    image=pygame.image.load(os.path.join(os.path.dirname(__file__),"assets","striker.png"))
    image = pygame.transform.scale(image, (50, 50))
    next_render = 0
    for _ in range(player.lives):
        screen.blit(image, (0+next_render, 750))
        next_render+=50
def draw_player_progression(screen, player, level):
    pixel_font = pygame.font.Font(font_path, 20)
    current_score = pixel_font.render(str(player.score), True, (255, 255, 255))
    score_text = pixel_font.render("Score:", True, (255, 255, 255))
    current_level = pixel_font.render(str(level), True, (255, 255, 255))
    level_text = pixel_font.render("Level:", True, (255, 255, 255))
    screen.blit(level_text, (20,25))
    screen.blit(current_level, (140,25))
    screen.blit(score_text, (20,55))
    screen.blit(current_score, (140,55))
def draw_health_bar(screen, player):
    image=pygame.image.load(os.path.join(os.path.dirname(__file__),"assets","striker.png"))
    image = pygame.transform.scale(image, (100, 100))
    health_left = player.health / player.max_health
    health_bar_width = int(health_left * 80)
    pygame.draw.rect(screen, (255, 0, 0), (player.x_coord+10, player.y_coord+95, 80, 5))
    pygame.draw.rect(screen,(0,255,0),(player.x_coord+10,player.y_coord+95,health_bar_width,5))
