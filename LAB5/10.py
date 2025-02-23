import re
txt= input()
x= re.sub("(.)([A-Z])", r"\1_\2", txt).lower()

print(x)
