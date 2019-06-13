import pandas as pd
import csv
from difflib import Differ


#this works, its just not what I need right now.
#currentmonth = pd.read_csv(r'C:\Users\Public\Documents\Audits\Duo_Audit\*.csv')
#lastmonth = pd.read_csv(r'C:\Users\Public\Documents\Audits\Duo_Audit\*.csv', usecols=['Username'])
currentmonth = pd.read_csv('new.csv')
lastmonth = pd.read_csv('old.csv', usecols=['Username'])
for df in [currentmonth, lastmonth]:
    df['Username'] = df['Username'].str.rstrip()
#result = pd.merge(currentmonth, lastmonth, on='Username', how='outer')
result = pd.concat([currentmonth, lastmonth], axis=0)
#result['Username'] = result['Username'].fillna('SerialN/A')
result = result.drop_duplicates(keep=False)
result.to_csv('results.csv', index=False)
print(result)
