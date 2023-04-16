import time
import winsound

# definim un translator Morse
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
              'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
              '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '/': '.-.-.-', '?': '..--..'
              }

def text_to_morse(text):
    # convertim textul introdus în majuscule
    text = text.upper()
    morse_text = ""
    # traducem fiecare caracter în cod Morse
    for char in text:
        if char in morse_dict:
            morse_text += morse_dict[char] + " "
    return morse_text

# citim textul de la tastatură
text = input("Introduceti textul: ")

# convertim textul în cod Morse
morse_text = text_to_morse(text)

# afișăm textul în cod Morse
print("Textul introdus: ", text)
print("Cod Morse: ", morse_text)

# redăm textul sub formă de sunet
for char in morse_text:
    if char == '.':
        winsound.Beep(1000, 250)  # sunet de 1000Hz pentru o durată de 250ms pentru o perioadă de 1.
    elif char == '-':
        winsound.Beep(1000, 750)  # sunet de 1000Hz pentru o durată de 750ms pentru o perioadă de 1.
    elif char == ' ':
        time.sleep(0.5)  # pauză de 0,25 secunde între litere
    elif char == '/':
        time.sleep(1)  # pauză de 1 secunde între cuvinte
