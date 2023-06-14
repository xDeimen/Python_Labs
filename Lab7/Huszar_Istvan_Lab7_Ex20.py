import re

text = "Temp -3.5 grade Celsius, temp maine fi 2.7 grade Celsius."
pattern = r"-?\b\d+(?:\.\d+)?\b"

matches = re.findall(pattern, text)

print(matches)
