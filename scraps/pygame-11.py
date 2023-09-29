import pygame, time


X, Y = 50, 40 # width, height in pixels
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)

# # The code below makes an array with incremental integers:
# count = 1
array = [] # this is the universe, a list of 0-Nx columns, each with 0-Ny elements
for j in range(Ny):
    col = []
    for i in range(Nx):
        col.append(0)
    array.append(col)

# make a copy before seeding
next_array = array

# seed the array, import from a separate file or it gets messy
# array = [[0, 0, 0, 0], 
#          [0, 0, 0, 0], 
#          [0, 0, 0, 0]]

array = [[1, 1, 0, 0, 0], 
         [0, 0, 1, 0, 0], 
         [0, 0, 1, 1, 0],
         [0, 0, 0, 0, 0]]

# for row in array:
#     print(row)

print(array)
print("Nx= ", Nx, " Ny= ", Ny)

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

        # for y in range(Ny):
        #     for x in range(Nx):
        for x in range(Nx):
            for y in range(Ny):
                state = decide_next(x, y, array, next_array, white, black)
                if state == 1:
                    drawCell(x, y, display, white, block_size)
                elif state == 0:
                    drawCell(x, y, display, black, block_size)
                else:
                    print("undef state!")

                time.sleep(0.1)
                pygame.display.update()

        for row in next_array:
            print(row)
        print()

        # pygame.display.update()


def drawGrid(X, Y, display, grid_color, block_size):
    for x in range(0, X, block_size):
        for y in range(0, Y, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(display, grid_color, rect, 1)

def drawCell(x, y, display, cell_color, block_size):
    rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    pygame.draw.rect(display, cell_color, rect, width=0)

def decide_next(x, y, array, next_array, alive_color, dead_color):
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
            next_array[y][x] = 1
        elif sum == 2:
            print(sum, " ", "survive", end="    ")
            next_array[y][x] = array[y][x]
        else:
            print(sum, " ", "die", end="    ")
            next_array[y][x] = 0

        print(next_array[y][x])
        return next_array[y][x]

    
if __name__ == "__main__":
    main()
