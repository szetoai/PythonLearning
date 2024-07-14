my_info = {
    "name" : "A",
    "age" : 18,
    "status" : "single :(",
    "skills" : ["meowing", "python", "valorant"]    
}

print(my_info["skills"][2]) # accessing info
my_info["orientation date"] = "July 8" # adding info
my_info["orientation date"] = "July 8th and 9th" # editing info
print("age" in my_info) # searches for keys only, not values
my_info.pop("name") # deletes name's value from dict
my_info.popitem() # removes last item (skills)
del my_info["status"] # can delete entire dict or key
print(my_info.items()) # turns dict into a list with tuples of each key and value
your_info = my_info.copy() # copies dict
print(my_info.keys()) # returns all keys from dict
print(my_info.values()) # returns all values from dict
print(my_info.clear()) # clears dict
