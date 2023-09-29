import pygame


X, Y = 200, 100 # width, height in pixels
block_size = 10
Nx, Ny = int(X/block_size), int(Y/block_size)

array = [] # this is the universe, a list of 0-Nx columns, each with 0-Ny elements
for i in range(Nx):
    col = []
    for j in range(Ny):
        col.append(0)
    array.append(col)

# make a copy before seeding
next_array = array

# seed the array
# TODO


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

    while True:
        decide_next(0, 0, array, next_array, white, black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def drawGrid(X, Y, display, grid_color, block_size):
    for x in range(0, X, block_size):
        for y in range(0, Y, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(display, grid_color, rect, 1)


def decide_next(x, y, array, next_array, alive_color, dead_color):
    #selection rule: B3/S23
    # cell born if 3 neighbours, survives if 2 or 3, dies otherwise
    
    # cells to consider are:
    # (x+1, y), (x-1, y),
    # (x, y+1), (x, y-1),
    # (x-1, y+1), (x+1, y+1), (x+1, y-1), (x-1, y-1)
    # corners and edges of universe:
    # if x-1 < 0: x-1 = X
    # if x+1 > X: x+1 = 0
    # if y-1 < 0: y-1 = Y
    # if y+1 > Y: y+1 = 0

    print(array[x][y])
    print(array[x+1][y+1])

if __name__ == "__main__":
    main()