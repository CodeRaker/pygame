from random import randint
import pygame

class SnowCannon:
    def __init__(self, screen_x, screen_y, screen, snowcolor):
        self.snowFlakes_small = 0
        self.snowFlakes_large = 0
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.screen = screen
        self.snowcolor = snowcolor

    def spawn(self):
        self.snowFlakes_small_x = [randint(0,self.screen_x) for x in range(0,self.snowFlakes_small)]
        self.snowFlakes_small_y = [randint(-self.screen_y,-10) for y in range(0,self.snowFlakes_small)]
        self.snowFlakes_large_x = [randint(0,self.screen_x) for x in range(0,self.snowFlakes_large)]
        self.snowFlakes_large_y = [randint(-self.screen_y,-10) for y in range(0,self.snowFlakes_large)]

    def animate(self):
        self.snowFlakes_small_x = [(x + randint(0,1)) if randint(0,1) == 0 else (x - randint(0,1)) for x in self.snowFlakes_small_x]
        self.snowFlakes_large_x = [(x + randint(0,1)) if randint(0,1) == 0 else (x - randint(0,1)) for x in self.snowFlakes_large_x]

        for i in range(0, self.snowFlakes_small):
            if self.snowFlakes_small_y[i] > self.screen_y:
                self.snowFlakes_small_y[i] = randint(-self.screen_y,-10)
                self.snowFlakes_small_x[i] = randint(0, self.screen_x)
            else:
                self.snowFlakes_small_y[i] = self.snowFlakes_small_y[i] + (1 + randint(0,1))

        for i in range(0, self.snowFlakes_large):
            if self.snowFlakes_large_y[i] > self.screen_y:
                self.snowFlakes_large_y[i] = randint(-self.screen_y,-10)
                self.snowFlakes_large_x[i] = randint(0, self.screen_x)
            else:
                self.snowFlakes_large_y[i] = self.snowFlakes_large_y[i] + (1 + randint(0,1))

    def blit(self):
        for i in range(0, self.snowFlakes_small):
            pygame.draw.circle(self.screen, self.snowcolor, (self.snowFlakes_small_x[i], self.snowFlakes_small_y[i]), 2)
        for i in range(0, self.snowFlakes_large):
            pygame.draw.circle(self.screen, self.snowcolor, (self.snowFlakes_large_x[i], self.snowFlakes_large_y[i]), 4)
