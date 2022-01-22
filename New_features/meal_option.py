# -*- coding: utf-8 -*-
"""Meal_option.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NhUt-PCqUlmNpRbnvgdyLm6ZzPbX61Dt
"""

import pandas as pd #data processing

file='finalupd.csv' #load the current dataset 
df = pd.read_csv(file)
print(df.describe()) #statistics

food=df.copy() #copy of dataset to work with a new feature

food.drop(['Unnamed: 0'], axis=1, inplace=True) #drop the redundant column
food

#replace the values for the 'feature' column

food['final'] = food['final'].replace(['[db_fv, blablacar]','[db_fv, blablacar, db_fv]'],'[blablacar, db_fv]')
food['final'] = food['final'].replace(['[db_fv, flixbus]','[db_fv, flixbus, db_fv]','[db_fv, flixbus, db_fv, flixbus]','[db_fv, flixbus, db_fv, flixbus, db_fv]','[flixbus, db_fv, flixbus, db_fv]','[flixbus, db_fv, flixbus]'],'[flixbus, db_fv]')
food['final'] = food['final'].replace(['[flixbus, blablacar, db_fv]','[db_fv, blablacar, flixbus]','[db_fv, blablacar, flixbus, db_fv]','[blablacar, db_fv, flixbus]','[blablacar, flixbus, db_fv]','[db_fv, flixbus, blablacar, flixbus]','[flixbus, blablacar, db_fv, flixbus]','[flixbus, db_fv, blablacar]','[flixbus, blablacar, flixbus, db_fv]','[blablacar, db_fv, flixbus, db_fv]','[db_fv, blablacar, db_fv, flixbus]'],'[db_fv, flixbus, blablacar]')
food['final'] = food['final'].replace(['[flixbus, blablacar]','[flixbus, blablacar, flixbus]'],'[blablacar, flixbus]')
food['final'] = food['final'].replace(['[flixbus, flight, db_fv, flixbus]','[db_fv, flight, flixbus, db_fv]'],'[flixbus, flight, db_fv]')
food['final'] = food['final'].replace(['[flixbus, flight, flixbus]'],'[flixbus, flight]')

food['col'] = 0 #create a new column to correct the datatypes in a column, from string to array

"""For example, assume, that 'train,bus,train' == 'train, bus' or 'bus,train' == 'train,bus' to estimate the food alternatives, since we are interested in the mode and food policy on the transport used by the traveler during the trip and not in sequence of the same mode label with different names (different train companies or flight possibilities)

This initial label compression will further help to create the values in general and reduce the labels from 33 to 10 for assigning the special luggage estimation
"""

#function to correct the values 
def parse_modelabel(modelabel):
  modelabel = modelabel.strip("[]")#remove the brackets
  modelabel = modelabel.replace(" ", "") #replace the redundant spaces
  modelabel = modelabel.split(',')#make array from the string by comma
  return modelabel

#fill out the values row by row
for row in range(0, len(food)):
  food['col'][row] = parse_modelabel(food['final'][row])

"""The column would be populated with the categorical values.

References to estimate the meal possibilities in general:

FLIGHT mode in Germany: based on Lufthansa policy per food opportunities on board https://www.lufthansa.com/be/en/menus-in-economy-class and https://www.lufthansa.com/be/en/menus-on-short-and-medium-haul-flights We estimate food options based on 'economy class' policy assuming that the majority of users would fly with the usage of economy class tariff; Assign: up to 30 min- chocolate, up to 60 min - free water, 60+ min snacks, beverages,cold vegetarian dish, alcohol is possible

CAR mode in Germany: consider the private car transportation ; Assign: prepared own snacks, buying at gas stations

FLIXBUS mode in Germany: references https://global.flixbus.com/service/services-on-our-buses; Assign: prepared own snacks, on-board purshase of low cost snacks&drinks

TRAIN mode in Germany: based on Regional Express hhttps://www.happyrail.com/en/regional-express section catering, Deutsche Bahn https://www.bahn.de/service/zug/bordgastronomie and https://www.bahn.de/service/zug/bordgastronomie/bestellen-am-platz; Assigned: catering trolley, on-board catering  with '2-g rule'

BLABLACAR mode in Germany: built estimations based on blablabus food policy https://support.blablacar.com/hc/en-gb/articles/360014546640-Can-I-eat-on-board-a-BlaBlaCar-bus-; Assign: prepared cold food&drinks, no alcohol
"""

