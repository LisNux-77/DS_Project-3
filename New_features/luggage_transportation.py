# -*- coding: utf-8 -*-
"""Luggage_transportation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EUkRI2F0JUHeMIU4-5zStpOt5_tP494X
"""

import pandas as pd #data processing

file='finalnew.csv' #load the current dataset 
df = pd.read_csv(file)
print(df.describe()) #statistics

baggage=df.copy() #copy of dataset to work with a new feature

baggage.drop(['Unnamed: 0'], axis=1, inplace=True) #drop the redundant column
baggage

baggage['final'] = baggage.loc[:, 'finalsolutionusedlabels'] #create a duplicate of a column for shrinking the labels to calculate the probabilities

#replace the values for the 'feature' column

baggage['final'] = baggage['final'].replace(['[db_fv, blablacar]','[db_fv, blablacar, db_fv]'],'[blablacar, db_fv]')
baggage['final'] = baggage['final'].replace(['[db_fv, flixbus]','[db_fv, flixbus, db_fv]','[db_fv, flixbus, db_fv, flixbus]','[db_fv, flixbus, db_fv, flixbus, db_fv]','[flixbus, db_fv, flixbus, db_fv]','[flixbus, db_fv, flixbus]'],'[flixbus, db_fv]')
baggage['final'] = baggage['final'].replace(['[flixbus, blablacar, db_fv]','[db_fv, blablacar, flixbus]','[db_fv, blablacar, flixbus, db_fv]','[blablacar, db_fv, flixbus]','[blablacar, flixbus, db_fv]','[db_fv, flixbus, blablacar, flixbus]','[flixbus, blablacar, db_fv, flixbus]','[flixbus, db_fv, blablacar]','[flixbus, blablacar, flixbus, db_fv]','[blablacar, db_fv, flixbus, db_fv]','[db_fv, blablacar, db_fv, flixbus]'],'[db_fv, flixbus, blablacar]')
baggage['final'] = baggage['final'].replace(['[flixbus, blablacar]','[flixbus, blablacar, flixbus]'],'[blablacar, flixbus]')
baggage['final'] = baggage['final'].replace(['[flixbus, flight, db_fv, flixbus]','[db_fv, flight, flixbus, db_fv]'],'[flixbus, flight, db_fv]')
baggage['final'] = baggage['final'].replace(['[flixbus, flight, flixbus]'],'[flixbus, flight]')

"""For instance, assume, that 'train,bus,train' == 'train, bus' or 'bus,train' == 'train,bus' to estimate the luggage policy, since we are interested in the mode and policy per transportation regime, that the traveler uses during the trip and not in sequence of the same mode label with different names (different train companies or flight possibilities)

This initial label compression will further help to create the values in general and reduce the labels from 33 to 10 for assigning the special luggage estimation
"""

baggage['col'] = 0 #create a new column to correct the datatypes in a column, from string to array

#function to correct the values 
def parse_modelabel(modelabel):
  modelabel = modelabel.strip("[]")#remove the brackets
  modelabel = modelabel.replace(" ", "") #replace the redundant spaces
  modelabel = modelabel.split(',')#make array from the string by comma
  return modelabel

#fill out the values row by row
for row in range(0, len(baggage)):
  baggage['col'][row] = parse_modelabel(baggage['final'][row])

"""The column will be populated with the categorical records.

References to estimate the policy in general:

FLIGHT mode in Germany: based on Lufthansa policy per carry-on luggage
https://www.lufthansa.com/de/en/carry-on-baggage and free baggage https://www.lufthansa.com/us/en/baggage-and-other-fees
We estimate based on economy class policy assuming that the majority of users would fly with the usage of economy class tariff;
Assign: 1 hand up to 8kg, 1 free checked baggage up to 23 kg, additional bags per fee

CAR mode in Germany: consider the 'Opel' car brand produced in Germany as an average car for usage with the prices for an ordinary customer= could possibly include unlimited hand bags and up to 6 moderate baggages wrt to dimensions into the boot;
Assign: hand bags, 6 bags, unlimited weight

FLIXBUS mode in Germany: references https://global.flixbus.com/service/luggage;
Assign:1 carry-on bag up to 7 kg, 1 free checked baggage up to 20 kg, additional bags per fee

TRAIN mode in Germany: based on Regional Express https://www.happyrail.com/en/regional-express and Deutsche Bahn https://www.bahn.com/en/trains/luggage
Assigned unlimited carry-on and standard bags,no extra charge

BLABLACAR mode in Germany: built estimations based on blablabus luggage policy https://www.thetrainline.com/bus-companies/blablabus;
two pieces of hand luggage and two pieces of checked baggage per passenger free of charge. Luggage placed in the hold must not exceed a maximum weight of 23kg and a cumulative size of 200cm (length + width + depth);
Assign:2 pieces of hand luggage, 2 pieces of checked baggage, additional bags per fee

"""

