import pygame
from pygame.locals import *

from Constants import *


class Menu:
    def __init__(self, game):
        self.game = game
        self.backround = pygame.image.load(
            "data/menu_data/menu_background.jpg")
        self.backround = pygame.transform.scale(
            self.backround, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.menu_buttons = [pygame.image.load("data/menu_data/button_process.png"), pygame.image.load(
            "data/menu_data/button_off.png"), pygame.image.load("data/menu_data/button_pressed.png")]
        self.font = pygame.font.Font("data/Font.ttf", 36)

    def render(self, n, buttons_text):
        self.game.screen.blit(self.backround, (0, 0))
        for i in range(0, n):
            self.game.screen.blit(
                self.menu_buttons[self.buttons_pressed[i]], (490, 100+150*i))
            self.game.screen.blit(buttons_text[i], (550, 175 + 150*i))
        pygame.display.update()


class LevelChoiceMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.buttons_text = [self.font.render("        Level 1", True, Yellow), self.font.render(
            "        Level 2", True, Yellow), self.font.render("        Back", True, Yellow)]
        self.buttons_pressed = [0, 0, 0]
        self.running = True

    def level2(self):
        self.game.level = 1
        self.stop()
        self.game.running = True
        self.game.menu_running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    self.game.main_menu.running = True
                    self.game.main_menu.start()
            if event.type == pygame.MOUSEMOTION:
                for i in range(0, 3):
                    if (event.pos[0] > 498) and (event.pos[0] < 788) and (event.pos[1] > 160 + 150*i) and (event.pos[1] < 160 + 75*(i+1) + 75*i):
                        self.buttons_pressed[i] = 1
                    else:
                        self.buttons_pressed[i] = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, 3):
                    if (event.pos[0] > 498) and (event.pos[0] < 788) and (event.pos[1] > 160 + 150*i) and (event.pos[1] < 160 + 75*(i+1) + 75*i):
                        self.buttons_pressed[i] = 2
                    else:
                        self.buttons_pressed[i] = 0
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(0, 3):
                    if (event.pos[0] > 498) and (event.pos[0] < 788) and (event.pos[1] > 160 + 150*i) and (event.pos[1] < 160 + 75*(i+1) + 75*i):
                        self.buttons_pressed[i] = 1
                        if i == 0:
                            self.game.level = 0
                            self.stop()
                            self.game.running = True
                            self.game.menu_running = False
                        if i == 1:
                            self.game.level = 1
                            self.stop()
                            self.game.running = True
                            self.game.menu_running = False
                        if i == 2:  # обработка выхода из игры через меню
                            self.stop()
                            self.game.main_menu.start()
                    else:
                        self.buttons_pressed[i] = 0

    def start(self):
        self.running = True
        while self.running:
            self.render(3, self.buttons_text)
            self.handle_events()

    def stop(self):
        self.running = False


class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.buttons_text = [self.font.render("New Game", True, Yellow), self.font.render(
            "Choose level", True, Yellow), self.font.render("        Exit", True, Yellow)]
        self.buttons_pressed = [0, 0, 0]
        self.running = True

        self.level_choice_menu = LevelChoiceMenu(game)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                for i in range(0, 3):
                    if (event.pos[0] > 498) and (event.pos[0] < 788) and (event.pos[1] > 160 + 150*i) and (event.pos[1] < 160 + 75*(i+1) + 75*i):
                        self.buttons_pressed[i] = 1
                    else:
                        self.buttons_pressed[i] = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, 3):
                    if (event.pos[0] > 498) and (event.pos[0] < 788) and (event.pos[1] > 160 + 150*i) and (event.pos[1] < 160 + 75*(i+1) + 75*i):
                        self.buttons_pressed[i] = 2
                    else:
                        self.buttons_pressed[i] = 0
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(0, 3):
                    if (event.pos[0] > 498) and (event.pos[0] < 788) and (event.pos[1] > 160 + 150*i) and (event.pos[1] < 160 + 75*(i+1) + 75*i):
                        self.buttons_pressed[i] = 1
                        if i == 0:  # обработка нажатия на кнопку New Game
                            self.stop()
                            self.game.running = True
                            self.game.menu_running = False
                        if i == 1:  # обработка нажатия кнопки выбора левла
                            self.stop()
                            self.level_choice_menu.start()
                        if i == 2:  # обработка выхода из игры через меню
                            self.stop()
                    else:
                        self.buttons_pressed[i] = 0

    def start(self):
        self.running = True
        while self.running:
            self.render(3, self.buttons_text)
            self.handle_events()

    def stop(self):
        self.running = False


class GameplayMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.buttons_text = [self.font.render("   Continue", True, Yellow), self.font.render(
            "Main Menu", True, Yellow), self.font.render("        Exit", True, Yellow)]
        self.buttons_pressed = [0, 0, 0]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.game.menu_running = False
            if event.type == pygame.MOUSEMOTION:
                for i in range(0, 3):
                    if (event.pos[0] > 498) and (event.pos[0] < 788) and (event.pos[1] > 160 + 150*i) and (event.pos[1] < 160 + 75*(i+1) + 75*i):
                        self.buttons_pressed[i] = 1
                    else:
                        self.buttons_pressed[i] = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(0, 3):
                    if (event.pos[0] > 498) and (event.pos[0] < 788) and (event.pos[1] > 160 + 150*i) and (event.pos[1] < 160 + 75*(i+1) + 75*i):
                        self.buttons_pressed[i] = 2
                    else:
                        self.buttons_pressed[i] = 0
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(0, 3):
                    if (event.pos[0] > 498) and (event.pos[0] < 788) and (event.pos[1] > 160 + 150*i) and (event.pos[1] < 160 + 75*(i+1) + 75*i):
                        self.buttons_pressed[i] = 1
                        if i == 0:
                            self.buttons_pressed[i] = 1
                            self.game.menu_running = False
                            self.game.running = True
                        if i == 1:
                            self.game.running = False
                            self.game.stop()
                            self.game.start()
                        if i == 2:
                            self.game.running = False
                    else:
                        self.buttons_pressed[i] = 0
