
# example blinker code, it was missing the display.fill([0,0,0,]) to make it work
import pygame, time
# stop indexing arrays the weird way for ease of printing

# At some point ask user input for array size Nx, Ny
X, Y = 50, 40 # display width, height in pixels
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)


def main():
    array_full = \
    [[0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]]

    array_empty = \
    [[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

    array = [row[:] for row in array_empty]

    iteration = 0
    
    print("Nx= ", Nx, " Ny= ", Ny)
    print("Seed array: ", end=" ")
    for row in array:
        print(row)

    print()

    pygame.init()

    display = pygame.display.set_mode((X, Y))

    pygame.display.set_caption('Life game by Fra')
    drawGrid(Nx, Ny, display)

    while True:

        display.fill([0,0,0])#([255,255,255])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        for x in range(Nx):
            for y in range(Ny):
                if array[x][y] == 1:
                    cell_on(x, y, block_size, display)
                elif array[x][y] == 0: #se:
                    cell_off(x, y, block_size, display)

        print(iteration)
        if iteration % 2 == 0:
            print("Even")
            array = [row[:] for row in array_full]
        else:
            print("Odd")
            array = [row[:] for row in array_empty]

        iteration += 1
        time.sleep(0.3)
    

def drawGrid(Nx, Ny, display):
    for x in range(Nx):
        for y in range(Ny):
            cell_off(x, y, block_size, display)
            time.sleep(0.025)
    time.sleep(0.7)
    # for x in range(Nx):
    #     for y in range(Ny):
    #         cell_on(x, y, block_size, display)
    #         time.sleep(0.02)
    # time.sleep(0.4)

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
