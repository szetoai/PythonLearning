"""
Lists: ordered, modifiable, duplicates
Tuples: ordered, unmodifiable, duplicates
Sets: unordered, unindexed, unmodifiable, can be added to, no duplicates
Dictionaries: unordered, modifiable, indexed, no duplicates
"""

# indexing
my_list = ["apple", "orange", "banana", "strawberry"]

one, two, *rest = my_list
print(f"{one} {two} {rest}") # unpacking list items

print(my_list[-1]) # negative indexing
print(my_list[0:3]) # all
print(my_list[2:]) # 2 and beyond
print(my_list[::2]) # every n'nd item from first item
print(my_list[-2:]) # negative index and beyond
print(my_list[::-2]) # every n'nd item starting from last item

my_list1 = [57, 435, 111, 5667, 459854]
my_list1.append(664) # inserts to the end
my_list1.insert(2, 777) # inserts to specific index
my_list1.remove(57) # removes FIRST occurence of item
my_list1.pop(5) # removes 1 indexed item (last if blank)
my_list1.clear() # clears list
del my_list1[0:2] # deleted indexes given (deletes list if blank)
print(my_list1)

my_list2 = [777, 888, 999]
my_list3 = my_list2.copy() # copies list

# combining lists
print(my_list2 + my_list3)
my_list2.extend(my_list3)

print(my_list2.count(777)) # counts times item appears in list
print(my_list2.index(777)) # returns index of first occurence
my_list2.reverse() # reverses list
my_list2.sort # sorts lists (changes OG list)
print(sorted(my_list2, reverse = True)) # sorts list without changing OG list
print(my_list2)