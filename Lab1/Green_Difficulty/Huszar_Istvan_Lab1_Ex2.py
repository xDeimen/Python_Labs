import winsound
import time

# Definirea listei de note muzicale
note_freq = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}

# Definirea unei melodii simple
melodie = [
    ('C', 500),  # nota C cu durata de 500ms
    ('D', 500),  # nota D cu durata de 500ms
    ('E', 500),  # nota E cu durata de 500ms
    ('F', 500)   # nota F cu durata de 500ms
]

# Funcție pentru redarea unei singure note
def play_note(note, duration):
    frequency = note_freq[note]
    winsound.Beep(int(frequency), duration)

# Redarea întregii melodii
def play_melody(melody):
    for note, duration in melody:
        play_note(note, duration)
        time.sleep(0.1)  # o pauză mică între note

# Redarea melodiei definite
play_melody(melodie)

# Exemplu de experimentare cu melodii
# melodie = [
#     ('C', 500),
#     ('G', 1000),
#     ('A', 750),
#     ('F', 500)
# ]
# play_melody(melodie)