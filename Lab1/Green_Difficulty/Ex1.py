import winsound

# Define the notes and their frequencies
notes = {
    'C4': 261,
    'D4': 277,
    'E4': 329,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 493,
    'C5': 523
}

# Define the melody as a list of tuples
melody = [
    ('E4', 4), ('A4', 6), ('C5', 4), ('B4', 4)
]

# Define the duration of a quarter note (in milliseconds)
quarter_note_duration = 250

# Play the melody
winsound.Beep(notes['E4'], 1000)
winsound.Beep(notes['A4'], 1500)
winsound.Beep(notes['C5'], 1000)
winsound.Beep(notes['B4'], 1000)
winsound.Beep(notes['A4'], 2000)



for note, duration in melody:
    frequency = notes[note]

