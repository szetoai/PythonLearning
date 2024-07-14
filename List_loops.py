jumper = [10, 20, 30, 40, "mrow"]

for x in jumper: # prints each item
    print(x)

m = [i for i in jumper] # assigning each value in jumper to m
print(m)
print([(i, i * 2) for i in jumper if type(i) == int]) # for each thing in jumper, make a tuple with each value and each value x 2, if the i's type is integer

listlist = [[1, 2, 3], [4, 5, 6]]
print([num for list in listlist for num in list]) # print a number for each list in listlist, with each number being for every num in list

