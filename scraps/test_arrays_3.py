# Nx, Ny = 4, 3

# # make an array of size Nx, Ny filled with zeroes:
# array = [] # this is the universe, a list of 0-Nx columns, each with 0-Ny elements
# for j in range(Ny):
#     col = []
#     for i in range(Nx):
#         col.append(0)
#     array.append(col)

# print(array)
# print()
# for col in array:
#     print(col)

#     # 
# print()
# print()

# array2 = [] # this is the universe, a list of 0-Nx columns, each with 0-Ny elements
# for i in range(Nx):
#     col = []
#     for j in range(Ny):
#         col.append(0)
#     array2.append(col)

# print(array2)
# for col in array2:
#     print(col)


def main():
    Nx, Ny = 6, 4
    x, y = 2,0
    # generate array above and copy it here, then edit it to use as seed
    array = next_array =\
    [[0, 0, 0, 2],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]]


    a, b, c = array[x-1][y-1], array[x-1][y], array[x-1][(y+1)%Ny] ## array[x-1][(y%Ny+1)%Ny]
    d, e = array[x][y-1], array[x][(y+1)%Ny]
    f, g, h = array[(x+1)%Nx][y-1], array[(x+1)%Nx][y], array[(x+1)%Nx][(y+1)%Ny]


    print(f"x:{x} y:{y}")
    print(a, b, c)
    print(d, " ", e)
    print(f, g, h)
    print(array[0][-5])

    
if __name__ == "__main__":
    main()

