"""
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
"""

format = 5
print(f"{format} joe")

# word indexes
word = "Pillowcase"
""""
print(word[0]) # First letter
print(word[-1]) # Last letter
print(word[0:3]) # starts at zero index and up to 3 but not include 3
print(word[3:]) # Letter 3 to end
print(word[-3:]) # Last 3 letters
print(word[::-1]) # reversal
print(word[0:9:2]) # only print every 2 letters in a word
"""
# string methods
word1 = "this\tis\tfor\tpeashooters"
print(word1.capitalize()) # capitalize
print(word1.count("s", 3, 11)) # counts number of "s"'s, start, end
print(word1.startswith("t")) # returns a bool
print(word1.endswith("s")) # returns a bool
print(word1.expandtabs(6)) # changes all tabs to n number of spaces
print(word1.find("for")) # returns index of first occurence of string (-1 if not)
print(word1.rfind("s")) # returns index of last occurence of string (-1 if not)

print(word1.isalnum()) # bool, true if whole string is alphanumerical (spaces make this false)
print(word1.isalpha()) # same as above with letters
print(word1.isdecimal()) # same but with ints 0-9
print(word1.isdigit()) # same as above but with some weird representations of 0-9 as well
print(word1.isnumeric()) # same but with all numbers
print(word1.isidentifier()) # checks if string could be used as a variable (doesnt start with num, no spaces, etc)
print(word1.islower()) # bool all lowercase
print(word1.isupper()) # bool all uppercase

word2 = ["Hi ", "there"]
word3 = "wWigglerr"
word4 = "Whats! up! man!"
print("".join(word2)) # joins strings; can only take 1 input for the strings
print(word3.strip("rw")) # removes characters at end or beginning of string
print(word3.replace("rr", "rs")) # replaces first given instances with second given
print(word4.split("!")) # splits string into list with words, by default based on space but can input others
print(word4.title()) # Capitalizes All
print(word4.swapcase()) # swaps upper and lowercase