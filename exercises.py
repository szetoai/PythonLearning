import re as r

paragraph = input("Enter Paragraph: ")
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