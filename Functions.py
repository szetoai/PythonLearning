def my_function(input1, input2 = "joe biden"):
    return(input1 + input2)

print(my_function("5", "10")) # input values (order does matter)
print(my_function(input2="imagined", input1="dragons ")) # input values (order doesnt matter)
print(my_function(input1="5 ")) # default value

def mult_inputs(cat, *fruits):
    print(cat)
    print(fruits)

mult_inputs("meow", "banana", "apple") # dont use keywords with this, just ordered

# lambdas: small, one-off functions
x = lambda item1, item2: item1 + item2
print(x(item2="there", item1="hi "))