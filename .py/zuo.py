import re
s=input()
for m in re.finditer(s,[1-9]\{5}):
    if m:
        print(m.group(0),end=',')

