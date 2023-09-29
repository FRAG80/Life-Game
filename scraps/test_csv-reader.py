import numpy, csv

seed_filename = "seed1.csv"

with open(seed_filename) as f:
    reader = csv.reader(f)
    list = list(reader)
    print(list)
    print()
    
    array = numpy.array(list)
    print(array)

# #Successfully installed panda-0.3.1
# import panda

# data = panda.read_csv("seed1.csv", dtype="int64")
# print(data)