# array = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

# print(array)
# print(array[0][4])

import random

array = []
Nx, Ny = 5, 4

# for j in range(Ny): # beware making it a transposed array so it prints easy to read later
#     column = []
#     for i in range(Nx):
#         column.append(random.randrange(10))
#     array.append(column)

count = 1
for j in range(Ny): # beware making it a transposed array so it prints easy to read later
    column = []
    for i in range(Nx):
        column.append(count)
        count += 1
    array.append(column)

for row in array:
    print(row)

# print(array[3][4]) # use this as print(y, x)
# print(array[Ny-1][Nx-1])

x, y = 9, 14
# print(array[y][x])
# print(array[0][0])
print(x%Nx-1, y%Ny-1)
# print(array[x%Nx-1][y%Ny-1])
print(array[y%Ny-1][x%Nx-1]) #need to index the other way round
# print()
