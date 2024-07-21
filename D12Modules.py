import D12Mymodule; from D12MyModule2 import modulefunc2 as myfunc # manual importing from self-made file; importing specific functions/renaming the,
D12Mymodule.modulefunc()
myfunc()

import os # operating system - does actual file directory stuff
# os.mkdir("folder") # makes a folder
# os.chdir("c:\\Users\\hazfr\\OneDrive\\Desktop\\Code\\30days") # changing directory path
print(os.getcwd()) # prints current working directory
# os.rmdir("c:\\Users\\hazfr\\OneDrive\\Desktop\\Code\\30days") # removes directory

import sys
# print(f"{sys.argv[1]}") # takes the index one of command prompt TRY "python Modules.py Hello"
print(sys.maxsize) # largest integer input (if you wanted to know that for some reason)
print(sys.path) # know environment path
# sys.exit() # exits program

from statistics import * # importing all funcs from stats; can now use without saying stats.func (just func)
nums = (5, 10)
print(mean(nums))       
print(median(nums))     
print(mode(nums))       
print(stdev(nums))

from math import *
print(pi)           # 3.141592653589793, pi constant
print(sqrt(2))      # 1.4142135623730951, square root
print(pow(2, 3))    # 8.0, exponential function
print(floor(9.81))  # 9, rounding to the lowest
print(ceil(9.81))   # 10, rounding to the highest
print(log10(100))   # 2, logarithm with 10 as base
print(round(10.1111)) # 10, not part of math

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~