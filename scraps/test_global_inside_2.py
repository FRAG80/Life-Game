
# glob_var = 1

# def main():

#     print(glob_var)

#     global glob_var
#     glob_var = 2

#     print(glob_var)

# # Code below works fine but not in main code:
# def main():
#     array = next_array = [[0,0,0],[0,0,0]]
#     print(array)

#     while True:
#         for x in range(2):
#             for y in range(3):
#                 state = flip_state(x, y, array)
#                 next_array[x][y] = state
#         print(next_array)

# def flip_state(x, y, array):
#     if array[x][y] == 0:
#         array[x][y] = 1
#     else:
#         array[x][y] = 0
#     return array[x][y]

# if __name__ == "__main__":
#     main()


# From pygame-14.py, testing:
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

    next_array =\
    [[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]


    iteration = 0

    print("Nx= ", Nx, " Ny= ", Ny)
    print("Seed array when iteration = 0")
    # for row in numpy.swapaxes(array, 0, 1):
    # for row in array:
    #     print(row)
    # numpy.swapaxes(array, 0, 1) ###
    # print()
    # print(array)
    # print()

    pygame.init()

    display = pygame.display.set_mode((X, Y))

    # pygame.transform.rotate(display, 90) ## need to blit after this, couldn't get it to work

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
                else:
                    cell_off(x, y, block_size, display)

                next_array[x][y] = decide_next(x, y, array)
                print(next_array[x][y])
                time.sleep(0.05)
        
        # print(array[0] is array[1])
        print()
        # print(iteration)
        # for row in numpy.swapaxes(next_array, 0, 1):
        print(f"next_array #{iteration}")
        for row in next_array:
            print(row)
        print()

        array = next_array

        iteration += 1

        time.sleep(0.5)


def decide_next(x, y, array):
    #selection rule: B3/S23, cell born if 3 neighbours, survives if 2 or 3, dies otherwise                       
    # sum neighbor cells.
    # Mapping: a d f
    #          b   g
    #          c e h

    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    sum, next_state = 0, 0

    try:
        # a, b, c = array[x-1][y-1], array[x][y-1], array[(x%Nx+1)%Nx][y-1]
        # d, e = array[x-1][y], array[(x%Nx+1)%Nx][y]
        # f, g, h = array[x-1][(y%Ny+1)%Ny], array[x][(y%Ny+1)%Ny], array[(x%Nx+1)%Nx][(y%Ny+1)%Ny]

        # a, b, c = array[x-1][y-1], array[x-1][y], array[x-1][(y%Ny+1)%Ny]
        # d, e = array[x][y-1], array[x][(y%Ny+1)%Ny]
        # f, g, h = array[(x%Nx+1)%Nx][y-1], array[(x%Nx+1)%Nx][y], array[(x%Nx+1)%Nx][(y%Ny+1)%Ny]

        # a, b, c = array[x-1][y-1], array[x-1][y], array[x-1][(y+1)%Ny]
        # d, e = array[x][y-1], array[x][(y+1)%Ny]
        # f, g, h = array[(x+1)%Nx][y-1], array[(x+1)%Nx][y], array[(x+1)%Nx][(y+1)%Ny]

        a, b, c = array[(x-1)%Nx][(y-1)%Ny], array[(x-1)%Nx][y], array[(x-1)%Nx][(y+1)%Ny]
        d, e = array[x][(y-1)%Ny], array[x][(y+1)%Ny]
        f, g, h = array[(x+1)%Nx][(y-1)%Ny], array[(x+1)%Nx][y], array[(x+1)%Nx][(y+1)%Ny]

    except IndexError: # x = Nx-1 or y = Ny-1
        print("Error")

    finally:
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

        # print(next_state)
        return next_state


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



