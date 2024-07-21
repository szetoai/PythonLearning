import re as r

txt = input("Enter Paragraph: ")
txt = r.split(" ", txt)
a = r"\W"
new_para = []
counted_para = []
for x in txt:
    if r.search(a, x) != None:
        x = r.sub(a, "", x)
    new_para.append(x)
for y in new_para:
    if ((new_para.count(y), f"{y}") in counted_para) == False:
        counted_para.append((new_para.count(y), y))
print(sorted(counted_para, reverse=True))