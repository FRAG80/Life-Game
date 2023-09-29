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

# seed the array, import from a separate file or it gets messy
array = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # for y in range(Ny):
        #     for x in range(Nx):
        for x in range(Nx):
            for y in range(Ny):
                decide_next(x, y, array, next_array, white, black)

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

    # try to sum neighbor cells
    # mapping: a b c, d xy e, f g h [corners:a,c,f,h]
    # if sum fails due to array out of bound error then it's an edge or a corner
    # use try/except to catch the error
    try:
        a, b, c = array[x-1][y-1], array[x][y-1], array[x+1][y-1]
        d, e = array[x-1][y], array[x+1][y]
        f, g, h = array[x-1][y+1], array[x][y+1], array[x+1][y+1]
        
    except IndexError: # either a corner or an edge cell
        # 8 cases: 1 2 3 4 corners, 5 6 7 8 edges
        # 1 6 2
        # 5   7
        # 3 8 4

        # For corner and edge cases need to reassign all values
        # past the one that triggered the error.
        # They are always either all values a-h, or subset c-h, or f-h
        # array cells to use for the calc depends on the exact case though  
        if y == 0:
            if x == 0:
                # case 1: top left corner: recalc abcdefgh
                a = array[Nx-1, Ny-1]
                b = array[0, Ny-1]
                c = array[1, Ny-1]
                d = array[Nx, 0]
                e = array[1, 0]
                f = array[Nx, 1]
                g = array[0, 1]
                h = array[1, 1] # error prone and tedious
            elif x == Nx-1:
                # case 2: top right corner: recalc abcdefgh
                a = array[x-1, Ny-1]
                b = array[x, Ny-1]
                c = array[0, Ny-1]
                d = array[x-1, y]
                e = array[0, 0]
                f = array[x-1, y+1]
                g = array[x, y+1]
                h = array[0, y+1]
            else:
                # case 6: top edge: recalc abcdefgh
                a = array[x-1, Ny-1]
                b = array[x, Ny-1]
                c = array[x+1, Ny-1]
                d = array[x-1, y]
                e = array[x+1, y]
                f = array[x-1, y+1]
                g = array[x, y+1]
                h = array[x+1, y+1]

        elif y == Ny-1:
            if x == 0:
                # case 3: bottom left corner: recalc abcdefgh
                a = array[Nx-1,y-1]
                b = array[x, y-1]
                c = array[x+1, y-1]
                d = array[Nx-1, Ny-1]
                e = array[x+1, y]
                f = array[Nx-1, y]
                g = array[0, 0]
                h = array[x+1, 0]

            elif x == Nx-1:
                # case 4: bottom right corner: recalc cdefgh
                # a,b should stay the same but not sure if multiple assignement goes thru when error on c
                a = array[x-1, y-1]
                b = array[x, y-1]
                c = array[0, y-1]
                d = array[x-1, y]
                e = array[0, Ny-1]
                f = array[x-1, 0]
                g = array[Nx-1, 0]
                h = array[0, 0]
            else:
                # case 8: bottom edge: recalc fgh
                f = array[x-1, 0]
                g = array[x, 0]
                h = array[x+1, 0]

        elif x == 0 and y not in [0, Ny-1]:
            # case 5: left edge: recalc abcdefgh
            a = array[Nx-1, y-1]
            b = array[x, y-1]
            c = array[x+1, y-1]
            d = array[Nx-1, y]
            e = array[x+1, y]
            f = array[Nx-1, y+1]
            g = array[x, y+1]
            h = array[x+1, y+1]

        elif x == Nx-1 and y not in [0, Ny-1]:
            # case 7: right edge: recalc cdefgh
            c = array[0, y-1]
            d = array[x-1, y]
            e = array[0, y]
            f = array[x-1, y+1]
            g = array[0, y]
            h = array[0, y+1]

    finally:
        sum = a + b + c + d + e + f + g + h

        if sum in [2, 3]:
            if sum == 3:
                print(x, y, "be born")
            else:
                print(x, y, "survive")
        else:
            print(x, y, "die")

    
if __name__ == "__main__":
    main()

# # if it's a corner cell
#     if x == 0 or y == 0 or x == Nx-1 or y == Ny-1:
#         if x == 0 and y == 0:
#             a = array[Nx-1][Ny-1]
#             b = array[Nx-1][y-1]