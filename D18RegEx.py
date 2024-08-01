import re as r

# match - only finds if string starts with substring (re.I is ignoring cases)
print(r.match("moon", "i moon", r.I))
print(r.match("moon", "Moonwalking", r.I))
# search - returns first instance found
print(r.search("son", "this is my fffson, he ate someone's son."))
# findall - finds all instances, returns list
print(r.findall("son", "this is my son, he ate someone's son."))
# sub - (target, replacement, string) replaces all instances of target with replacement
print(r.sub("!", " ", "z!a!b!c!d"))
# split - splits string into list of strings based on targeted key
print(r.split("#", "yams#peanuts#cookies"))
# lots of different search things with the r"" (see docs)
search = r"[a-zA-z0-9]om"
print(r.findall(search, "aom nom 9om Aom"))
# search for digits of length 5
search = r"\d{5}"
print(r.findall(search, "aom nom 9om 99999 9999"))