import re as r

def var_check(var):
    if r.search(r"^\d", var) != None or r.search(r"\W", r.sub("_", "", var)) != None:
        return False
    else:
        return True
test_var = input("Input a variable name to test: ")
if var_check(test_var) == True:
    print("Valid!")
else:
    print("Invalid :(")