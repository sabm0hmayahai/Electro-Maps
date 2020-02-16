# Electro-Maps
<b>ML powered Electricity Outage Prediction. Know when and where there is a chance of an electricity outage to make more informed and smart decisions.</b>

## The problem Electro-Maps solves
Various industries and domestic factions run into problems with varying degree of significance by receiving no warnings about electricity outages. Electricity boards and government offices are often understaffed and unwilling to go out of their way to warn citizens. This may cause problems like inconvenience to students and educational institutes, retail stores etc. We can imagine more significant issues caused in Hospitals and the labour industry where critical operations depend on the surety of availability of electricity. It is a common practice to blame power outages on the 'big boys in the office' but according to a study conducted by Climate Central, 80% of electricity outages between the year 2003-2012 in USA were caused by the weather. This is why we take into account various components of the weather during our predictions.
Institutes and workshops can make use of this to know if there is a chance of an outage when they are conducting an activity or examination which depends on the availability of computing equipment.
Medical hospitals can be prepared with enough generator power to sustain them through an emergency outage situation.
Industries and such can plan alternate methods of turnover and customer interaction in case their online operations go down. Companies looking to open new operations in a region can be aware of the current and future predicted electricity outage frequency and plan accordingly after considering their own added electricity consumption. This makes them more liable for the well being of the society and assists us in understanding effects of our industrialisation over the years.
Household activities can also be assisted by making use of our application. Working of an electric pump, water heater, oven, electric stoves etc. can be stalled because of untimely outages. Members of the household can be warned beforehand, allowing them to make necessary arrangements.
So this application allows us to make smarter life choices.

## Challenges we ran into

We ran into a good number of challenges while scrapping and training the data and also while making the front-end for this application.
1) Scrapping the data provided to be hard as we had to get data from various different sources and map them according to the date, time and region.
2) Once our dataset was ready we got to training our Neural Network model on it. This proved to be task as we were unable to get a good accuracy value. We dove into the internet and soon realised that our dataset was not balanced. So we went back to the drawing board and came back with a more outage/no outage dataset for our model. With this we managed to get a good accuracy reading for both training and testing.
3) Once the model was ready, we thought of using flask for deploying the ML model and we took the challenge of considering x-factors for our model like current weather, min & max temp from an free API call, holidays in a year, current date and time by the user.
4) The inputs given were used to predict the electricity outage and we thought of using an opensource Map API to give a heatmap of the areas where there will be no electricity. We have used OpenStreetMap API for visualization of output data given by the model.
5) The output was in the form of a probability (an array which has 14 values) for each region of Bengaluru, we used this value and mapped with a colour depending on the probability and we have produced a heatmap.

## Instructions for running the project
1) Project has **Electro-Maps-Website** folder in where you can find all written codes.
2)  **Dashboard** is a homepage which generates the charts with dataset that we created. All hosted server files are linked       here.
    **Feedback** it is a interface created for users to submit feedback and suggestions. To run this just run 
    ***$node app.js***
    **Maps** this is done using flask which is connected with ML model and takes input from user and provides output in the       form of visulization on OpenStreetMaps (Opensource API). To run this run ***$python flaskproto.py***
3) Data was scrapped from BESCOM and Weather websites. Final dataset name **15th_3.12.xlsx**

# Image Gallery

![GitHub Logo](https://github.com/sabm0hmayahai/Electro-Maps/blob/master/images/Dashboard.JPG)
Format: ![Alt Text](url)

![GitHub Logo](https://github.com/sabm0hmayahai/Electro-Maps/blob/master/images/dashboard1.JPG)
Format: ![Alt Text](url)


![GitHub Logo](https://github.com/sabm0hmayahai/Electro-Maps/blob/master/images/dashboard2.JPG)
Format: ![Alt Text](url)


![GitHub Logo](https://github.com/sabm0hmayahai/Electro-Maps/blob/master/images/dashboard3.JPG)
Format: ![Alt Text](url)


![GitHub Logo](https://github.com/sabm0hmayahai/Electro-Maps/blob/master/images/feedback.JPG)
Format: ![Alt Text](url)

Project created at **DevHack 2.0** (36hrs Hackathon at IIT Dharwad, Karnataka) - **Team Sabm0hmayahai** 😄
