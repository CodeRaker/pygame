import pygame as pg
from random import randint
from colorpalette import RGBColors
from snowflakes import *
from settings import *
from display import *

class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((screen_x, screen_y))
        pg.display.set_caption("SnowFall")
        self.clock = pg.time.Clock()
        self.rgb = RGBColors()
        self.running = True
        self.frameRate = 60
        self.windTime = randint(0,self.frameRate*60)
        self.windDirection = randint(-1,1)
        self.snowflakes_count = 100
        self.snowflakes_on_ground = 0
        self.myfont = pg.font.SysFont('Consolas', 130)
        self.textsurface = self.myfont.render('Tools INCIDENTS', False, (255, 255, 255))
        self.background = pg.image.load('images/mili.jpg').convert()
        self.background = pg.transform.scale(self.background, (screen_x, screen_y))
        self.logo = pg.image.load('images/tools-logo.png').convert()
        self.logo.set_colorkey((255,255,255))


    def spawn_assets(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.snowflakes = pg.sprite.Group()
        #self.snowground = SnowGround(self)
        self.town = Town(self)
        self.toolio = Toolio(self)
        self.display = Display(self)
        self.widget = Widget(self)
        self.run()

    def run(self):
        #Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(self.frameRate)
            self.events()
            self.weather()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def weather(self):
        if self.windTime != 0:
            self.windTime -= 1
        elif self.windTime == 0:
            self.windTime = randint(0,self.frameRate*60)
            self.windDirection = randint(-1,1)

    def update(self):
        self.all_sprites.update()
        if self.snowflakes_count != 0:
            SnowFlake(self)
            self.snowflakes_count -= 1
        snowflake_hits = pg.sprite.spritecollide(self.town, self.snowflakes, False, pg.sprite.collide_mask)
        #snowflake_snowground_hits = pg.sprite.spritecollide(self.snowground, self.snowflakes, False, pg.sprite.collide_mask)
        snowflake_toolio_hits = pg.sprite.spritecollide(self.toolio, self.snowflakes, False, pg.sprite.collide_mask)
        snowflake_widget_hits = pg.sprite.spritecollide(self.widget, self.snowflakes, False, pg.sprite.collide_mask)
        snowflake_display_hits = pg.sprite.spritecollide(self.display, self.snowflakes, False, pg.sprite.collide_mask)
        if snowflake_hits:
            for s in snowflake_hits:
                s.collision = True
        # if snowflake_snowground_hits:
        #     for s in snowflake_snowground_hits:
        #         s.collision = True
        if snowflake_toolio_hits:
            for s in snowflake_toolio_hits:
                s.collision = True
        if snowflake_display_hits:
            for s in snowflake_display_hits:
                s.collision = True
        if snowflake_widget_hits:
            for s in snowflake_widget_hits:
                s.collision = True

    def draw(self):
        #self.screen.fill(self.rgb.white)
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.logo,(30,50))
        #self.screen.blit(self.textsurface,(30,50))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

g = Game()
while g.running:
    g.spawn_assets()
pg.quit()
