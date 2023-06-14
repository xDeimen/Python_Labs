
"""
Creatiun dictionarcare saafisezetoatecuvinteledintr-un text aflatintr-un fisiersinumarulde aparitiial fiecaruicuvant.
"""
import re

with open("text.txt", "r") as f:
    text = f.read()

text = re.sub(r'[^\w\s]', '', text)
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


for word, count in word_count.items():
    print(word, count)