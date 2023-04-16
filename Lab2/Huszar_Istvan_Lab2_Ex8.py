x = int(input("x= "))
y = int(input("y= "))
#Ce lipsește din următorul cod pentru a afișa 'Hello, world!' dacă x este mai mic decât 10 sau mai mare decât 20?
print("Ce lipsește din următorul cod pentru a afișa 'Hello, world!' dacă x este mai mic decât 10 sau mai mare decât 20?")
if x < 10 or x > 20:
    print("Hello, world!")

#Ce lipsește din următorul cod pentru a afișa 'Hello, world!' dacă x este mai mare decât 10 sau y este mai mic decât 20?
print("Ce lipsește din următorul cod pentru a afișa 'Hello, world!' dacă x este mai mare decât 10 sau y este mai mic decât 20?")
if x > 10 or y < 20:
    print("Hello, world!")

print("Problema interval")
'''
1.Intervalul A: numerele de la 0 la 9, inclusiv
2.Intervalul B: numerele pare de la 10 la 18, inclusiv
3.Intervalul C: numerele impare de la 11 la 19, inclusiv
'''
num = int(input("Introduceti un numar: "))

if num >= 0 and num <= 9:
    print("Numarul se incadreaza in intervalul A.")
elif num >= 10 and num <= 18 and num % 2 == 0:
    print("Numarul se incadreaza in intervalul B.")
elif num >= 11 and num <= 19 and num % 2 != 0:
    print("Numarul se incadreaza in intervalul C.")
else:
    print("Numarul nu se incadreaza in niciunul dintre intervalele specificate.")
