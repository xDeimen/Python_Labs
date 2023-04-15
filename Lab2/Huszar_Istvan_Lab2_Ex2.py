'''
Am definit variabila cost_cazare ca fiind prețul pe noapte al hotelului (140 lei) înmulțit cu numărul de nopți de cazare.
Apoi, am folosit o declarație if-elif pentru a stabili prețul transportului în funcție de locația aleasă.
Am definit variabila cost_transport ca fiind prețul specific pentru locația respectivă.
Următorul pas a fost de a calcula costul închirierii mașinii.
Am definit variabila cost_inchiriere_masina ca fiind prețul pe zi al închirierii mașinii (40 lei) înmulțit cu numărul de nopți de cazare.
Am definit variabila cost_masa ca fiind suma pe care dorești să o cheltuiești pentru masă.
În final, am calculat costul total al călătoriei adunând toate costurile definite anterior.
Funcția returnează costul total calculat.
'''


def cost_calatorie(destinatie, nopti_cazare):
    cost_cazare = 140 * nopti_cazare
    if destinatie == "Cluj":
        cost_transport = 183
    elif destinatie == "Timisoara":
        cost_transport = 220
    elif destinatie == "Bucuresti":
        cost_transport = 222
    elif destinatie == "Iasi":
        cost_transport = 475
    else:
        print("Destinatie invalida")
        return 0

    cost_inchiriere_masina = 40 * nopti_cazare
    cost_masa = 600

    cost_total = cost_cazare + cost_transport + cost_inchiriere_masina + cost_masa

    return cost_total

print("Excursie la Cluj costa: ", cost_calatorie("Cluj", 3))
print("Excursie la Timisoara costa: ", cost_calatorie("Timisoara", 4))
print("Excursie la Bucuresti costa: ", cost_calatorie("Bucuresti", 6))
print("Excursie la Iasi costa: ", cost_calatorie("Iasi", 2))