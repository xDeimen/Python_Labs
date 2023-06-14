import winsound
import time

# Funcție pentru a calcula numerele prime ale secvenței Fibonacci
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Solicitarea utilizatorului pentru introducerea unui număr întreg
n = int(input("Introduceți un număr întreg: "))

# Calcularea primelor n numere prime Fibonacci
fib_nums = fibonacci(n)

# Generarea melodiei bazate pe numerele prime Fibonacci
melodie = []
for num in fib_nums:
    frequency = 440 * 2**((num-49)/12)
    # Verificarea și ajustarea frecvenței, dacă este necesar
    if frequency < 37:
        frequency = 37
    elif frequency > 32767:
        frequency = 32767
    duration = 500  # durata fiecărei note în milisecunde
    melodie.append((frequency, duration))

# Funcție pentru redarea unei singure note
def play_note(frequency, duration):
    winsound.Beep(int(frequency), duration)

# Redarea întregii melodii
def play_melody(melodie):
    for frequency, duration in melodie:
        play_note(frequency, duration)
        time.sleep(0.1)  # o pauză mică între note

# Redarea melodiei generate
play_melody(melodie)