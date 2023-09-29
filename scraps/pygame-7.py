import pygame, random


X, Y = 40, 30 # width, height in pixels
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)

array = [] # this is the universe, a list of 0-Nx columns, each with 0-Ny elements
for i in range(Nx):
    col = []
    for j in range(Ny):
        col.append(random.randrange(10))
    array.append(col)

# make a copy before seeding
next_array = array

# seed the array, import from a separate file or it gets messy
# array = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# for row in array:
#     print(row)

print(array)

def main():
    pygame.init()
    
    display = pygame.display.set_mode((X,Y))
    # pygame.display.update()
    pygame.display.set_caption('Life game by Fra')
    white = (255, 255, 255)
    black = (0,0,0)


    drawGrid(X, Y, display, white, block_size)

    # for row in array: # confusing as this seemingly transposes the array
    #     print(row)
    # print(Nx, Ny)

    # while True:  ##Re-enable later

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # for y in range(Ny):
    #     for x in range(Nx):
    for x in range(Nx):
        for y in range(Ny):
            decide_next(x, y, array, next_array, white, black)

    
    # decide_next(x, y, array, next_array, white, black)

    pygame.display.update()


def drawGrid(X, Y, display, grid_color, block_size):
    for x in range(0, X, block_size):
        for y in range(0, Y, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(display, grid_color, rect, 1)


def decide_next(x, y, array, next_array, alive_color, dead_color):
    #selection rule: B3/S23
    # cell born if 3 neighbours, survives if 2 or 3, dies otherwise

    # try to sum neighbor cells
    # mapping: a b c, d xy e, f g h [corners:a,c,f,h]
    
    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    try:
        # a, b, c = array[x%Nx-1][y%Ny-1], array[x%Nx][y%Ny-1], array[x%Nx+1][y%Ny-1]
        # d, e = array[x%Nx-1][y%Ny], array[x%Nx+1][y%Ny]
        # f, g, h = array[x%Nx-1][y%Ny+1], array[x%Nx][y%Ny+1], array[x%Nx+1][y%Ny+1]
        
        # a, b, c = array[x%(Nx-1)-1][y%(Ny-1)-1], array[x%(Nx-1)][y%(Ny-1)-1], array[x%(Nx-1)+1][y%(Ny-1)-1]
        # d, e = array[x%(Nx-1)-1][y%(Ny-1)], array[x%(Nx-1)+1][y%(Ny-1)]
        # f, g, h = array[x%(Nx-1)-1][y%(Ny-1)+1], array[x%(Nx-1)][y%(Ny-1)+1], array[x%(Nx-1)+1][y%(Ny-1)+1]

        a, b, c = array[(x%Nx-1)-1][(y%Ny-1)-1], array[(x%Nx-1)][(y%Ny-1)-1], array[(x%Nx-1)+1][(y%Ny-1)-1]
        d, e = array[(x%Nx-1)-1][(y%Ny-1)], array[(x%Nx-1)+1][(y%Ny-1)]
        f, g, h = array[(x%Nx-1)-1][(y%Ny-1)+1], array[(x%Nx-1)][(y%Ny-1)+1], array[(x%Nx-1)+1][(y%Ny-1)+1]
        
    except IndexError: # x = Nx-1 or y = Ny-1
        print("Error")

    finally:
        # sum = a + b + c + d + e + f + g + h

        # if sum in [2, 3]:
        #     if sum == 3:
        #         print(x, y, "be born")
        #     else:
        #         print(x, y, "survive")
        # else:
        #     print(x, y, "die")
        print(x, y)
        print(a, b, c)
        print(d, " ", e)
        print(f, g, h)
        print()

    
if __name__ == "__main__":
    main()
