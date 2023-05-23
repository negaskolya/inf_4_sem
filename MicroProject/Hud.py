import pygame
import Textures
import Constants


class Hud:
    def __init__(self, game):
        self.hp_frame = pygame.image.load(Textures.HUD_HP)
        self.mana_frame = pygame.image.load(Textures.HUD_MANA)
        self.hp_tick = pygame.image.load(Textures.HUD_HP_TICK)
        self.mana_tick = pygame.image.load(Textures.HUD_MANA_TICK)
        self.game = game
        self.hp_tick = pygame.image.load(Textures.HUD_HP_TICK)

    def render(self, obj, position):
        x = position[0]
        y = position[1]
        self.game.screen.blit(self.hp_frame, (x, y))
        self.game.screen.blit(self.mana_frame, (x, y+20))
        m = 0
        while m <= 388 * obj.mp / Constants.MAX_MP:
            self.game.screen.blit(self.mana_tick, (x+3+m, y+24))
            m += 1

        m = 0
        while m <= 388 * obj.hp/Constants.MAX_HP:
            self.game.screen.blit(self.hp_tick, (x+3+m, y+4))
            m += 1

    def tick(self, object):
        """Регенерация здоровья и маны"""
        if object.mp + Constants.MP_REG < Constants.MAX_MP:
            object.mp += Constants.MP_REG
        else:
            object.mp = Constants.MAX_MP

        if object.hp + Constants.HP_REG < Constants.MAX_HP:
            object.hp += Constants.HP_REG
        else:
            object.hp = Constants.MAX_HP

    def default_hud(self, obj):
        self.game.screen.blit(pygame.image.load(
            Textures.HP_FRAME).convert_alpha(), (obj.x + 12, obj.y + 58))
        self.game.screen.blit(pygame.image.load(
            Textures.MP_FRAME).convert_alpha(), (obj.x + 12, obj.y + 58 + 6))
        m = 0
        while m <= 40*obj.hp/ Constants.MAX_HP:
            self.game.screen.blit(pygame.image.load(
                Textures.HP_TICK), (obj.x + 12 + m, obj.y + 59))
            m += 1
        m = 0
        while m <= 40*obj.mp/ Constants.MAX_MP:
            self.game.screen.blit(pygame.image.load(
                Textures.MP_TICK), (obj.x + 12 + m, obj.y + 59 + 6))
            m += 1


class Perks_line():
    def __init__(self, game, position):
        #position is array (x,y)
        self.game = game
        self.x = position[0]
        self.y = position[1]
        self.frame = pygame.image.load(Textures.HUD_FRAME)
        self.frame.set_colorkey((255, 255, 255))
        self.grey_frame = pygame.image.load(Textures.HUD_FRAME_CHOSEN)
        self.grey_frame.set_colorkey((255, 255, 255))
        self.arrow = pygame.image.load(Textures.PERK_ARROW)
        self.fireball = pygame.image.load(Textures.PERK_FIREBALL)
        self.hp_potion = pygame.image.load(Textures.HP_POTION)
        self.mp_potion = pygame.image.load(Textures.MP_POTION)
        self.font = pygame.font.Font("data/Font.ttf", 10)
        self.White = (255, 255, 255)
        self.buttons_text = [self.font.render("1", True, self.White), self.font.render("2", True, self.White),
                             self.font.render("3", True, self.White), self.font.render("4", True, self.White), self.font.render("5", True, self.White)]

    def render(self):
        self.potions_number = [self.font.render(str(self.game.player.damage_type[2]), True, self.White),
                               self.font.render(str(self.game.player.damage_type[3]), True, self.White)]
        self.game.screen.blit(self.arrow, (self.x, self.y+1))
        self.game.screen.blit(self.fireball, (self.x + 63, self.y+1))
        self.game.screen.blit(self.hp_potion, (self.x + 2*63, self.y+1))
        self.game.screen.blit(self.mp_potion, (self.x + 3*63, self.y+1))
        for i in range(0, 4):
            self.game.screen.blit(self.frame, (self.x + 62*i, self.y))
            self.game.screen.blit(
                self.buttons_text[i], (self.x + 62*i + 2, self.y + 1))
        for i in range(0, 2):
            self.game.screen.blit(
                self.potions_number[i], (self.x + 62*(2+i)+52, self.y+53))
        if self.game.player.damage_type[0] == 1:
            self.game.screen.blit(self.grey_frame, (self.x, self.y))
        if self.game.player.damage_type[1] == 1:
            self.game.screen.blit(self.grey_frame, (self.x + 62, self.y))
