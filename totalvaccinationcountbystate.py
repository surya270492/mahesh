import pandas as pd
df = pd.read_json('h1-database.json')
df.head()
df.groupby(['State'])['vaccinated_total'].sum()