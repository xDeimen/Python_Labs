import pandas as pd

url = "https://data.gov.ro/dataset/abcd.csv"
df = pd.read_csv(url)
df.to_excel('rezultat.xlsx', index=False)