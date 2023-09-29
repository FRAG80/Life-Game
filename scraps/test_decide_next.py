
# Nx, Ny = 3, 4
Nx, Ny = 6, 4

def main():

    # array = \
    # [[1,1,0,0],
    #  [0,1,0,0],
    #  [0,0,0,0]]
    
    array = \
    [[0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

    for row in array:
        print(row)

    print(decide_next(2, 2, array))
    print(decide_next(1, 0, array))


def decide_next(x, y, array):
    #selection rule: B3/S23, cell born if 3 neighbours, survives if 2 or 3, dies otherwise                       
    # sum neighbor cells.
    # Mapping: a d f
    #          b   g
    #          c e h

    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    sum = 0

    try:
        # a, b, c = array[x-1][y-1], array[x][y-1], array[(x%Nx+1)%Nx][y-1]
        # d, e = array[x-1][y], array[(x%Nx+1)%Nx][y]
        # f, g, h = array[x-1][(y%Ny+1)%Ny], array[x][(y%Ny+1)%Ny], array[(x%Nx+1)%Nx][(y%Ny+1)%Ny]

        a, b, c = array[x-1][y-1], array[x-1][y], array[x-1][(y%Ny+1)%Ny]
        d, e = array[x][y-1], array[x][(y%Ny+1)%Ny]
        f, g, h = array[(x%Nx+1)%Nx][y-1], array[(x%Nx+1)%Nx][y], array[(x%Nx+1)%Nx][(y%Ny+1)%Ny]
        print(a, b, c)
        print(d, " ", e)
        print(f, g, h)


    except IndexError: # x = Nx-1 or y = Ny-1
        print("Error")

    finally:
        sum = a + b + c + d + e + f + g + h
        print(f"x= {x}, y= {y}, sum= ", end="")
        if sum == 3:
            print(sum, " ", "be born")
            next_state = 1
        elif sum == 2:
            print(sum, " ", "survive")
            next_state = array[x][y]
        else:
            print(sum, " ", "die")
            next_state = 0

        # print(next_state)
        return next_state

if __name__ == "__main__":
    main()