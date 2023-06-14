import re
text = input()
pattern = r"\b[A-Z][a-z]{4,}\b"
matches = re.findall(pattern, text)
print(matches)

