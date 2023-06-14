import pandas as pd

# Definirea structurii datelor cu citate
data = {
    'id': [],
    'autor': [],
    'citat': []
}

# Definirea subiectului pentru citate
subiect = 'inteligenta'  # Înlocuiți cu subiectul dvs. de interes


numar_linii = 50  # Specificați numărul minim de linii de citate

for i in range(numar_linii):
    data['id'].append(i + 1)
    data['autor'].append('Autor ' + str(i + 1))
    data['citat'].append('Citat ' + str(i + 1) + ' despre ' + subiect)


df = pd.DataFrame(data)
nume_fisier_excel = 'citater_inteligenta.xlsx'  # Specificați numele fișierului Excel

df.to_excel(nume_fisier_excel, index=False)
df = pd.read_excel(nume_fisier_excel)
json_data = df.to_json(orient='records')

# Salvați datele JSON într-un fișier
nume_fisier_json = 'citater_inteligenta.json'  # Specificați numele fișierului JSON
with open(nume_fisier_json, 'w') as file:
    file.write(json_data)
