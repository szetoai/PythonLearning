# note: very similar to lists but bad, can only add/remove items from them, use for more comparison stuff

feline = {"cat", "lion", "tiger"}
print(len(feline)) # length
print("lion" in feline) # checks if item exists
feline.add("jaguar") # add 1 item
feline.update(["puma", "panther"]) # add multiple items
feline.remove("jaguar") # remove item
feline.pop() # removes a random item
feline.clear() # clears set
del feline # deletes feline

# joining sets
hi = {1, 2, 3}
hi1 = {4, 5, 6}
hi2 = hi.union(hi1) # union returns a new set
hi.update(hi1) # update updates a existing set - STEALS all items from input
print(hi.isdisjoint(hi1)) # bool if they have any in common

a = {101, 1101, 1111, 2222}
b = {1101, 101, 1111, 333}
print(a.intersection(b)) # same items in both lists
print(a.issuperset(b)) # bool is superset of input
print(b.issubset(a)) # bool is subset of input
print(a.difference(b)) # returns difference of sets (ONLY FOR what 1st set has that input doesnt)
print(a.symmetric_difference(b)) # returns differences from both sets