import random

OP = ["a", "b", "c"]
comp = random.choice(OP)

print("Calculatorul a ales din lista", OP, "aleator: ", comp)
user = input("Alegeti un element din lista: ")

if user == comp:
    print("Bravo! Ai ghicit!")
else:
    print("Imi pare rau, ai gresit.", comp, ", nu", user)
