def check_ADN(secventa):
    esantioane = ["GTA", "GGG", "CAG"]
    nr_aparitii = 0

    for esantion in esantioane:
        nr_aparitii += secventa.count(esantion)

    if nr_aparitii >= 3:
        return "Suspectul trebuie investigat mai departe."
    else:
        return "Suspectul nu mai este suspect."


ADN = "ATGTCAGGTAAGGGCTA"
rezultat = check_ADN(ADN)
print(rezultat)
