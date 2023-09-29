import pygame

pygame.init()
dis=pygame.display.set_mode((600,400))
# pygame.display.update()
pygame.display.set_caption('Life game by Fra')
game_over=False

while not game_over:
    for event in pygame.event.get():
        print(event)   #prints out all the actions that take place on the screen

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()