import Creatures
import Barrier
import Textures
import Constants

import pygame
import random


class Level1:
    def __init__(self, game):
        self.game = game
        self.backround = pygame.image.load(Textures.LEVEL1_BACKGROUND)
        self.grid_matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        # self.grid = pygame.image.load(Textures.GRID)
        # self.grid.set_colorkey((255, 255, 255))

        self.objects = [Barrier.Cutted_tree(game, (329, 318)),
                        Barrier.Cutted_tree(self.game, (128, 448)),
                        Barrier.Cutted_tree(self.game, (1152, 192)),
                        Barrier.Cutted_tree(self.game, (448, 515)),
                        Barrier.Cutted_tree(self.game, (1088, 576)),
                        Barrier.Cutted_tree(self.game, (704, 192)),
                        Barrier.Tree(self.game, (384, 256)),
                        Barrier.Tree(self.game, (512, 448)),
                        Barrier.Tree(self.game, (252, 576)),
                        Barrier.Tree(self.game, (1088, 192)),
                        Barrier.Tree(self.game, (576, 576)),
                        Barrier.Tree(self.game, (512, 128)),
                        Barrier.Tree(self.game, (1024, 448)),
                        Barrier.Tree(self.game, (192, 192)),
                        Barrier.Tree(self.game, (768, 128)),
                        Barrier.Grass(
                            self.game, ((0, 0), (Constants.SCREEN_WIDTH, 64))),
                        Barrier.Grass(self.game, ((0, 0), (64, 768))),
                        Barrier.Grass(self.game, ((0, 640), (1280, 720))),
                        Barrier.Grass(self.game, ((832, 448), (896, 720))),
                        Barrier.Grass(self.game, ((896, 256), (1088, 384))),
                        Barrier.Wall(self.game, ((1216, 384), (1280, 448))),
                        Barrier.Wall(self.game, ((1216, 512), (1280, 576))), ]

        self.npc = []
        self.add_demon()

    def add_demon(self):
        self.npc.append(Creatures.Demon(
            self.game, 'Philipp', 1152, 256, self.grid_matrix))
        self.npc.append(Creatures.Demon(
            self.game, 'Philipp', 128, 256, self.grid_matrix))

    def render(self):
        self.game.screen.blit(self.backround, (0, 0))
        # self.game.screen.blit(self.grid, (0, 0))
        for i in self.objects:
            i.render()
        for i in self.npc:
            i.render()
        self.game.screen.blit(self.game.myfont.render(
            f'Time: {self.game.counter}', False, (0, 0, 0)), (1080, 10))

        # moving of npc
        for i in self.npc:
            if i.state != Constants.DEAD:
                i.move()

    def level_handle_events(self):
        for i in self.objects:
            self.action()
            i.handle_events(self.game.player)
            for j in self.npc:
                i.handle_events(j)
            for k in self.game.projective:
                i.handle_arrow(k)

    def action(self):
        if self.game.counter == 10:
            self.game.count = False
            if self.game.player.x > 1216 and 330 < self.game.player.y < 468:
                self.game.count = False
                # self.game.myfont.render()
                self.game.stop()
                self.game.next_level = True
                self.game.start()
                self.game.main_menu.level_choice_menu.level2()


class Level2:
    def __init__(self, game):
        self.game = game
        self.backround = pygame.image.load(Textures.CASTLE_BACKGROUND)
        # self.grid = pygame.image.load(Textures.GRID)
        # self.grid.set_colorkey((255, 255, 255))
        self.torch = pygame.image.load(Textures.TORCH)
        self.torch_coords = []
        for i in range(0, 30):
            self.torch_coords.append(
                (random.randint(100, 1200), random.randint(0, 700)))

        self.objects = [Barrier.Wall(self.game, ((0, 0), (Constants.SCREEN_WIDTH, 64))),
                        Barrier.Wall(self.game, ((Constants.SCREEN_WIDTH - 64, 0),
                                                 (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))),
                        Barrier.Wall(self.game, ((896, 0), (960, 128))),
                        Barrier.Wall(self.game, ((896, 256), (960, 448))),
                        Barrier.Wall(self.game, ((896, 576), (960, 720))),
                        Barrier.Wall(self.game, ((960, 320), (1152, 384))),
                        Barrier.Wall(self.game, ((128, 256), (640, 448))),
                        Barrier.Wall(self.game, ((640, 192), (768, 576))),
                        Barrier.Wall(self.game, ((0, 640), (1280, 720))),
                        Barrier.Chest(self.game, (64, 128)),
                        Barrier.Chest(self.game, (768, 128)),
                        Barrier.Chest(self.game, (384, 512)),
                        Barrier.Chest(self.game, (1024, 128)),
                        Barrier.Chest(self.game, (1088, 512)),
                        Barrier.Chest(self.game, (128, 512))]

        self.grid_matrix = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        self.npc = []

    def add_demon(self):
        self.npc.append(Creatures.Demon(
            self.game, 'Karasev', 1088, 256, self.grid_matrix))
        self.npc.append(Creatures.Demon(
            self.game, 'Koldunov', 64, 500, self.grid_matrix))

    def render(self):
        self.game.screen.blit(self.backround, (0, 0))
        # self.game.screen.blit(self.grid, (0, 0))
        for i in self.torch_coords:
            self.game.screen.blit(self.torch, i)
        for i in self.objects:
            i.render()

        for i in self.npc:
            i.render()

        for i in self.npc:
            i.move()

    def level_handle_events(self):
        for i in self.objects:
            i.handle_events(self.game.player)
            for j in self.npc:
                i.handle_events(j)
            for k in self.game.projective:
                i.handle_arrow(k)
