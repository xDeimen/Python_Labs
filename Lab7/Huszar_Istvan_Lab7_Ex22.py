import re
text = "Mama mananca Placinta pe malul Marii Negre, si se uita Cum doi Pescarusi zboara in Larg."
pattern = r"\b[A-Z][a-z]*[aeiou]\b"
matches = re.findall(pattern, text)
print(matches)

