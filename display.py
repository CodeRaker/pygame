import pygame as pg
from settings import *

class Display(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 4
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load('images\display-background.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (1545, 913))
        self.rect = self.image.get_rect()
        self.rect.y = 160
        self.rect.x = 0

    def update(self):
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.mask = pg.mask.from_surface(self.image)

class Widget(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 4
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load('images\widget-background.png').convert_alpha()
        self.image = pg.transform.scale(self.image, ((screen_x // 5) * 1, 1069))
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 1530

    def update(self):
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.mask = pg.mask.from_surface(self.image)
