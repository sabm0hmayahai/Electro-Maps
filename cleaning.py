
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#load the outrage dataset
dataset = pd.read_excel('BESCOM-electricity-data-outrage.xlsx')

#loading the holiday dataset
holiday = pd.read_excel('holidayData.xlsx')
#cleaning up the holiday data
holiday = holiday['Dates'].dt.date

#deleting useless columns from outrage data
x = dataset.iloc[:,1:-2]

del x['Circle']
del x['Substation']
del x['Subdivision']
del x['Feeders']
del x['Areas Affected']#idk

#adding labels
#add this later if de-activated
#x['Outrage'] = np.ones((x.shape[0]))

dates = x['From'].dt.date
fromTime = x['From'].dt.time
toTime = x['To'].dt.time

del x['From']
del x['To']

x['Date'] = dates
x['From Time'] = fromTime
x['To Time'] = toTime

x['Holiday'] = np.zeros((x.shape[0]))

ughdat = np.array(x['Date'])
dat = np.array(holiday)

#adding holiday data
for g in dat:
    if g in ughdat:
        tup = np.where(ughdat == g)
        for k in tup:
            x['Holiday'][k] = 1
      
#unique divisions        
div = x.Division.unique()

x = x.dropna(subset=['Division'])
x = x.reset_index(drop=True)

dic = {
       "HSR Division" : 105265,
       "Koramangala Division" : 63987,
       "Indiranagar" : 58830,
       "Shivajinagar" : 57437,
       "Hebbal" : 54301,
       "Whitefield" : 84428,
       "Malleshwaram" : 57107,
       "Rajaji Nagara Division" : 55250,
       "Jayanagar" : 56658,
       "Jalahalli" : 63391,
       "Kengeri Division" : 68087,
       "R R NAGAR" : 82848,
       "Vidhanasoudha" : 69057,
       "Peenya Division" : 96549
       }


x['Population'] = x['Division']
    
x = x.replace({"Population": dic})
  
#binarizer for divisions
from sklearn import preprocessing
lb = preprocessing.LabelBinarizer()
lb.fit(['HSR Division', 'Koramangala Division', 'Indiranagar',
       'Shivajinagar', 'Hebbal', 'Whitefield', 'Malleshwaram',
       'Rajaji Nagara Division', 'Jayanagar', 'Jalahalli',
       'Kengeri Division', 'R R NAGAR', 'Vidhanasoudha',
       'Peenya Division'])
lb.classes_
divs = lb.transform(x['Division'])

x = pd.concat([pd.DataFrame(divs), x], axis=1)

#del x['Date'] date needed for 
del x['Division']
del x['To Time']

#binarizer for hour of outrage
x['Hour'] = [f.hour for f in x['From Time']]

x['Duration'] = [f[7:9] for f in x['LC Duration']]

#outlier(s)
x = x.drop(index = 13993)

x['Duration'] = pd.to_numeric(x['Duration'])
x = x.reset_index(drop=True)

del x['LC Duration']

#binarizer for 24 hour value
lb = preprocessing.LabelBinarizer()
lb.fit([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
lb.classes_
hur = lb.transform(x['Hour'])

#fill this up later
x = pd.concat([pd.DataFrame(hur), x], axis=1)

del x['Hour']
del x['From Time']


temp_dataset = pd.read_excel('weather_data_max_min.xlsx')

t_dates = temp_dataset.iloc[:,0]
max_temp = temp_dataset.iloc[:,1]
min_temp = temp_dataset.iloc[:,2]

t_dates = t_dates.dt.date

max_dictionary = dict(zip(t_dates, max_temp))
min_dictionary = dict(zip(t_dates, min_temp))

max_list = np.zeros((x.shape[0]))
min_list = np.zeros((x.shape[0]))


for i in range(x.shape[0]):
    max_list[i] = max_dictionary[x['Date'][i]]
    min_list[i] = min_dictionary[x['Date'][i]]
    
x = pd.concat([pd.DataFrame(max_list), x], axis=1)
x = pd.concat([pd.DataFrame(min_list), x], axis=1)

del x['From Time']
del x['Date']

temp = pd.DataFrame()

#hour binarisation
for i in range(x.shape[0]):
    dur = x.iloc[i]['Duration']
    hr = x.iloc[i]['Hour']
    while dur>0:
        dur = dur - 1
        temp[temp.shape[1]] = x.iloc[i]
        temp[temp.shape[1]-1]['Hour']  = hr = (hr+1)%24
    
temp = temp.T
    

x.to_csv('cleanedup_with_date_temp.csv')



