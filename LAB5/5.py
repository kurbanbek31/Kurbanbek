import re

txt = str(input())
x = re.match('a.*b$', txt)

print(x.group())


