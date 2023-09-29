import pygame, time
# stop indexing arrays the weird way for ease of printing

# At some point ask user input for array size Nx, Ny
X, Y = 50, 40 # display width, height in pixels
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)

# Use this code to make an empty array, then edit it to use as seed and copy paste below.
# array = [] # this is the universe, a list of 0-Nx rows, each with 0-Ny elements
# for x in range(Nx):
#     row = []
#     for j in range(Ny):
#         row.append(0)
#     array.append(row)

# # # make a copy before seeding
# # next_array = array

# generate array above and copy it here, then edit to use as seed
array = next_array =\
[[0, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 1, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 0]]

iteration = 0

def main():
    global array
    print("Nx= ", Nx, " Ny= ", Ny)
    print("Seed array: ", end=" ")
    for row in array:
        print(row)

    print()

    pygame.init()

    display = pygame.display.set_mode((X, Y))

    pygame.display.set_caption('Life game by Fra')
    drawGrid(Nx, Ny, display)
    time.sleep(0.5)

    # for x in range(Nx):
    #     for y in range(Ny):
    #         cell_on(x, y, block_size, display)
    #         time.sleep(0.2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # display.fill(black)
        # drawGrid(X, Y, display, white, block_size)


        for x in range(Nx):
            for y in range(Ny):
                state = decide_next(x, y, array)
                globals()["next_array[x][y]"] = state
                if state == 1:
                    print(f"cell {x} {y} ON")
                    cell_on(x, y, block_size, display)
                elif state == 0:
                    print(f"cell {x} {y} OFF")
                    cell_off(x, y, block_size, display)
                time.sleep(0.05)

#                 # pygame.display.update()
#                 # pygame.display.flip()
        print(iteration)

        for row in next_array:
            print(row)
        print()

        array = next_array

#         # Copy newly generated array to use in next iteration
#         globals()["array"] = next_array
#         # globals()["next_array"] = []
#         print(iteration)
        globals()["iteration"] += 1

        # pygame.display.update()



def decide_next(x, y, array):
    #selection rule: B3/S23
    # cell born if 3 neighbours, survives if 2 or 3, dies otherwise
                                                    
    # sum neighbor cells
    # mapping: a b c, d xy e, f g h [corners:a,c,f,h]
    
    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    sum = 0

    try:
        # a, b, c = array[x-1][y-1], array[x][y-1], array[(x%Nx+1)%Nx][y-1]
        # d, e = array[x-1][y], array[(x%Nx+1)%Nx][y]
        # f, g, h = array[x-1][(y%Ny+1)%Ny], array[x][(y%Ny+1)%Ny], array[(x%Nx+1)%Nx][(y%Ny+1)%Ny]

        a, b, c = array[x-1][y-1], array[x-1][y], array[x-1][(y%Ny+1)%Ny]
        d, e = array[x][y-1], array[x][(y%Ny+1)%Ny]
        f, g, h = array[(x%Nx+1)%Nx][y-1], array[(x%Nx+1)%Nx][y], array[(x%Nx+1)%Nx][(y%Ny+1)%Ny]
        
    except IndexError: # x = Nx-1 or y = Ny-1
        print("Error")

    finally:
        sum = a + b + c + d + e + f + g + h

        # print(x, y, "   ", array[x][y], "   ", end="sum=")

        if sum == 3:
            # print(sum, " ", "be born", end="    ")
            next_state = 1
        elif sum == 2:
            # print(sum, " ", "survive", end="    ")
            next_state = array[x][y]
        else:
            # print(sum, " ", "die", end="    ")
            next_state = 0

        # print(next_state)
        return next_state
    

def drawGrid(Nx, Ny, display):
    for x in range(Nx):
        for y in range(Ny):
            cell_off(x, y, block_size, display)


# def drawGrid(Nx, Ny, display):
#     for x in range(Nx):
#         for y in range(Ny):
#             cell_off(x, y, block_size, display)

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
