from random import randint
import pygame

class SnowCannon:
    def __init__(self, screen_x, screen_y, screen, snowcolor):
        self.snowFlakes_small = 0
        self.snowFlakes_large = 0
        self.snowFlakes_size_small = 2
        self.snowFlakes_size_large = 4
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.screen = screen
        self.snowcolor = snowcolor
        self.groundfall = False
        self.groundfall_bookkeeper_small = {}
        self.groundfall_bookkeeper_large = {}

    def spawn(self):
        #Generate randomized snowflake starting xy coordinates
        self.snowFlakes_small_x = [randint(0,self.screen_x) for x in range(0,self.snowFlakes_small)]
        self.snowFlakes_small_y = [randint(-self.screen_y,-10) for y in range(0,self.snowFlakes_small)]
        self.snowFlakes_large_x = [randint(0,self.screen_x) for x in range(0,self.snowFlakes_large)]
        self.snowFlakes_large_y = [randint(-self.screen_y,-10) for y in range(0,self.snowFlakes_large)]

    def animate(self):
        #Move snowflakes from side to side
        self.snowFlakes_small_x = [(x + randint(0,1)) if randint(0,1) == 0 else (x - randint(0,1)) for x in self.snowFlakes_small_x]
        self.snowFlakes_large_x = [(x + randint(0,1)) if randint(0,1) == 0 else (x - randint(0,1)) for x in self.snowFlakes_large_x]

        #Reset small snowflakes if they fall below y axis
        for i in range(0, self.snowFlakes_small):

            #Snowflakes dont stay on ground
            if not self.groundfall:

                #Snowflake is reset because it hit ground
                if self.snowFlakes_small_y[i] > self.screen_y:
                    self.snowFlakes_small_y[i] = randint(-self.screen_y,-10)
                    self.snowFlakes_small_x[i] = randint(0, self.screen_x)

                #Snowflake has not hit ground and continues down the screen
                else:
                    self.snowFlakes_small_y[i] = self.snowFlakes_small_y[i] + (1 + randint(0,1))
            else:
                #Snowflake hit the ground and should stay for a while
                if self.snowFlakes_small_y[i] > (self.screen_y - self.snowFlakes_size_small):

                    #Snowflake is not registered by bookkeeper, so here we register with a counter
                    if not i in self.groundfall_bookkeeper_small:
                        self.groundfall_bookkeeper_small.update({i:100})

                    #Snowflake is registered by bookkeeper, so here we count down to reset
                    elif i in self.groundfall_bookkeeper_small:
                        if self.groundfall_bookkeeper_small[i] == 0:
                            self.groundfall_bookkeeper_small.pop(i)
                            self.snowFlakes_small_y[i] = randint(-self.screen_y,-10)
                            self.snowFlakes_small_x[i] = randint(0, self.screen_x)
                        else:
                            self.groundfall_bookkeeper_small[i] = self.groundfall_bookkeeper_small[i] - 1

                #Snowflake did not hit the ground yet
                else:
                    #Is not in bookkeeper and should further move down
                    if not i in self.groundfall_bookkeeper_small:
                        self.snowFlakes_small_y[i] = self.snowFlakes_small_y[i] + (1 + randint(0,1))

                    #Is still in bookkeeper and should stay on ground
                    else:
                        self.snowFlakes_small_y[i] = self.screen_y - (self.snowFlakes_size_small - 3)

        #Reset large snowflakes if they fall below y axis
        for i in range(0, self.snowFlakes_large):

            #Snowflakes dont stay on ground
            if not self.groundfall:

                #Snowflake is reset because it hit ground
                if self.snowFlakes_large_y[i] > self.screen_y:
                    self.snowFlakes_large_y[i] = randint(-self.screen_y,-10)
                    self.snowFlakes_large_x[i] = randint(0, self.screen_x)

                #Snowflake has not hit ground and continues down the screen
                else:
                    self.snowFlakes_large_y[i] = self.snowFlakes_large_y[i] + (1 + randint(0,1))
            else:
                #Snowflake hit the ground and should stay for a while
                if self.snowFlakes_large_y[i] > (self.screen_y - self.snowFlakes_size_large):

                    #Snowflake is not registered by bookkeeper, so here we register with a counter
                    if not i in self.groundfall_bookkeeper_large:
                        self.groundfall_bookkeeper_large.update({i:100})

                    #Snowflake is registered by bookkeeper, so here we count down to reset
                    elif i in self.groundfall_bookkeeper_large:
                        if self.groundfall_bookkeeper_large[i] == 0:
                            self.groundfall_bookkeeper_large.pop(i)
                            self.snowFlakes_large_y[i] = randint(-self.screen_y,-10)
                            self.snowFlakes_large_x[i] = randint(0, self.screen_x)
                        else:
                            self.groundfall_bookkeeper_large[i] = self.groundfall_bookkeeper_large[i] - 1

                #Snowflake did not hit the ground yet
                else:
                    #Is not in bookkeeper and should further move down
                    if not i in self.groundfall_bookkeeper_large:
                        self.snowFlakes_large_y[i] = self.snowFlakes_large_y[i] + (1 + randint(0,1))

                    #Is still in bookkeeper and should stay on ground
                    else:
                        self.snowFlakes_large_y[i] = self.screen_y - (self.snowFlakes_size_large - 3)

    def blit(self):
        #Draw snowflakes to pygame screen
        for i in range(0, self.snowFlakes_small):
            pygame.draw.circle(self.screen, self.snowcolor, (self.snowFlakes_small_x[i], self.snowFlakes_small_y[i]), self.snowFlakes_size_small)
        for i in range(0, self.snowFlakes_large):
            pygame.draw.circle(self.screen, self.snowcolor, (self.snowFlakes_large_x[i], self.snowFlakes_large_y[i]), self.snowFlakes_size_large)
