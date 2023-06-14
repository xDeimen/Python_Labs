import winsound
import time

"""
C D E D C E E E
D D D E G G
C D E D C E E E
D D E D C
"""
# Definirea notelor și duratele corespunzătoare
notes = {
    'C': 261,  # frecvența pentru nota C
    'D': 293,  # frecvența pentru nota D
    'E': 329,  # frecvența pentru nota E
    'G': 392   # frecvența pentru nota G
}

duration = 500  # durata fiecărei note în milisecunde

# Definirea partiturii
sheet_music = [
    'C', 'D', 'E', 'D', 'C', 'E', 'E', 'E',
    'D', 'D', 'D', 'E', 'G', 'G',
    'C', 'D', 'E', 'D', 'C', 'E', 'E', 'E',
    'D', 'D', 'E', 'D', 'C'
]

# Redarea partiturii
for note in sheet_music:
    frequency = notes[note]
    winsound.Beep(frequency, duration)
    time.sleep(0.1)  # o pauză mică între note