#prepare the food policy with estimations and assignment and populate the respective column 'meal_option"
def food_estimations(data):
  
  food_car = 'prepared own snacks, buying at gas stations'
  food_flixbus = 'prepared own snacks, on-board purshase of low cost snacks&drinks'
  food_train = 'catering trolley, on-board catering with 2-g rule'
  food_flight = 'up to 30 min- chocolate, up to 60 min - free water, 60+ min snacks, beverages,cold vegetarian dish, alcohol is possible' 
  food_blablacar = 'prepared cold food&drinks, no alcohol'

  comb1= 'prepared cold food&drinks, no alcohol + catering trolley, on-board catering with 2-g rule'
  comb2= 'prepared own snacks, on-board purshase of low cost snacks&drinks + catering trolley, on-board catering with 2-g rule'
  comb3= 'catering trolley, on-board catering with 2-g rule+ prepared own snacks, on-board purshase of low cost snacks&drinks+ prepared cold food&drinks, no alcohol'
  comb4= 'prepared cold food&drinks, no alcohol+ prepared own snacks, on-board purshase of low cost snacks&drinks'
  comb5='prepared own snacks, on-board purshase of low cost snacks&drinks+ up to 30 min- chocolate, up to 60 min - free water, 60+ min snacks, beverages,cold vegetarian dish, alcohol is possible+ catering trolley, on-board catering with 2-g rule'
  comb6= 'prepared own snacks, on-board purshase of low cost snacks&drinks+ up to 30 min- chocolate, up to 60 min - free water, 60+ min snacks, beverages,cold vegetarian dish, alcohol is possible'


  data['meal_option'] = "null" #new column
  for i in range(0, len(data)): #iterate

    if ["flixbus"] == data["col"].values[i]:
      data["meal_option"].values[i] = food_flixbus #check and assign the specific values per mode/combination 
    elif ["db_fv"] == data["col"].values[i]:
      data["meal_option"].values[i] = food_train
    elif ["car"] == data["col"].values[i]:
      data["meal_option"].values[i] = food_car
    elif ["blablacar"] == data["col"].values[i]:
      data["meal_option"].values[i] = food_blablacar

#in case of the combinations of modes per trip combine all the food options 
    elif ["blablacar", "db_fv"] == data["col"].values[i]: #blablacar policy is stricter
      data["meal_option"].values[i] = comb1
    elif ["flixbus", "db_fv"] == data["col"].values[i]: #flixbus policy is stricter
      data["meal_option"].values[i] = comb2
    elif ["db_fv", "flixbus", "blablacar"] == data["col"].values[i]: #flixbus policy is stricter
      data["meal_option"].values[i] = comb3
    elif ["blablacar", "flixbus"] == data["col"].values[i]: #flixbus policy is stricter
      data["meal_option"].values[i] = comb4
    elif ["flixbus", "flight", "db_fv"] == data["col"].values[i]: #assume here that flixbus rarely checks the heaviness of the laggage, use here the flight policy to follow the Lufthansa rules
      data["meal_option"].values[i] = comb5
    elif ["flixbus", "flight"] == data["col"].values[i]: ##assume here that flixbus rarely checks the heaviness of the laggage, use here the flight policy to follow the Lufthansa rules
      data["meal_option"].values[i] = comb6

food_estimations(food) #calculate

food#investigate the dataframe

#train involvement
food.loc[food['meal_option'] =='catering trolley, on-board catering with 2-g rule'] #examine the concrete values

#explore the uniqness of the created column
uniqueValues1 = food['meal_option'].unique() 
#enumeration 
uniqueValues2 = food['meal_option'].nunique() 
#count 
print (uniqueValues1) 
print (uniqueValues2)

