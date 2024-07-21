import re as r

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph = r.split(" ", paragraph)
a = r"\W"
new_para = []
word_count = []
for x in paragraph:
    if r.search(a, x) != None:
        x = r.sub(a, "", x)
    new_para.append(x)

for y in new_para:
    if ((new_para.count(y), f"{y}") in word_count) == False:
        word_count.append((new_para.count(y), y))
print(sorted(word_count, reverse=True))