
key = {'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'}

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char in key.values():
            for k, v in key.items():
                if v == char:
                    decrypted_text += k
        else:
            decrypted_text += char
    return decrypted_text

with open("text_criptat.txt", "r") as f:
    encrypted_text = f.read()

print("Textul criptat: ", encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print("Textul decriptat este:", decrypted_text)