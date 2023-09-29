import pygame, time, numpy

X, Y = 60, 40 # display width, height in pixels
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)

def main():
    # generate array above and copy it here, then edit it to use as seed
    array = next_array =\
    [[0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

    iteration = 0

    print("Nx= ", Nx, " Ny= ", Ny)
    print("Seed array:")
    # for row in numpy.swapaxes(array, 0, 1):
    for row in array:
        print(row)
    # numpy.swapaxes(array, 0, 1) ###
    print()
    print(array)
    print()
    pygame.init()

    display = pygame.display.set_mode((X, Y))

    # pygame.transform.rotate(display, 90)

    pygame.display.set_caption('Life game by Fra')

    # display.blit(pygame.transform.rotate(display, 90), (0, 0))

    time.sleep(0.8)
    drawGrid(Nx, Ny, display)
    time.sleep(0.8)


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # display.fill(black)
        # drawGrid(X, Y, display, white, block_size)

        for x in range(Nx):
            for y in range(Ny):
                if array[x][y] == 1:
                    cell_on(x, y, block_size, display)
                else:
                    cell_off(x, y, block_size, display)

        time.sleep(0.1)
        print(iteration)
        iteration += 1

def drawGrid(Nx, Ny, display):
    for x in range(Nx):
        for y in range(Ny):
            cell_off(x, y, block_size, display)


def cell_on(x, y, block_size, display):
    filled_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, (255, 255, 255), filled_rect, width=0)
    pygame.display.flip()
    # time.sleep(0.02)


def cell_off(x, y, block_size, display):
    filled_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, (255, 255, 255), filled_rect, width=1)
    pygame.display.flip()
    # time.sleep(0.02)

    
if __name__ == "__main__":
    main()