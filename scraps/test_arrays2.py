# array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# for col in array:
#     print(col)

# Nx, Ny = 4, 3
# x, y = 3, 2
# print(array[y][x])

# print(array[(y%Ny)+1][x-1])

# print(array[y%Ny+1][x])
# print(array[y%Ny+1][x%Nx+1])

array2 = [1, 2, 3, 4]
size = 4
x = 3
print(array2[x])
print(array2[x%size])
print(array2[x%size-1])
print(array2[(x%size+1)%size]) #+1 needs %size again or it overflows

print()
x = 0
print(array2[x])
print(array2[x%size])
print(array2[x%size-1]) #-1 DOES NOT need %size again; array[-n] works
print(array2[(x%size-1)%size])