import pygame as pg
from random import randint
from colorpalette import RGBColors
from snowcannon_new import SnowCannon
from settings import *

class ToolsMonitor:
    def __init__(self):
        pg.init()
        pg.display.set_caption("SnowFall")
        self.screen = pg.display.set_mode((screen_x, screen_y))
        self.clock = pg.time.Clock()
        self.rgb = RGBColors()
        self.load_assets()
        self.running = True
    #    self.frameCount = 0
        self.frameRate = 60
    #    self.gameTimer = 0
        self.windTime = randint(0,self.frameRate*60)
        self.windDirection = randint(-1,1)

    def weather(self):
        if self.windTime != 0:
            self.windTime -= 1
        elif self.windTime == 0:
            self.windTime = randint(0,self.frameRate*60)
            self.windDirection = randint(-1,1)

    def load_assets(self):
        self.snowflakes = []
        self.snowflake_count = 100
        for s in range (0,self.snowflake_count):
            s = SnowCannon(screen_x, screen_y, self.snowflakes)
            self.snowflakes.append(s)
        self.ctown = pg.image.load('christmas-town.png')
        self.ctown_rect = self.ctown.get_rect()
        self.ctown_pos = (((screen_x - self.ctown_rect.width) / 2), (screen_y - self.ctown_rect.height))

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def next(self):
        self.screen.fill(self.rgb.christmasblue)
        self.screen.blit(self.ctown, self.ctown_pos)
        self.weather()
        for s in self.snowflakes:
            s.animate(self.screen, self.windDirection)
        pg.display.flip()
        print(len(self.snowflakes))
        self.clock.tick(self.frameRate)

    #    if self.frameCount == self.frameRate:
    #        self.frameCount = 0
    #        self.gameTimer += 1

t = ToolsMonitor()
while t.running:
    t.events()
    t.next()
pg.quit()
