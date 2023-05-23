import pygame
import Textures
import Constants


class Projective:
    def __init__(self, game, x_start, y_start, direction, image_pack, damage):
        self.game = game
        self.x = x_start
        self.y = y_start
        self.damage = damage
        self.direction = direction
        self.image = pygame.image.load(image_pack).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.images = [self.image.subsurface(0, 0, 64, 64), self.image.subsurface(
            64, 0, 64, 64), self.image.subsurface(128, 0, 64, 64), self.image.subsurface(192, 0, 64, 64)]

    def render(self):
        self.game.screen.blit(self.images[self.direction], (self.x, self.y))

    def move(self):
        if self.direction == Constants.RIGHT:
            self.x += self.speed
        elif self.direction == Constants.DOWN:
            self.y += self.speed
        elif self.direction == Constants.LEFT:
            self.x -= self.speed
        elif self.direction == Constants.UP:
            self.y -= self.speed

        if self.x > Constants.SCREEN_WIDTH or self.x < -32 or self.y > Constants.SCREEN_HEIGHT or self.y < -32:
            self.remove()

        self.hits_checking()

    def hits_checking(self):
        #        if self.game.player.state != Constants.DEAD:
        #            if abs(self.game.player.x - self.x) < 32 and abs(self.game.player.y - self.y) < 32:
        #                if self.game.player.hp > 0:
        #                    self.damage(self.game.player)
        #                if self.game.player.hp <= 0:
        #                    self.game.player.dead()
        #                self.remove()
        for k in self.game.levels[self.game.level].npc:
            if k.state != Constants.DEAD:
                if abs(k.x - self.x) < 32 and abs(k.y - self.y) < 32:
                    self.remove()
                    if k.hp > 0:
                        self.damaging(k)
                    if k.hp <= 0:
                        k.dead()

    def remove(self):
        try:
            self.game.projective.remove(self)
        except ValueError:
            pass

    def damaging(self, obj):
        obj.hp -= self.damage


class Arrow(Projective):
    def __init__(self, game, x_start, y_start, direction):
        self.image = Textures.ARROW
        self.speed = 10
        self.damage = 30
        super().__init__(game, x_start, y_start, direction, self.image, self.damage)


class Fireball(Projective):
    def __init__(self, game, x_start, y_start, direction):
        self.image = Textures.FIREBALL
        self.speed = 15
        self.damage = 60
        super().__init__(game, x_start, y_start, direction, self.image, self.damage)
