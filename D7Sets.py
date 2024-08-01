# note: very similar to lists but bad, can only add/remove items from them, use for more comparison stuff

meow = {"cat", "feline", "lion", "tiger"}
print(len(meow)) # length
print("lion" in meow) # checks if item exists
meow.add("jaguar") # add 1 item
meow.update(["puma", "panther"]) # add multiple items
meow.remove("jaguar") # remove item
meow.pop() # removes a random item
meow.clear() # clears set
del meow # deletes meow

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