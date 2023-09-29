import pygame

def main():
    pygame.init()

    X, Y = 600, 400
    display = pygame.display.set_mode((X,Y))
    # pygame.display.update()
    pygame.display.set_caption('Life game by Fra')
    white = (255, 255, 255)
    black = (0,0,0)
    game_over = False

    # Square_size = [10, 10] #not sure if a tuple better

    while not game_over:
        drawGrid(X, Y, display, white)
        for event in pygame.event.get():
            print(event)   #prints out all the actions that take place on the screen

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def drawGrid(X,Y: int, display, white):
    blockSize = 20 #Set the size of the grid block
    for x in range(0, X, blockSize):
        for y in range(0, Y, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(display, white, rect, 1)


if __name__ == "__main__":
    main()