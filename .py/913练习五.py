import re
s=input()
mat=re.compile(r"[1-9]\d{5}")
ls=mat.findall(s.strip("\n"))
print(",".join(ls))

