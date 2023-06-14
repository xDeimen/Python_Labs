import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('curs_valutar.xlsx')
date_list = df['Data'].tolist()
ora_list = []
for date in date_list:
    ora = date.strftime('%H:%M:%S')
    ora_list.append(ora)

valori_consecutive = list(range(len(ora_list)))
plt.plot(ora_list, valori_consecutive, marker='o')
plt.xlabel('Ora')
plt.ylabel('Index')
plt.title('Ora cursului valutar')
plt.show()

