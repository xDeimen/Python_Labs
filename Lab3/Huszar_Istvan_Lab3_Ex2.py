
'''
Acesta este un ciclu for care iterează prin elementele dintr-o listă generată dintr-un generator de listă (list comprehension).
Generatorul de listă creează o listă cu elementele j*0.1 pentru fiecare valoare a lui j în intervalul [0, 1, 2, ..., 9].

În cadrul corpului ciclului for, se afișează valoarea curentă a variabilei i și semnul →, dar și valoarea variabilei j, care a fost definită anterior în cod cu valoarea 1.
Dar deoarece valoarea variabilei j nu este modificată în niciun moment în corpul ciclului for, valoarea afișată va fi mereu 1.

Astfel, output-ul acestui cod va fi o listă de valori, fiecare dintre ele fiind o valoare din intervalul [0.0, 0.9] și urmată de semnul → și valoarea 1:
'''

j=1
for i in [j*0.1 for j in range(10)]:
    print (i, " → ", j)
