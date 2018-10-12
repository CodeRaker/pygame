from random import randint
import pygame as pg
from settings import *

class SnowFlake(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = snowflake_layer
        self.groups = game.all_sprites, game.snowflakes
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load('images\snowflake.png').convert_alpha()
        self.randsize = randint(3,6)
        self.image = pg.transform.scale(self.image, (self.randsize, self.randsize))
        self.rect = self.image.get_rect()
        self.rect.y = randint(-screen_y,0)
        self.rect.x = randint(0,screen_x)
        self.ttl = 500
        self.collision = False
        self.has_spawned_clone = False

    def update(self):
        if not self.collision:
            self.rect.y += 1
            self.rect.x += randint(-1,1) + self.game.windDirection
        if self.ttl == 0:
            self.kill()
            self.game.snowflakes_on_ground -= 1
        if self.rect.y > screen_y - self.rect.height:
            self.collision = True
        if self.collision == True:
            if not self.has_spawned_clone:
                SnowFlake(self.game)
                self.has_spawned_clone = True
                self.game.snowflakes_on_ground +=1
            self.ttl -= 1
        if self.rect.x > screen_x + self.rect.width:
            self.rect.x = 0
        elif self.rect.x < 0 - self.rect.width:
            self.rect.x = screen_x
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.center = center
        self.collision = False

class Town(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = ctown_layer
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load('images\dxc-building.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() // 5, self.image.get_height() // 5))
        self.rect = self.image.get_rect()
        self.rect.y = 55
        self.rect.x = 1200

    def update(self):
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.mask = pg.mask.from_surface(self.image)

class SnowGround(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 3
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load('images\snowground.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (screen_x, screen_y // 8))
        self.rect = self.image.get_rect()
        self.rect.y = 100
        self.rect.centerx = screen_x / 2

    def update(self):
        #move ground up and down
        if self.game.snowflakes_on_ground %5 == 0 and self.game.snowflakes_on_ground < 150:
            self.rect.y = 190 - (self.rect.height // 3 + self.game.snowflakes_on_ground // 2)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.mask = pg.mask.from_surface(self.image)

class Toolio(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 3
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.direction = 'left'
        self.blink = 0
        self.walk = 50
        self.image_picker = 0

        self.images = []
        self.images.append(pg.image.load('images\Joolio-OpenEyes.png').convert_alpha())
        self.images.append(pg.image.load('images\Joolio-Stand.png').convert_alpha())
        self.images.append(pg.image.load('images\Joolio-ClosedEyes.png').convert_alpha())
        self.images[0] = pg.transform.scale(self.images[0], (self.images[0].get_width() // 12, self.images[0].get_height() // 12))
        self.images[1] = pg.transform.scale(self.images[1], (self.images[1].get_width() // 12, self.images[1].get_height() // 12))
        self.images[2] = pg.transform.scale(self.images[2], (self.images[2].get_width() // 12, self.images[2].get_height() // 12))
        self.image = self.images[self.image_picker]
        self.rect = self.image.get_rect()
        self.rect.y = 55
        self.rect.centerx = screen_x // 2

    def image_update(self):
        x = self.rect.x
        y = self.rect.y
        #centerx = self.rect.centerx
        self.image = self.images[self.image_picker]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self):
        if self.direction == 'left':
            self.rect.x -= 1
            if self.rect.x < 10:
                self.direction = 'right'
        elif self.direction == 'right':
            self.rect.x += 1
            if self.rect.x > 1400:
                self.direction = 'left'

        self.walk -= 1
        if self.walk == 0 and self.image_picker in [0,2]:
            self.walk = 50
            self.image_picker = 1
            self.image_update()
        elif self.walk == 0 and self.image_picker == 1:
            self.blink += randint(0,1)
            if self.blink == 5:
                self.image_picker = 2
                self.blink = 0
            else:
                self.image_picker = 0
            self.walk = 50
            self.image_update()

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.mask = pg.mask.from_surface(self.image)
