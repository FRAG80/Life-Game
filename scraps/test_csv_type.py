# import numpy, csv

# seed_filename = "seed1.csv"

# with open(seed_filename) as f:
#     reader = csv.reader(f)
#     list = list(reader)
#     string_array = numpy.array(list)
#     print(string_array)
    # conv_array = []
    # conv_row = []
    # for row in string_array:
    #     for item in row:
    #         item = int(item)
    #         print(item)
    #         conv_row = numpy.append(conv_row, item)
    #     print(conv_row)
    #     conv_array = numpy.append(conv_array, conv_row)
    #     conv_row = []
    # print(conv_array)


#nope
    # int_row, int_array = [], []
    # for row in list:
    #     print(row)
    #     for item in row:
    #         int_data = int(item)
    #         int_row = numpy.append(int_row, int_data)
    #     print(int_row)
    #     int_array = numpy.append(int_array, int_row)
    #     int_row = []
    # print(int_array)

    # for row in string_array:
    #     for col in row:
    #         entry = int(col[0])
    #         row = row.append(entry)

import csv

seed_filename = "seed1.csv"

with open(seed_filename) as f:
    reader = csv.reader(f)
    top_list = list(reader)

    # print(top_list) # list of lists of strings

    int_top_list = [] ### new integer list of lists
    for row in top_list:
        # print(row)
        int_list = [] ### new integer sub list
        for item in row:
            int_item = int(item)
            # print(item, int_item)
            int_list.append(int_item)
        # print(int_list)
        int_top_list.append(int_list)
    # print(int_top_list)
    # print()
    for row in int_top_list:
        print(row)
        



