
#1
print("1. Care dintre ele este mai mare")

num1 = int(input("Introduceți primul număr întreg: "))
num2 = int(input("Introduceți al doilea număr întreg: "))

if num1 > num2:
    print(f"{num1} este mai mare.")
else:
    print(f"{num2} este mai mare.")

#2
print("2. Verifică dacă numărul introdus este par sau impar.")

num = int(input("Introduceți un număr întreg: "))
if num % 2 == 0:
    print(f"{num} este un număr par.")
else:
    print(f"{num} este un număr impar.")

#3
print("3. Verifică dacă numărul introdus este pozitiv sau negativ.")

num = int(input("Introduceți un număr întreg: "))

if num > 0:
    print(f"{num} este un număr pozitiv.")
elif num < 0:
    print(f"{num} este un număr negativ.")
else:
    print("Numărul introdus este zero.")

#4
print("4. Compară cele două numere întregi introduse și afișează dacă ele sunt egale sau nu.")

num1 = int(input("Introduceți primul număr întreg: "))
num2 = int(input("Introduceți al doilea număr întreg: "))

if num1 == num2:
    print("Cele două numere sunt egale.")
else:
    print("Cele două numere sunt diferite.")

#5
print("5. Două șiruri de caractere și apoi afișează șirul de caractere care este mai lung.")

str1 = input("Introduceți primul șir de caractere: ")
str2 = input("Introduceți al doilea șir de caractere: ")

if len(str1) > len(str2):
    print(f"{str1} este mai lung.")
elif len(str1) < len(str2):
    print(f"{str2} este mai lung.")
else:
    print("Cele două șiruri de caractere au aceeași lungime.")

#6
print("6. Lista de numere; afișează cel mai mare număr.")

nums = list(map(int, input("Introduceți o listă de numere separate prin spațiu: ").split()))

max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num

print(f"Cel mai mare număr din listă este {max_num}.")

#7.
print("7. Ordine crescătoare.")

nums.sort()
print("Lista de numere în ordine crescătoare:", nums)

#8
print("8. Ordine descrescătoare")
nums.sort(reverse=True)
print("Lista de numere în ordine descrescătoare:", nums)

#9
print("9. Doua siruri de caractere de la tastatura")

str1 = input("Introduceți primul șir de caractere: ")
str2 = input("Introduceți al doilea șir de caractere: ")

#10
print("10. Siruri identice")
if str1 == str2:
    print("Cele două șiruri de caractere sunt identice.")
else:
    print("Cele două șiruri de caractere sunt diferite.")

#11
print("11. Siruri alphabetic")

if str1 < str2:
    print(f"{str1} este alfabetic mai înainte decât {str2}.")
elif str1 > str2:
    print(f"{str2} este alfabetic mai înainte decât {str1}.")
else:
    print("Cele două șiruri sunt identice din punct de vedere al ordinii alfabetic.")