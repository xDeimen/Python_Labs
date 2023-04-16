
# întrebăm utilizatorul câte perechi de încălțăminte dorește să cumpere
numar_perechi = int(input("Câte perechi doriți să cumpărați? "))

# inițializăm prețul total cu prețul unei singure perechi
pret_unitar = 50  # exemplu de preț unitar fictiv
pret_total = numar_perechi * pret_unitar

# aplicăm reduceri de preț în funcție de numărul de perechi cumpărate
if numar_perechi >= 3 and numar_perechi <= 4:
    reducere = 0.05  # 5% reducere
    pret_total = pret_total * (1 - reducere)
elif numar_perechi >= 5 and numar_perechi <= 6:
    reducere = 0.1  # 10% reducere
    pret_total = pret_total * (1 - reducere)
elif numar_perechi >= 7:
    reducere = 0.15  # 15% reducere
    pret_total = pret_total * (1 - reducere)

# afișăm prețul final al achiziției cu reducerea de preț aplicată, dacă există
if reducere:
    print(f"Prețul final al achiziției este de {pret_total:.2f} lei, cu o reducere de {reducere*100:.0f}%.")
else:
    print(f"Prețul final al achiziției este de {pret_total:.2f} lei.")
