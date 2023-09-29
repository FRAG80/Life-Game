import array, numpy, copy #, deepcopy
# from array import *

def main():
    # Nx, Ny = 6, 4
    x, y = 2, 0
    # generate array above and copy it here, then edit it to use as seed
    array = \
    [[0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

    # current_array = array.array("I",\
    # [[0, 0, 0, 0],
    # [0, 1, 0, 0],
    # [0, 1, 0, 0],
    # [0, 1, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0]])

    # next_array = current_array.copy()

    # next_array = deepcopy(array)

    next_array = [row[:] for row in array]

    next_array[x][y] = 3

    print(id(array))
    print(array)
    print()
    print(id(next_array))
    print(next_array)
    print()

    # print(f"x:{x} y:{y}")
    # print(array[x][y], next_array[x][y])

    rows = len(array)
    cols = len(array[0])
    print(rows, cols)


    
if __name__ == "__main__":
    main()

