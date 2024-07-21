# functions as parameters
def adding1(p):
    return p + 1

def adding(f, x):
    return f(x)

print(adding(adding1, 11))

# functions as return values
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def AoS(f, x, y):
    if f == add:
        return add(x, y)
    elif f == sub:
        return sub(x, y)

print(AoS(add, 10, 5))

# closures/nested functions
def outer():
    def inner(x):
        print(x + " something")
    return inner
p = outer()
p("hi")

# decorators
def uppercaser(f):
    def wrapper(para1):
        return f(para1).upper()
    return wrapper
def reverser(f):
    def wrapper(para1):
        return f(para1)[::-1]
    return wrapper

@uppercaser # applies decorator
@reverser
def printingstuff(printee):
    return printee

print(printingstuff("testing"))

# higher order functions examples

# map: needs function and itterable, runs through itterable with function
mrrp = [1, 2, 3, 4, 5]
def squaring(x):
    return x ** 2
print(list(map(squaring, mrrp)))

# filter, needs function and itterable, returns all that return true
mrrp2 = ["meow", "mrow", "purr"]
def meow_check(x):
    if x == "meow":
        return True
    else:
        return False
print(list(filter(meow_check, mrrp2)))

# reduce, takes function and itterable, reduces itterable to one value
import functools as f
mrrp3 = ["cat", "maid", "nya"]
def adder(x, y):
    return x + y
print(f.reduce(adder, mrrp3))