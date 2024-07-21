x = 5
while x < 10:
    print('hi')
    x += 1
else:
    print("hello") # executes when loops end

y = 10
while y < 15:
    y += 1
    if y == 11:
        y += 1
        continue # ends that loop starts a new one
    if y == 13:
        pass # continues in same loop, used for when you just need something there
    if y == 13:
        break # exits while loop entirely
    print("cat")

for item in ("cat"): # works for every letter in strings and items in lists/tuples/dicts/sets
    print('meow')
else:
    print('dog') # executes when loops end