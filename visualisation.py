import pandas as pd
import numpy as np

dataset = pd.read_csv(r'visualisation_dataset.csv')

dataset=dataset.iloc[:,1:]

#Total outages per region
counts = dataset.groupby('Region').size()

#Total outages per week basis
weeks= dataset.groupby('week').size()

outageOnHolidays=np.zeros((len(counts),1))

countD =pd.DataFrame()
countD['Regions']=counts.keys()
countD['Outagesintot'] = counts.values

month=[]

for k in range(0,len(counts)):
    for i in range(dataset.shape[0]):
        if(dataset['Holiday'][i]==1):
            if(dataset['Region'][i]==countD['Regions'][k]):
                outageOnHolidays[k]+=1
    

countD['OOH']=outageOnHolidays

for i in range(0,dataset.shape[0]):
    x = dataset['Date'][i]
    y = int(x[5:7])
    month.append(y)
    
dataset['Month'] = month

mc = []

for i in range(0,len(counts)):
    mc.append(0)
x=[]
for i in range(0,12):
    x.append(0)
for i in range(0,len(counts)):
    mc[i]=x    

#Outages in each region per month
xc=dataset.groupby(['Month','Region']).size()


