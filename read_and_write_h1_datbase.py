import pandas as pd
df=pd.read_excel('COVID-19_Vaccinations_in_the_United_States_County-1.xlsx')
df=df.replace({pd.NaT:None})
df=df.where(pd.notnull(df),None)
df.head()
#converting into dataframe to json
sample_json = df.to_json(orient="records")
# Writing to sample.json
with open("h1-database.json", "a") as outfile:
    for json in sample_json:
        
        outfile.write(json)
        
