
"""
Pentru a putea transmite codul Morse cvasi-simultan cu introducerea textului de la tastatură în Python,
putem folosi pachetul keyboard pentru a detecta apăsarea tastelor și funcția winsound.Beep()
pentru a reproduce sunetele codului Morse.
"""
import keyboard
import time
import winsound

# Definim tabela de conversie Morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


def play_morse_sound(duration):
    # Reproducem un ton de 800 Hz cu durata specificată
    winsound.Beep(800, int(duration * 1000))

# Funcția care convertește textul în cod Morse și transmite codul cvasi-simultan cu introducerea textului
def transmit_morse():
    text = ''
    while True:
        # Așteptăm apăsarea unei taste
        event = keyboard.read_event()
        # Dacă s-a apăsat o tastă de caractere, adăugăm caracterele la text
        if event.event_type == 'down' and event.name.isprintable():
            text += event.name.upper()

            """
            În Python, flush=True specifică dacă trebuie să se forțeze golirea buffer-ului după ce afișează textul dat. 
            Acest lucru poate fi util pentru a asigura faptul că textul este afișat imediat, fără întârzieri.
            De asemenea, end='' este un argument opțional pentru funcția de afișare print() care specifică ce să afișeze la sfârșitul liniei. 
            În loc de a afișa un caracter nou la sfârșitul fiecărei apelări, end='' specifică să nu se afișeze nimic. 
            Astfel, dacă se fac mai multe apeluri print() consecutiv, textul afișat nu va fi pe linii separate
            """
            print(event.name.upper(), end='', flush=True)  # afișăm caracterul pe ecran
            if event.name.upper() in morse_dict:
                # Convertim caracterul în cod Morse și transmitem sunetele codului Morse
                code = morse_dict[event.name.upper()]
                for symbol in code:
                    if symbol == '.':
                        play_morse_sound(0.2)
                    elif symbol == '-':
                        play_morse_sound(0.5)
                time.sleep(0.2)  # pauză între caractere
            else:
                time.sleep(0.1)  # pauză pentru tastele care nu sunt în tabelul Morse
        # Dacă s-a apăsat tasta Enter, încheiem transmisia și ieșim din funcție

transmit_morse()