import re
text = input()
p = r"\b[A-Z][a-z]*\b"
m = re.findall(p,text)
print(m)