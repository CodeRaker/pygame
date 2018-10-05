import pygame

pygame.init()

#########
# Beauty
#########

class TextObjects(object):

    def __init__(self):
        self.color = (255, 255, 255)
        self.position_x = 30
        self.position_y = 30
        self.font = pygame.font.SysFont("consolas", 36)

    def setColor(self, color):
        if color == 'white':
            self.color = (255, 255, 255)
        elif color == 'blue':
            self.color = (0, 0, 255)
        elif color == 'red':
            self.color = (255, 0, 0)

    def fontSize(self, size):
        self.font = pygame.font.SysFont("consolas", size)

    def writeText(self, text):
        text = self.font.render(text, True, self.color)
        self.position_y += text.get_height() + 2
        screen.blit(text, (self.position_x, self.position_y))


#########
# Beauty
#########
screen_x = 1920
screen_y = 1080

screen = pygame.display.set_mode((screen_x, screen_y))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

font = pygame.font.SysFont("consolas", 36)


clicked = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:

                    #SPACE
                    if event.key == pygame.K_SPACE:
                        if clicked == False:
                            text = text1
                            clicked = True
                        else:
                            text = text2
                            clicked = False

                    #UP
                    if event.key == pygame.K_UP:
                        pass

                    #DOWN
                    if event.key == pygame.K_DOWN:
                        pass

        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(30, 30, 60, 60))

        #Draws a black screen
        screen.fill((0, 0, 0))

        #Draw select bar

        #prints text 10 times and calculates position
        t = TextObjects()
        for i in range(0,10):
            t.writeText('INC100000345653  This is Great man')


        pygame.display.flip()
        clock.tick(60)
