import re
text = input()
pattern = r"\b\d+\b"
m = re.findall(pattern,text)
print(m)
