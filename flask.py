import os
import flask
import pandas as pd
import tensorflow as tf
from keras.models import load_model
import requests
import datetime
from sklearn import preprocessing
import numpy as np
from sklearn.preprocessing import StandardScaler
import json
import pickle
from sklearn.pipeline import Pipeline

# instantiate flask 
app = flask.Flask(__name__)

# load the model, and pass in the custom metric function
global graph
graph = tf.get_default_graph()
model = load_model('devhacks_weights_83p81.h5')

holidays_tt = ["2020-01-01",
                "2020-01-15",
                "2020-01-26",
                "2020-02-21",
                "2020-03-10",
                "2020-03-25",
                "2020-04-02",
                "2020-04-06",
                "2020-04-10",
                "2020-05-01",
                "2020-05-07",
                "2020-05-25",
                "2020-06-23",
                "2020-08-01",
                "2020-08-03",
                "2020-08-12",
                "2020-08-15",
                "2020-08-22",
                "2020-08-30",
                "2020-08-31",
                "2020-10-02",
                "2020-10-25",
                "2020-10-30",
                "2020-11-14",
                "2020-11-30",
                "2020-12-25"
                ]
url = "https://api.openweathermap.org/data/2.5/weather?q=Bengaluru,in&APPID=b1a275b64af38a8f9823800a58345b93"
# homepage
@app.route("/", methods=["GET","POST"])
def homepage():
    return flask.render_template("index.html")


#trained keras model
model = load_model('final_model.h5')


@app.route("/predict", methods=["POST"])
def predict():
    dat = flask.request.form['date']
    time = flask.request.form['time']

    if str(dat) in holidays_tt:
        holiday=1
    else:
        holiday=0
    
    
    
    response = requests.get(url).json()
    temp = float(response["main"]["temp"]) - 273.15
    temp_min = float(response["main"]["temp_min"]) - 283.15
    temp_max = float(response["main"]["temp_max"]) - 273.15
    pressure = response["main"]["pressure"]
    humidity = response["main"]["humidity"]


    
    #week
    date_time_obj = datetime.datetime.strptime(dat, '%Y-%m-%d')
    week = datetime.date(date_time_obj.year,date_time_obj.month,date_time_obj.day).isocalendar()[1]
    

    
    #hour
    hour = int(time[:-3])
    
    #population
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
    
    
    lb = preprocessing.LabelBinarizer()
    lb.fit(['HSR Division', 'Koramangala Division', 'Indiranagar',
       'Shivajinagar', 'Hebbal', 'Whitefield', 'Malleshwaram',
       'Rajaji Nagara Division', 'Jayanagar', 'Jalahalli',
       'Kengeri Division', 'R R NAGAR', 'Vidhanasoudha',
       'Peenya Division'])
    
    
    lt = list(dic.keys())
    
    df = pd.DataFrame(lt)
    
    divs = lb.transform(df)
    
    divs = pd.DataFrame(divs)
    
    week = [week]*14
    
    temp_max = [temp_max]*14
    temp_min = [temp_min]*14
                        
    holiday = [holiday]*14  
    
    divs = pd.concat([pd.DataFrame(temp_max), divs], axis=1)
    divs = pd.concat([pd.DataFrame(temp_min), divs], axis=1)
    divs = pd.concat([pd.DataFrame(week), divs], axis=1)
    divs = pd.concat([divs, pd.DataFrame(holiday)], axis=1)
    
        
    pop = [dic[x] for x in lt]
    
    #population
    divs = pd.concat([divs, pd.DataFrame(pop)], axis=1)
    
    
    hour = [hour]*14
    
    divs = pd.concat([ divs, pd.DataFrame(hour)], axis=1)
    
    
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    divs = sc_X.fit_transform(divs)
    

    
    with graph.as_default():
        prd = model.predict(divs)
    

    newprd = prd.tolist()


    #return to webpage
    return flask.render_template("index.html", data = newprd)
    
    
    
    
# start the flask app, allow remote connections 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)