import re
txt = str(input())
x = re.findall("a[b]{2,3}", txt)

print(x)
