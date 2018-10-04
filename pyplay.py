import pygame

pygame.init()

#########
# Beauty
#########

class TextObjects(object):
    def __init__(self, text):
        self.color = (255, 255, 255)
        self.text = font.render(text, True, self.color)

    def fontColor(self, color):
        if color == 'white':
            self.color = (255, 255, 255)
        elif color == 'blue':
            self.color = (0, 0, 255)
        elif color == 'red':
            self.color = (255, 0, 0)


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

text1 = font.render("INC100000345653  This is Great man  ", True, (255, 255, 255))
text2 = font.render("INC100000345653  This is AWESOME man  ", True, (255, 255, 255))

counter = 0
clicked = False
text = text1
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

        text_pos_x = 30
        text_pos_y = 30

        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(30, 30, 60, 60))

        #Draws a black screen
        screen.fill((0, 0, 0))

        #Draw select bar

        #prints text 10 times and calculates position
        for i in range(0,10):
            screen.blit(text, (text_pos_x, text_pos_y))
            text_pos_y+=(text.get_height() + 2)

        counter+=1
        counter_text = font.render(str(counter), True, (255, 255, 255))
        screen.blit(counter_text, (text_pos_x, text_pos_y))


        pygame.display.flip()
        clock.tick(60)
