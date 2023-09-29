# keeping arrays local to main()
import pygame, time, numpy

X, Y = 60, 40 # display width, height in pixels
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)

def main():
    # generate array above and copy it here, then edit it to use as seed
    array =\
    [[0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

    # next_array = array.copy()
    next_array = [row[:] for row in array]

    # next_array =\
    # [[0, 0, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0]]

    iteration = 0

    print("Nx= ", Nx, " Ny= ", Ny)
    print("Seed array when iteration = 0")

    pygame.init()

    display = pygame.display.set_mode((X, Y))

    pygame.display.set_caption('Life game by Fra')
    drawGrid(Nx, Ny, display)
    time.sleep(0.8)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # display.fill(black)
        # drawGrid(X, Y, display, white, block_size)

        # Print array again to check if it assigned correctly at the end of last cycle:
        print(f"Array #{iteration}")
        for row in array:
            print(row)
        print()
        for x in range(Nx):
            for y in range(Ny):
                if array[x][y] == 1:
                    cell_on(x, y, block_size, display)
                elif array[x][y] == 0: #se:
                    cell_off(x, y, block_size, display)

        next_array = decide_next_whole(array, next_array)

        # print(array[0] is array[1])
        print()
        # print(iteration)
        
        print(f"next_array #{iteration}")
        for row in next_array:
            print(row)
        print()

        # Cannot assign, it only makes a ref to the same object
        # array = next_array

        # not sure I understand shallow copying, but I do need deep copying here
        # array = next_array.copy()
        array = [row[:] for row in next_array]

        iteration += 1

        time.sleep(0.5)


def decide_next_whole(array, next_array):
    #selection rule: B3/S23, cell born if 3 neighbours, survives if 2 or 3, dies otherwise

    for x in range(Nx):
        for y in range(Ny):

            a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
            next_state, sum = 0, 0

            a, b, c = array[(x-1)%Nx][(y-1)%Ny], array[(x-1)%Nx][y], array[(x-1)%Nx][(y+1)%Ny]
            d, e = array[x][(y-1)%Ny], array[x][(y+1)%Ny]
            f, g, h = array[(x+1)%Nx][(y-1)%Ny], array[(x+1)%Nx][y], array[(x+1)%Nx][(y+1)%Ny]
            print()
            print(a, b, c)
            print(d, " ", e)
            print(f, g, h)

            sum = a + b + c + d + e + f + g + h
            print(f"x= {x}, y= {y}, sum= ", end="")
            if sum == 3:
                print(sum, " ", "be born", end="    next_state = ")
                next_state = 1
            elif sum == 2:
                print(sum, " ", "survive", end="    next_state = ")
                next_state = array[x][y]
            else:
                print(sum, " ", "die", end="    next_state = ")
                next_state = 0

            print(next_state)
            next_array[x][y] = next_state

    return next_array


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



