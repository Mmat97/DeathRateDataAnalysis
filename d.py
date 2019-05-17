import pandas as pd
df = pd.read_csv (r'/Users/michaelmathew/Desktop/ComparisonDeathRates/NCHS_-_Leading_Causes_of_Death__United_States.csv')



print("The top 3 years from 1999-2016")

#print(df[['State']][df['Deaths'] == df['Deaths'].max()])
dx=df.sort_values(by=['Year','State', 'Deaths'])
print(dx)
