from prettytable import PrettyTable

# table = [['col 1', 'col 2', 'col 3', 'col 4'], [1, 2222, 30, 500], [4, 55, 6777, 1]]
# tab = PrettyTable(table[0])
# tab.add_rows(table[1:])


table = [['x1', 'x2', 'x3', 'x4', 'x5'], [0, 0, 0, 0, 1]]
tab = PrettyTable(table[0])
# tab.add_rows([0,0,0,0,1])
tab.add_rows(table[1:]) ## has to be specified as a range
tab.add_rows(table[1:])
print(tab) 