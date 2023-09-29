import pygame, time


X, Y = 50, 40 # width, height in pixels
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)


def main():
    pygame.init()
    
    display = pygame.display.set_mode((X,Y))
    # pygame.display.update()
    pygame.display.set_caption('Life game by Fra')
    white = (255, 255, 255)
    black = (0,0,0)


    # drawGrid(X, Y, display, white, block_size)

    while True:  ##Re-enable later

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        display.fill(black)
        drawGrid(X, Y, display, white, block_size)
        
        for x in range(Nx):
            for y in range(Ny):
                drawCell(x, y, display, white, block_size)
                time.sleep(0.1)
                pygame.display.update()

def drawGrid(X, Y, display, grid_color, block_size):
    for x in range(0, X, block_size):
        for y in range(0, Y, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(display, grid_color, rect, width=1)

def drawCell(x, y, display, cell_color, block_size):
    rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, cell_color, rect, width=0)
    # fli() would be better as it only updates a portion of the display


if __name__ == "__main__":
    main()
