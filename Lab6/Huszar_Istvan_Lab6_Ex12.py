import pandas as pd
import random

df = pd.read_excel('date.xlsx', usecols=[0, 1])
df = df.iloc[1:]
random_data = []
for i in range(len(df)):
    random_data.append(''.join(random.sample(df.iloc[:, 0].tolist()[i], len(df.iloc[:, 0].tolist()[i]))))
df['Data aleatoare'] = random_data
with pd.ExcelWriter('date.xlsx', mode='a', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=len(df)+2)