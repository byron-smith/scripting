import pandas as pd

'''Count unique workstartdates for timesheet data. Can ignore paycodes that do not trigger work.'''

# when we have a list of paycodes to ignore. Filter them out on the .read_csv step if possible
df = pd.read_csv("Source_5_22.csv", usecols=[8,45,47]) #only grab SSN, WorkStartDate, PayCode

df.insert(2,'VACM','VACM')#

#df = df.loc[((df['PayCode'] == '497') | (df['PayCode'] == '10'))] #filter df for only rows with Paycode equal to provided values
df = df.loc[( (df['PayCode'] != '543') & (df['PayCode'] != '383') &(df['PayCode'] != '72') & (df['PayCode'] != '201') & (df['PayCode'] != '344') & (df['PayCode'] != '73') & (df['PayCode'] != '434') & (df['PayCode'] != '978') & (df['PayCode'] != '71'))] # filter df to include all but these paycodes

out = df.groupby(['SSN'])['WorkStartDate'].nunique() #group by SSN and count unique WorkStartDates

out.to_csv("counted.csv") #print to a csv
#print(out.head(15)) #for testing in shell
