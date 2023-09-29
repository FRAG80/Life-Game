import pygame, time

#  I am stuck messing around with how to update next_array etc
#  done a test with same structure (passing as argument rather than as global) and it worked, not sure why not working in main code)



# At some point ask user input for array size Nx, Ny
X, Y = 50, 40 # width, height in pixels
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)

# # # Make an empty array
# array = [] # this is the universe, a list of 0-Nx columns, each with 0-Ny elements
# for j in range(Ny):
#     col = []
#     for i in range(Nx):
#         col.append(0)
#     array.append(col)

# # make a copy before seeding
# next_array = array

# # seed the array, import from a separate file or it gets messy
# # hard-seeding for now
array = next_array =    [[0, 0, 0, 0, 0], 
                        [0, 0, 1, 0, 0], 
                        [0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0]]
 
# # for row in array:
# #     print(row)

# print(array)
# print("Nx= ", Nx, " Ny= ", Ny)

def main():
        # # Make an empty array
    # array = [] # this is the universe, a list of 0-Nx columns, each with 0-Ny elements
    # for j in range(Ny):
    #     col = []
    #     for i in range(Nx):
    #         col.append(0)
    #     array.append(col)

    # # make a copy before seeding
    # next_array = array

    # seed the array, import from a separate file or it gets messy
    # hard-seeding for now
    # array = next_array =    [[0, 0, 0, 0, 0], 
    #                         [0, 0, 1, 0, 0], 
    #                         [0, 0, 1, 0, 0],
    #                         [0, 0, 1, 0, 0]]
    
    # for row in array:
    #     print(row)

    print(array)
    print("Nx= ", Nx, " Ny= ", Ny)

    pygame.init()
    
    display = pygame.display.set_mode((X,Y))
    # pygame.display.update()
    pygame.display.set_caption('Life game by Fra')
    # white = (255, 255, 255)
    # black = (0,0,0)


    drawGrid(X, Y, display, block_size)
    time.sleep(0.5)

    iteration = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # display.fill(black)
        # drawGrid(X, Y, display, white, block_size)

        # for y in range(Ny):
        #     for x in range(Nx):
        for x in range(Nx):
            for y in range(Ny):
                state = decide_next(x, y, array)
                next_array[y][x] = state
                if state == 1:
                    print(f"cell {x} {y} ON")
                    # drawCell(x, y, display, white, block_size)
                    cell_on(x, y, block_size, display)
                elif state == 0:
                    print(f"cell {x} {y} OFF")
                    # drawCell(x, y, display, black, block_size)
                    cell_off(x, y, block_size, display)

                time.sleep(0.05)

                # pygame.display.update()
                # pygame.display.flip()

        for row in next_array:
            print(row)
        print()

        # Copy newly generated array to use in next iteration
        globals()["array"] = next_array
        # globals()["next_array"] = []
        print(iteration)
        iteration += 1

        # pygame.display.update()



def drawGrid(X, Y, display, block_size):
    for x in range(0, X, block_size):
        for y in range(0, Y, block_size):
            # rect = pygame.Rect(x, y, block_size, block_size)
            # pygame.draw.rect(display, grid_color, rect, 1)
            cell_off(x, y, block_size, display)

# def drawCell(x, y, display, cell_color, block_size):
#     rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
#     pygame.draw.rect(display, cell_color, rect, width=0)

def decide_next(x, y, array):
    #selection rule: B3/S23
    # cell born if 3 neighbours, survives if 2 or 3, dies otherwise
                                                    
    # sum neighbor cells
    # mapping: a b c, d xy e, f g h [corners:a,c,f,h]
    
    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    sum = 0

    try:
        a, b, c = array[y-1][x-1], array[y-1][x], array[y-1][(x%Nx+1)%Nx]
        d, e = array[y][x-1], array[y][(x%Nx+1)%Nx]
        f, g, h = array[(y%Ny+1)%Ny][x-1], array[(y%Ny+1)%Ny][x], array[(y%Ny+1)%Ny][(x%Nx+1)%Nx]

    except IndexError: # x = Nx-1 or y = Ny-1
        print("Error")

    finally:
        sum = a + b + c + d + e + f + g + h

        print(x, y, "   ", array[y][x], "   ", end="sum=")

        if sum == 3:
            print(sum, " ", "be born", end="    ")
            next_state = 1
        elif sum == 2:
            print(sum, " ", "survive", end="    ")
            next_state = array[y][x]
        else:
            print(sum, " ", "die", end="    ")
            next_state = 0

        print(next_state)
        return next_state
    

def cell_on(x, y, block_size, display):
    filled_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, (255, 255, 255), filled_rect, width=0)
    # pygame.display.update()
    pygame.display.flip()
    time.sleep(0.02)


def cell_off(x, y, block_size, display):
    filled_rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, (255, 255, 255), filled_rect, width=1)
    # pygame.display.update()
    pygame.display.flip()
    time.sleep(0.02)

    
if __name__ == "__main__":
    main()
