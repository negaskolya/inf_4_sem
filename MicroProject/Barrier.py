import pygame
import Textures


class Barrier:
    def __init__(self, game, position, texture):
        # position is a list ((x1,y1),(x2,y2))
        self.game = game
        self.x1 = position[0][0]
        self.x2 = position[1][0]
        self.y1 = position[0][1]
        self.y2 = position[1][1]
        self.background = pygame.image.load(texture)
        self.piece_surface = pygame.Surface((self.x2-self.x1, self.y2-self.y1))
        self.tmp = self.piece_surface.blit(self.background, (0, 0))

    def handle_events(self, obj):
        if (obj.x + 64 > self.x2 - 10 > obj.x > self.x1 - 10 and obj.y + 54 - self.y1 > 3
                and self.y2 - obj.y > 13):
            obj.x = self.x2 - 10

        if (self.x1 - 54 < obj.x < self.x1 and obj.x < self.x2 - 10 and obj.y + 54 - self.y1 > 3
                and self.y2 - obj.y > 13):
            obj.x = self.x1 - 54

        if (self.y1 - 54 < obj.y < self.y1 and obj.y < self.y2-64 and obj.x + 54 - self.x1 > 3
                and self.x2 - 10 - obj.x > 3):
            obj.y = self.y1 - 54

        if (self.y1-64 < obj.y < self.y2 - 10 < obj.y + 64 and obj.x + 54 - self.x1 > 3
                and self.x2 - 10 - obj.x > 3):
            obj.y = self.y2 - 10

    def handle_arrow(self, arrow):
        if (arrow.x + 42 > self.x1 and arrow.x + 22 < self.x2
                and arrow.y + 42 > self.y1 and arrow.y + 22 < self.y2):
            arrow.remove()

    def render(self):
        self.game.screen.blit(self.piece_surface, (self.x1, self.y1))


class Wall(Barrier):
    def __init__(self, game, position):
        super().__init__(game, position, Textures.BARRIER)


class Cutted_tree(Barrier):
    def __init__(self, game, position):
        self.game = game
        self.position = position
        self.texture = pygame.image.load(Textures.CUTTED_TREE)
        self.texture.set_colorkey((255, 255, 255))
        self.x1 = position[0]
        self.x2 = position[0]+64
        self.y1 = position[1]
        self.y2 = position[1]+64
        self.tmp_wall = Wall(
            self.game, ((self.x1, self.y1), (self.x2, self.y2)))

    def render(self):
        self.game.screen.blit(
            self.texture, (self.position[0], self.position[1]))

    def handle_arrow(self, arrow):
        pass


class Tree(Barrier):
    def __init__(self, game, position):
        self.game = game
        self.position = position
        self.texture = pygame.image.load(Textures.TREE)
        self.texture.set_colorkey((255, 255, 255))
        self.x1 = position[0]+12
        self.x2 = position[0]+52
        self.y1 = position[1]+14
        self.y2 = position[1]+54
        self.tmp_wall = Wall(
            self.game, ((self.x1, self.y1), (self.x2, self.y2)))

    def render(self):
        self.game.screen.blit(
            self.texture, (self.position[0], self.position[1]))

    def handle_arrow(self, arrow):
        pass


class Chest(Barrier):
    def __init__(self, game, position):
        self.game = game
        self.position = position
        self.texture = pygame.image.load(Textures.CHEST)
        self.texture.set_colorkey((255, 255, 255))
        self.x1 = position[0]+5
        self.x2 = position[0]+53
        self.y1 = position[1]+8
        self.y2 = position[1]+56
        self.tmp_wall = Wall(
            self.game, ((self.x1, self.y1), (self.x2, self.y2)))

    def render(self):
        self.game.screen.blit(
            self.texture, (self.position[0], self.position[1]))


class Grass(Barrier):
    def __init__(self, game, position):
        super().__init__(game, position, Textures.GRASS)
