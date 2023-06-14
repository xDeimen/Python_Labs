import requests

# Setările cererii HTTP către API
url = "URL_API"  # Înlocuiți "URL_API" cu URL-ul specificat în documentația API
headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY"  # Înlocuiți "YOUR_API_KEY" cu cheia de autentificare API RapidAPI
}

# Exemplu de cerere GET către API
response = requests.get(url, headers=headers)

# Obțineți datele din răspunsul API
data = response.json()

# Utilizați datele pentru a crea statistici și pentru a le afișa într-un "dashboard"


import pandas as pd
import matplotlib.pyplot as plt

# Procesați datele pentru a le adapta nevoilor dvs.
df = pd.DataFrame(data)  # Transformați datele într-un DataFrame pentru a le manipula mai ușor

# Creați diverse statistici și vizualizări utilizând biblioteca Matplotlib
# Exemplu: Histograma numărului de cazuri pe țări
plt.bar(df['country'], df['cases'])
plt.xlabel('Țară')
plt.ylabel('Număr de cazuri')
plt.title('Număr de cazuri COVID-19 pe țări')
plt.xticks(rotation=90)
plt.show()