#outline the luggage estimations values and populate the respective column 'luggage_transportation"
def luggage_policy_estimations(data):
  
  luggage_policy_car = 'several hand bags, 6 bags, unlimited weight'
  luggage_policy_flixbus = '1 carry-on bag up to 7 kg, 1 free checked baggage up to 20 kg, additional bags per fee'
  luggage_policy_train = 'unlimited carry-on and standard bags,no extra charge'
  luggage_policy_flight = '1 carry-on bag up to 8kg, 1 free checked baggage up to 23 kg, additional bags per fee' 
  luggage_policy_blablacar = '2 pieces of hand luggage, 2 free pieces of checked baggage up to 23 kg, additional bags per fee'


  data['luggage_transportation'] = "null" #new column
  for i in range(0, len(data)): #iterate

    if ["flixbus"] == data["col"].values[i]:
      data["luggage_transportation"].values[i] = luggage_policy_flixbus #check and assign the specific values per mode/combination
    elif ["db_fv"] == data["col"].values[i]:
      data["luggage_transportation"].values[i] = luggage_policy_train
    elif ["car"] == data["col"].values[i]:
      data["luggage_transportation"].values[i] = luggage_policy_car
    elif ["blablacar"] == data["col"].values[i]:
      data["luggage_transportation"].values[i] = luggage_policy_blablacar

#in case of the combinations of modes per trip the strictest policy on suitcases has been taken into account and probabilities of the heavy luggage to be checked on blablabus fleet 
    elif ["blablacar", "db_fv"] == data["col"].values[i]: #blablacar policy is stricter
      data["luggage_transportation"].values[i] = luggage_policy_blablacar
    elif ["flixbus", "db_fv"] == data["col"].values[i]: #flixbus policy is stricter
      data["luggage_transportation"].values[i] = luggage_policy_flixbus
    elif ["db_fv", "flixbus", "blablacar"] == data["col"].values[i]: #flixbus policy is stricter
      data["luggage_transportation"].values[i] = luggage_policy_flixbus
    elif ["blablacar", "flixbus"] == data["col"].values[i]: #flixbus policy is stricter
      data["luggage_transportation"].values[i] = luggage_policy_flixbus
    elif ["flixbus", "flight", "db_fv"] == data["col"].values[i]: #assume here that flixbus rarely checks the heaviness of the laggage, use here the flight policy to follow the Lufthansa rules
      data["luggage_transportation"].values[i] = luggage_policy_flight
    elif ["flixbus", "flight"] == data["col"].values[i]: ##assume here that flixbus rarely checks the heaviness of the laggage, use here the flight policy to follow the Lufthansa rules
      data["luggage_transportation"].values[i] = luggage_policy_flight

luggage_policy_estimations(baggage) #calculate

baggage#investigate the dataframe

#blablacar involvement
baggage.loc[baggage['luggage_transportation'] =='2 pieces of hand luggage, 2 free pieces of checked baggage up to 23 kg, additional bags per fee'] #examine the concrete values

#explore the uniqness of the created column
uniqueValues1 = baggage['luggage_transportation'].unique() 
#enumeration 
uniqueValues2 = baggage['luggage_transportation'].nunique() 
#count 
print (uniqueValues1) 
print (uniqueValues2)

"""5 different options were assigned"""

#download final Dataset for sharing with the team
from google.colab import files
baggage.to_csv('finalupd.csv') 
files.download('finalupd.csv')

#check the density of values
m = baggage.luggage_transportation
counts = m.value_counts()
percent = m.value_counts(normalize=True)
percent100 = m.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
pd.DataFrame({'counts': counts, 'per': percent, 'per100': percent100})

"""40% stands for unlimited, 38.5 for 1 hand bag and 1 free checked baggage, the minority only 178 records per flight estimations"""

#for Mykola to populate the dashboard

if best_recommendation_df.luggage_transportation.to_string(index=False) == "unlimited carry-on and standard bags,no extra charge":
                        st.write(
                            ":bag: The luggage policy is generous, enjoy your trip with no limitations on board of RE/RB, Deutsche Bahn- trains")
                    elif best_recommendation_df.luggage_transportation.to_string(index=False) == "1 carry-on bag up to 7 kg, 1 free checked baggage up to 20 kg, additional bags per fee":
                        st.write(
                            ":bag: The luggage policy is pretty strict, although suitcases may not be checked and weighed. However, it is recommended to follow the rules of the carrier company: an upper bound is 1 carry-on bag up to 7 kg& 1 free checked baggage up to 20 kg. An additional bags might be included per fee")
                    elif best_recommendation_df.luggage_transportation.to_string(index=False) == "2 pieces of hand luggage, 2 free pieces of checked baggage up to 23 kg, additional bags per fee":
                        st.write(
                            ":bag: The luggage policy is moderate and you can bring a lot of things with you.The suitcases may not be checked and weighed. However, it is recommended to follow the rules of the carrier company: an upper bound is 2 pieces of hand luggage, 2 free pieces of checked baggage up to 23 kg, additional bags per fee "
                            "destination__")
                    elif best_recommendation_df.luggage_transportation.to_string(index=False) == "several hand bags, 6 bags, unlimited weight":
                        st.write(
                            ":bag: You are the host of your own baggage policy, since you are traveling by your private car. It is recommended to take into account the number of passengers in the car and the volume of the trunk to calculate the luggage that can be placed inside "
                            "destination__")
                    elif best_recommendation_df.luggage_transportation.to_string(index=False) == "1 carry-on bag up to 8kg, 1 free checked baggage up to 23 kg, additional bags per fee":
                        st.write(
                            ":bag: The luggage policy is strict, the suitcases will be 100% checked with respect to the dimensions and weighed. It is highly recommended to follow the rules of the carrier company: an upper bound is 1 carry-on bag up to 8kg, 1 free checked baggage up to 23 kg, additional bags per fee "
                            "destination__")