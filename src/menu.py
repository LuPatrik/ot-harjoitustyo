import sys
import os
import pygame
from game_values import GameValues
pygame.init()
game_values = GameValues()
screen_size = game_values.screen_size
screen = pygame.display.set_mode(screen_size)
current_directory = os.path.dirname(__file__)
FONT_FILE = "PressStart2P-Regular.ttf"
font_path = os.path.join(current_directory, FONT_FILE)
class Menu():
    def __init__(self):
        title_font = pygame.font.Font(font_path, 75)
        pixel_font = pygame.font.Font(font_path, 50)
        self.menu_running = True
        self.pause_menu_running = False
        self.clock = pygame.time.Clock()
        self.title = title_font.render("Fleet Zero", True, (255, 255, 255))
        self.start_text = pixel_font.render("Start game", True, (255, 255, 255))
        self.highscores_text = pixel_font.render("Highscores", True, (255, 255, 255))
        self.quit_text = pixel_font.render("Quit", True, (255, 255, 255))
        self.resume_text = pixel_font.render("Resume", True, (255, 255, 255))
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_clicked = pygame.mouse.get_pressed()[0]
    def run_main_menu(self):
        while self.menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_clicked = pygame.mouse.get_pressed()[0]
            screen.fill((0, 0, 0))
            screen.blit(self.title, (screen_size[0] // 2 - self.title.get_width()//2,200))
            screen.blit(self.start_text, (screen_size[0] // 2 - self.start_text.get_width()//2,400))
            #screen.blit(self.highscores_text, (screen_size[0]
            #// 2 - self.highscores_text.get_width() // 2, 550))
            screen.blit(self.quit_text,(screen_size[0]//2-self.quit_text.get_width()//2,550))
            if (self.start_text.get_rect(x=screen_size[0] // 2 -
                self.start_text.get_width() // 2, y=400).collidepoint(self.mouse_pos)
                and self.mouse_clicked):
                self.menu_running = False
                break
            if (self.quit_text.get_rect(x=screen_size[0]//2-
            self.quit_text.get_width()//2,y=550).collidepoint(self.mouse_pos)
            and self.mouse_clicked):
                pygame.quit()
                sys.exit()
            pygame.display.update()
            self.clock.tick(60)
    def pause_menu(self):
        while self.pause_menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_clicked = pygame.mouse.get_pressed()[0]
            screen.fill((0, 0, 0))
            screen.blit(self.title, (screen_size[0] // 2 - self.title.get_width()//2,200))
            screen.blit(self.resume_text, (screen_size[0]//2-self.resume_text.get_width()//2,400))
            screen.blit(self.quit_text, (screen_size[0]//2-self.quit_text.get_width() // 2, 550))
            if (self.resume_text.get_rect(x=screen_size[0] // 2 -
                self.resume_text.get_width() // 2, y=400).collidepoint(self.mouse_pos)
                and self.mouse_clicked):
                self.pause_menu_running = False
                break
            if (self.quit_text.get_rect(x=screen_size[0]//2-
            self.quit_text.get_width()//2,y=550).collidepoint(self.mouse_pos)
            and self.mouse_clicked):
                pygame.quit()
                sys.exit()
            pygame.display.update()
            self.clock.tick(60)
