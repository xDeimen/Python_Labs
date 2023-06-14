import re

text = "ship, kale, rest,"
pattern = r"\bs\w*[aeiouAEIOU]\w*\b"

matches = re.findall(pattern, text)

print(matches)
