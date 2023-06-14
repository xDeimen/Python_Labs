import re

text = "VISA credit card number is 4444 1111 2222 4040 or 5015 2222 3333 1221"
pattern = r"\d{4} \d{4} \d{4} \d{4}"
matches = re.findall(pattern,text)
print(matches)
