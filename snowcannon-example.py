import pygame
from random import randint
from colorpalette import RGBColors
from snowcannon import SnowCannon

##
# PYGAME INIT
##
pygame.init()
rgb = RGBColors()
screen_x = 400
screen_y = 300
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("SnowFall")

##
# SnowCannon
##
snowCannon = SnowCannon(screen_x, screen_y, screen, rgb.white)
snowCannon.snowFlakes_small = 25
snowCannon.snowFlakes_large = 10
snowCannon.groundfall = True
snowCannon.spawn()

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(rgb.christmasblue)
    snowCannon.animate()
    snowCannon.blit()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
