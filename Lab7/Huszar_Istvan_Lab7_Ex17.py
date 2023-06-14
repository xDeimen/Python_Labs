import re
text = input();
pattern = r"\b[a-z]+\b"
m = re.findall(pattern,text)
print(m)
