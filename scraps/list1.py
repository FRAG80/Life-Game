# N = 5
# array = [0] * N
# print(array)

# The entire array is created as a list of references to the same inner list, resulting in aliasing. Any change made to an element in one row will be reflected in all rows. 
# rows, cols = (5, 5)
# arr = [[0]*cols]*rows
# print(arr, "before")
 
# arr[0][0] = 1 # update only one element
# print(arr, "after")

# method below better, rows are independent objects, no risk of aliasing
# rows, cols = (5, 5)
# print([[0 for i in range(cols)] for j in range(rows)])

arr=[]
rows, cols = 2, 5
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)
print(arr)
print()
for row in arr:
    print(row)
