import pygame, time

X, Y = 50, 40
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)

# x, y = 0, 0

def main():

    pygame.init()
    
    display = pygame.display.set_mode((X,Y))
    # pygame.display.update()
    pygame.display.set_caption('Rect testing')
    # white = (255, 255, 255)
    # black = (0,0,0)

    while True:  ##Re-enable later

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # just a demo
        empty_rect = pygame.Rect(0, 0, block_size, block_size)
        pygame.draw.rect(display, (255, 255, 255), empty_rect, width=1)

        filled_rect = pygame.Rect(0+block_size, 0+block_size, block_size, block_size)
        pygame.draw.rect(display, (255, 255, 255), filled_rect, width=0)

        pygame.display.update()
        time.sleep(0.2)

    # 
        # make everything black
        display.fill((0,0,0))
        pygame.display.update()
        time.sleep(0.2)

    # 

        # for x in range(Nx):
        #     for y in range(Ny):
        #         empty_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        #         pygame.draw.rect(display, (255, 255, 255), empty_rect, width=1)
        #         pygame.display.update()
        #         time.sleep(0.05)

        # # 
        

        # for x in range(Nx):
        #     for y in range(Ny):
        #         filled_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        #         pygame.draw.rect(display, (255, 255, 255), filled_rect, width=0)
        #         pygame.display.update()
        #         time.sleep(0.05)

        # # make everything black
        # display.fill((0,0,0))
        # pygame.display.update()
        # time.sleep(0.2)

    #  update cells from a list:
        array = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]] 

        array2 = [[1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1]]          
    
        # array2 = [[1, 0, 1, 0, 0],
        #          [0, 1, 0, 0, 0],
        #          [0, 0, 1, 0, 0],
        #          [0, 0, 0, 0, 0]]

        for x in range(Nx):
            for y in range(Ny):
                if array[y][x] != array2[y][x]:
                    print("updating cells")

                    if array[y][x] == 0:
                        cell_on(x, y, block_size, display)
                        print("cell on")
                    else:
                        cell_off(x, y, block_size, display)
                        print("cell off")
        time.sleep(1.5)


def cell_on(x, y, block_size, display):
    filled_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, (255, 255, 255), filled_rect, width=0)
    pygame.display.update()
    time.sleep(0.05)


def cell_off(x, y, block_size, display):
    filled_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, (255, 255, 255), filled_rect, width=0)
    pygame.display.update()
    time.sleep(0.05)


if __name__ == "__main__":
    main()
