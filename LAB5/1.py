import re



txt = str(input())
x = re.findall("ab*", txt)

print(x)