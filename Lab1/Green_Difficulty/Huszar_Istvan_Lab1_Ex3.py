import winsound
import time

# Definirea dicționarului de mape note-litere
note_freq = {
    'A': 440.00,
    'B': 493.88,
    'C': 523.25,
    'D': 587.33,
    'E': 659.25,
    'F': 698.46,
    'G': 783.99
}

# Solicitarea utilizatorului pentru introducerea propoziției
propozitie = input("Introduceți o propoziție: ")

# Definirea cheii muzicale și modelului ritmic
cheie_muzicala = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
model_ritmic = [500, 400, 300, 200, 100]

# Generarea melodiei bazate pe propoziție
melodie = []
for litera in propozitie:
    if litera.isalpha():
        nota = cheie_muzicala[ord(litera.upper()) % len(cheie_muzicala)]
        durata = model_ritmic[len(melodie) % len(model_ritmic)]
        melodie.append((nota, durata))

# Funcție pentru redarea unei singure note
def play_note(note, duration):
    frequency = note_freq[note]
    winsound.Beep(int(frequency), duration)

# Redarea întregii melodii
def play_melody(melody):
    for note, duration in melody:
        play_note(note, duration)
        time.sleep(0.1)  # o pauză mică între note

# Redarea melodiei generate
play_melody(melodie)