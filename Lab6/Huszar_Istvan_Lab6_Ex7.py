import pandas as pd
import matplotlib.pyplot as plt

# URL-ul către fișierul CSV
url = "https://data.gov.ro/dataset/abcd.csv"

# Citirea datelor din URL și stocarea lor într-un DataFrame
df = pd.read_csv(url)

# Afișarea datelor pentru a verifica dacă au fost încărcate corect
print(df.head())

# Exemplu de creare a unui grafic (puteți ajusta codul pentru a vă potrivi nevoilor)
plt.figure(figsize=(10, 6))
df.plot(x='data', y='valoare', kind='line')
plt.xlabel('Data')
plt.ylabel('Valoare')
plt.title('Graficul valorilor în funcție de dată')
plt.show()