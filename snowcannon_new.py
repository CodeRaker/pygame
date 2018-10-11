from random import randint
import pygame

class SnowCannon:
    def __init__(self, screen_x, screen_y, snowflakes):
        self.size = randint(2,3)
        self.x = randint(0,screen_x)
        self.y = randint(-screen_y,0)
        self.color = (255,255,255)
        self.snowflakes = snowflakes
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.ttl = 1000
        self.has_spawned_clone = False

    def animate(self, screen, wind):
        #snowflake is in air
        if self.ttl == 1000:
            self.y += 1
            self.x += (randint(-1,1) + wind)

        #snowflake exits x-axis and is reset
        if self.x > self.screen_x:
            self.x = 0
        elif self.x < 0:
            self.x = self.screen_x

        #snowflake hits ground
        if self.y > self.screen_y:
            self.ttl -= 1

            #create new snowflake, while on ground
            if self.has_spawned_clone == False:
                s = SnowCannon(self.screen_x, self.screen_y, self.snowflakes)
                self.snowflakes.append(s)
                self.has_spawned_clone = True

            #on-ground timer has expired and object deletes itself
            if self.ttl == 0:
                self.snowflakes.remove(self)
                return

        #draw snowflake
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
