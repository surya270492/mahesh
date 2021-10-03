df = pd.read_json('h1-database.json')
df.head()
new_df=df[['Date','State','vaccinated_total','vaccinated_12+','Metro_status']]
del df
new_df['quarter'] = new_df['Date'].dt.quarter

#create unique list of names
Uniquequarters = new_df.quarter.unique()

#create a data frame dictionary to store your data frames
DataFrameDict = {elem : pd.DataFrame for elem in Uniquequarters}

for key in DataFrameDict.keys():
    DataFrameDict[key] = new_df[:][new_df.quarter == key]
for key,value in DataFrameDict.items():
     print("Table for quarter {}".format(key))
     print("{}".format(value))