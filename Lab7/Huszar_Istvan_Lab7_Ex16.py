import re

text = input();
pattern = r"\b\w+@\w+\.\w{2,}\b"
m = re.findall(pattern, text)
print(m)