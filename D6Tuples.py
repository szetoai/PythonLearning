# note: very similar to lists just unmodifiable; if you want to edit turn it into a list using list()


help = (4, 64, 677)
help2 = (555, 666, 777)
print(len(help)) # length
print(help[-2]) # index
print(help[0:1]) # slicing
print(64 in help) # checking if item exists
help = help + help2 # joining tuples; CANNOT use .extend like with lists
del help # CANNOT delete specific indexes like with lists, only the entire tuple