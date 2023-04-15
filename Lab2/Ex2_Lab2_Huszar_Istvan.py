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