# coding: utf-8
import Constants
import Creatures
import Menu
import pygame
import Hud
import Level

from pygame.locals import *


class Main:
    """
    Главный класс игры, тут объявляется обработчик событий, отрисовка
    """

    def __init__(self, screen):
        self.screen = screen
        self.main_menu = Menu.MainMenu(self)
        self.gameplay_menu = Menu.GameplayMenu(self)

        self.counter = 0
        self.count = True
        self.myfont = pygame.font.Font("data/Font.ttf", 36)
        self.running = False
        self.menu_running = False
        self.next_level = False
        self.soundtrack = pygame.mixer.music.load('soundtrack.mp3')
        pygame.mixer.music.play(-1, 0.0)
        self.start()

    def handle_events(self):
        """
        Обработчик событий, в частности действий пользователя
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stop()
            elif event.type == USEREVENT+1:
                if self.player.state != Constants.DEAD:
                    self.player.tick()
                    if self.count:
                        self.counter += 1
            elif event.type == USEREVENT+2:
                self.levels[self.level].add_demon()
            # Передвижение игрока
            # При нажатии на клавиш DOWN
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    self.player.moving[0] = 1
                if event.key == K_s:
                    self.player.moving[1] = 1
                if event.key == K_a:
                    self.player.moving[2] = 1
                if event.key == K_w:
                    self.player.moving[3] = 1
                if event.key == K_SPACE:
                    if self.player.mp >= Constants.SKILL1_COST and self.player.state != Constants.SHOOT:
                        self.player.state = Constants.SHOOT
                if event.key == K_ESCAPE:
                    self.menu_running = True
                if event.key == K_1:
                    self.player.damage_type = [
                        1, 0, self.player.damage_type[2], self.player.damage_type[3]]
                if event.key == K_2:
                    self.player.damage_type = [
                        0, 1, self.player.damage_type[2], self.player.damage_type[3]]
                if event.key == K_3 and self.player.damage_type[2] > 0:
                    if self.player.hp + Constants.HP_REG < Constants.MAX_HP:
                        self.player.hp += Constants.HP_REG
                    else:
                        self.player.hp = Constants.MAX_HP
                    self.player.damage_type[2] = self.player.damage_type[2]-1
                if event.key == K_4 and self.player.damage_type[3] > 0:
                    if self.player.mp + Constants.MP_REG < Constants.MAX_MP:
                        self.player.mp += Constants.MP_REG
                    else:
                        self.player.mp = Constants.MAX_MP
                    self.player.damage_type[3] = self.player.damage_type[3]-1
            # При отжатии клавиш UP
            elif event.type == KEYUP:
                if event.key == K_d:
                    self.player.moving[0] = 0
                if event.key == K_s:
                    self.player.moving[1] = 0
                if event.key == K_a:
                    self.player.moving[2] = 0
                if event.key == K_w:
                    self.player.moving[3] = 0
                if event.key == K_SPACE:
                    self.player.shoot()

    def get_rect(self, x, y):
        return x * 64 + 1, y * 64 + 1, 64 - 2, 64 - 2

    def render_path(self, goal, visited):
        path_head, path_segment = goal, goal
        while path_segment and path_segment in visited:
            pygame.draw.rect(self.screen, pygame.Color('white'), self.get_rect(
                *path_segment), 64, border_radius=64 // 3)
            path_segment = visited[path_segment]

    def main_render(self):
        """
        Main render of all objects.
        """
        self.levels[self.level].render()
        self.player.render()
        self.perks_line.render()
        for i in self.projective:
            i.render()
        pygame.display.update()

    def main_move(self):
        self.player.move()
        self.levels[self.level].level_handle_events()
        for i in self.projective:
            i.move()
        self.handle_events()
        self.main_render()

    def start(self):
        """
        Main method of game
        """
        self.level = 0
        if not self.next_level:
            self.main_menu.start()
        self.player = Creatures.Player(
            self, "Name", Constants.START_PLAYER_X, Constants.START_PLAYER_Y)
        self.perks_line = Hud.Perks_line(self, (500, 650))
        # массив, который будет содержать в себе объекты классов стрел, огненных шаров и тд. (см. Projective)
        self.projective = []
        self.levels = [Level.Level1(self), Level.Level2(self)]
        pygame.time.set_timer(USEREVENT+1, 1000)
        pygame.time.set_timer(USEREVENT+2, 10000)
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(60)
            if self.menu_running:
                self.gameplay_menu.render(3, self.gameplay_menu.buttons_text)
                self.gameplay_menu.handle_events()
            else:
                self.main_move()
            pygame.display.set_caption(f'FPS: {int(clock.get_fps())}')
    def stop(self):
        self.running = False


pygame.init()
screen = pygame.display.set_mode(
    (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
game = Main(screen)
