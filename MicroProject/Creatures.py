import Constants
import Projective
import Textures
import Hud
import Ai

import pygame


class Creatures:
    def __init__(self, game, name, start_x, start_y):
        self.images = []
        self.game = game
        self.name = name
        self.state = Constants.ALIVE
        self.direction = Constants.RIGHT
        self.x = start_x
        self.y = start_y
        self.hp = Constants.MAX_HP
        self.mp = Constants.MAX_MP
        self.moving = [0, 0, 0, 0]
        self.damage_type = [1, 0, 10, 10]

    def load_textures(self, image_pack):
        for image in image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = [temp.subsurface(0, 0, 64, 64), temp.subsurface(
                64, 0, 64, 64), temp.subsurface(128, 0, 64, 64)]
            self.images.append(i)

    def render(self):
        self.game.screen.blit(
            self.images[self.direction][self.state], (self.x, self.y))
        self.render_ui()

    def render_ui(self):
        """
        Отрисовка полос здоровья и манны у создания
        """
        Hud.Hud(self.game).render(self, ((10, 10)))

    def tick(self):
        """
        Регенерация здоровья и маны
        """
        Hud.Hud(self.game).tick(self)

    def dead(self):
        self.state = Constants.DEAD
        self.mp = 0


class Player(Creatures):
    def __init__(self, game, name, start_x, start_y):
        super().__init__(game, name, start_x, start_y)
        self.load_textures([Textures.PLAYER_RIGHT, Textures.PLAYER_DOWN,
                           Textures.PLAYER_LEFT, Textures.PLAYER_UP])

    def move(self):
        if self.state != Constants.DEAD:
            if self.moving[Constants.RIGHT] == 1:
                self.x += Constants.PLAYER_SPEED
                self.direction = Constants.RIGHT
            if self.moving[Constants.DOWN] == 1:
                self.y += Constants.PLAYER_SPEED
                self.direction = Constants.DOWN
            if self.moving[Constants.LEFT] == 1:
                self.x -= Constants.PLAYER_SPEED
                self.direction = Constants.LEFT
            if self.moving[Constants.UP] == 1:
                self.y -= Constants.PLAYER_SPEED
                self.direction = Constants.UP
        if self.hp <= 0:
            self.state = Constants.DEAD

            # Границы передвижения
            if self.x <= 0:
                self.x = 0
            if self.y <= 0:
                self.y = 0
            if self.x >= Constants.SCREEN_WIDTH - 60:
                self.x = Constants.SCREEN_WIDTH - 60
            if self.y >= Constants.SCREEN_HEIGHT - 70:
                self.y = Constants.SCREEN_HEIGHT - 70

    def shoot(self):
        if self.mp >= Constants.SKILL1_COST and self.state != Constants.DEAD and self.damage_type[0] == 1:
            self.mp -= Constants.SKILL1_COST
            if self.direction == Constants.RIGHT:
                self.__shoot__(48, 0)
            elif self.direction == Constants.DOWN:
                self.__shoot__(0, 48)
            elif self.direction == Constants.LEFT:
                self.__shoot__(-48, 0)
            elif self.direction == Constants.UP:
                self.__shoot__(0, -48)
            self.state = Constants.ALIVE

        if (self.mp >= Constants.SKILL1_COST*2 and self.state != Constants.DEAD and self.damage_type[1] == 1):
            self.mp -= Constants.SKILL1_COST*2
            if self.direction == Constants.RIGHT:
                self.__shoot__(48, 0)
            elif self.direction == Constants.DOWN:
                self.__shoot__(0, 48)
            elif self.direction == Constants.LEFT:
                self.__shoot__(-48, 0)
            elif self.direction == Constants.UP:
                self.__shoot__(0, -48)
            self.state = Constants.ALIVE

    def __shoot__(self, x, y):
        if self.damage_type[0] == 1:
            self.game.projective.append(Projective.Arrow(
                self.game, self.x + x, self.y + y, self.direction))

        if self.damage_type[1] == 1:
            self.game.projective.append(Projective.Fireball(
                self.game, self.x + x, self.y + y, self.direction))


class Demon(Creatures):
    def __init__(self, game, name, start_x, start_y, grid):
        super().__init__(game, name, start_x, start_y)
        self.load_textures([Textures.DEMON_RIGHT, Textures.DEMON_DOWN,
                           Textures.DEMON_LEFT, Textures.DEMON_UP])
        self.ai = Ai.Ai(grid)
        self.goal, self.queue, self.visited = [], [], []
        try:
            self.target_x = self.search_path()[0]*64
            self.target_y = self.search_path()[1]*64
        except TypeError:
            self.target_x = self.game.player.x//64 * 64
            self.target_y = self.game.player.y//64 * 64
        self.damage_cost = 1
        self.damaging = 0

    def render_ui(self):
        Hud.Hud(self.game).default_hud(self)

    def search_path(self):
        try:
            path = []
            self.goal, self.queue, self.visited = self.ai.choice_path(
                (self.x+32, self.y+32), (self.game.player.x+32, self.game.player.y+32))
            # self.game.render_path(self.goal, self.queue, self.visited)
            path_head, path_segment = self.goal, self.goal
            # print(self.visited)
            while path_segment and path_segment in self.visited:
                path_segment = self.visited[path_segment]
                path.append(path_segment)
            return path[:-2][-1]
        except IndexError:
            pass

    def move(self):
        if self.target_x > self.x:
            self.moving = [1, 0, 0, 0]
        if self.target_x < self.x:
            self.moving = [0, 0, 1, 0]
        if self.target_y > self.y:
            self.moving = [0, 1, 0, 0]
        if self.target_y < self.y:
            self.moving = [0, 0, 0, 1]

        if self.state != Constants.DEAD:
            if self.moving[Constants.RIGHT] == 1:
                self.x += Constants.DEMON_SPEED
                self.direction = Constants.RIGHT
            if self.moving[Constants.DOWN] == 1:
                self.y += Constants.DEMON_SPEED
                self.direction = Constants.DOWN
            if self.moving[Constants.LEFT] == 1:
                self.x -= Constants.DEMON_SPEED
                self.direction = Constants.LEFT
            if self.moving[Constants.UP] == 1:
                self.y -= Constants.DEMON_SPEED
                self.direction = Constants.UP
        try:
            if (self.target_x == self.x) and (self.target_y == self.y):
                self.target_x = self.search_path()[0]*64
                self.target_y = self.search_path()[1]*64
            self.damaging = 0
        except TypeError:
            self.moving = [0, 0, 0, 0]
            self.damage()

    def damage(self):
        if self.state != Constants.DEAD:
            self.state = Constants.SHOOT
            self.game.player.hp -= self.damage_cost

    # def check_collisions(self):
    #     #FIXME
    #     for i in self.game.levels[self.game.level].npc:
    #         if i != self:
    #             if i.x == self.x and i.y == self.y:
    #                 self.target_x = self.x + 64
    #                 self.target_y = self.y - 64