"""10 unique possible rows got assigned"""

#download final Dataset for sharing with the team
from google.colab import files
food.to_csv('finalupd1.csv') 
files.download('finalupd1.csv')

#check the density of values
m = food.meal_option
counts = m.value_counts()
percent = m.value_counts(normalize=True)
percent100 = m.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
pd.DataFrame({'counts': counts, 'per': percent, 'per100': percent100})

"""the majority would be alligned with the train policy, minority is with 3 combinations involving the flight"""

#for Mykola to populate the dashboard per 2d feature

if best_recommendation_df.meal_option.to_string(index=False) == "catering trolley, on-board catering with 2-g rule":
                        st.write(
                            ":food: There is no need to prepare the snacks in advance, you can buy them on board. Restaurant serving options are possible in compliance with 2-g rule ")
                    elif best_recommendation_df.meal_option.to_string(index=False) == "prepared own snacks, on-board purshase of low cost snacks&drinks + catering trolley, on-board catering with 2-g rule":
                        st.write(
                            ":food: There is no need to bring the snacks with you, it would be possible to buy them in a bus. Restaurant serving options are available in compliance with 2-g rule in trains. However, your trip is combined and you may consider to buy your own edibles in advance. ")
                    elif best_recommendation_df.meal_option.to_string(index=False) == "prepared cold food&drinks, no alcohol + catering trolley, on-board catering with 2-g rule":
                        st.write(
                            ":food: You could only eat your own cold food in a bus.Catering trolley and the restaurant serving options are possible in compliance with 2-g rule in trains ")
                    elif best_recommendation_df.meal_option.to_string(index=False) == "prepared own snacks, on-board purshase of low cost snacks&drinks":
                        st.write(
                            ":snack: You can either prepare your own simple snacks and drinks in advance or purchase them on board the bus ")
                            
                    elif best_recommendation_df.meal_option.to_string(index=False) == "prepared own snacks, buying at gas stations":
                        st.write(
                            ":food: Driving your own car, consider the possibility of having a meal prepared in advance or stop at a gas station to satisfy your hunger ")
                            
                      
                    
                    elif best_recommendation_df.meal_option.to_string(index=False) == "catering trolley, on-board catering with 2-g rule+ prepared own snacks, on-board purshase of low cost snacks&drinks+ prepared cold food&drinks, no alcohol":
                        st.write(
                            ":food: Your trip incudes 3 different transports, where you can either buy food on board or bring your own food in advance. To get service in a restaurant , you must follow the 2-g rule ")
                            
                    elif best_recommendation_df.meal_option.to_string(index=False) == "prepared cold food&drinks, no alcohol+ prepared own snacks, on-board purshase of low cost snacks&drinks":
                        st.write(
                            ":snacks: Not all buses are equipped with the option of buying food, it is better to take care of your own nutritious cold snacks and beverages in advance ")
                            
                    elif best_recommendation_df.meal_option.to_string(index=False) == "prepared cold food&drinks, no alcohol":
                        st.write(
                            ":food: It is necessary to bring food with you, buying on board would be impossible, just like drinking alcohol ")
                            
                    elif best_recommendation_df.meal_option.to_string(index=False) == "prepared own snacks, on-board purshase of low cost snacks&drinks+ up to 30 min- chocolate, up to 60 min - free water, 60+ min snacks, beverages,cold vegetarian dish, alcohol is possible+ catering trolley, on-board catering with 2-g rule":
                        st.write(
                            ":food: Your trip involves an airplane, where meals are already included and a train where, according to the 2-g rule, you can get service in a restaurant. If you want to eat more on the bus, you can buy light snacks on board ")
                            
                    elif best_recommendation_df.meal_option.to_string(index=False) == "prepared own snacks, on-board purshase of low cost snacks&drinks+ up to 30 min- chocolate, up to 60 min - free water, 60+ min snacks, beverages,cold vegetarian dish, alcohol is possible":
                        st.write(
                            ":food: Your trip involves an airplane where meals are already included. If you want to eat more on the bus, you can buy light snacks on board or prepare the cold dishes & drinks in advance ")
