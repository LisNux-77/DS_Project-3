# -*- coding: utf-8 -*-
"""Possible_expences.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ttA1gHjOBEW2gcWfb7biZ0cFe0yM0lDn

At first tried to allign a feature "possible_spendings" based on level of salaries per city and "Current cost of living" index= new dataset with alignment based on requests
"""

import pandas as pd #data processing
from pprint import pprint #“pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter
from collections import defaultdict #for the dictionary
import requests #allows to send HTTP requests using Python

cities = ['Gelsenkirchen', 'Oberhausen', 'Bonn', 'Duisburg', 'München',
       'Bochum', 'Solingen', 'Nürnberg', 'Karlsruhe', 'Wuppertal',
       'Hagen', 'Dortmund', 'Düsseldorf', 'Essen', 'Erlangen',
       'Osnabrück', 'Leipzig', 'Würzburg', 'Mannheim', 'Ulm', 'Bamberg',
       'Darmstadt', 'Köln', 'Stuttgart', 'Heidelberg', 'Erfurt', 'Berlin',
       'Aachen', 'Hamburg']

#tried per salary
url = 'https://www.salaryexpert.com/salary/area/germany/'
#url ='https://www.salaryexpert.com/salary/browse/cities/all/germany' # api-endpoint
for city in cities:
   url_1 = url + city

# define a params dict for the parameters to be sent to the API
PARAMS = {}
  
# send get request and save the response as response object
r = requests.get(url = url_1, params = PARAMS) 
  
# extract data in json format
#response = r.json() #parse the response

print(r.text) #not all the cities are available

#tried per "cost_of_living_index"
import requests

url = "https://cities-cost-of-living1.p.rapidapi.com/get_cities_details_by_name"

payload = "cities=%5B%7B%22name%22%3A%22Gelsenkirchen%22%2C%22country%22%3A%22Germany%22%7D%2C%7B%22name%22%3A%22Oberhausen%22%2C%22country%22%3A%22Germany%22%7D%2C%7B%22name%22%3A%22Bonn%22%2C%22country%22%3A%22Germany%22%7D%2C%7B%22name%22%3A%22Duisburg%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22M%C3%BCnchen%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Bochum%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Solingen%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22N%C3%BCrnberg%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Karlsruhe%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Wuppertal%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Hagen%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Dortmund%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Essen%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Erlangen%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Osnabr%C3%BCck%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Leipzig%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22W%C3%BCrzburg%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Mannheim%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Ulm%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Bamberg%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Darmstadt%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22K%C3%B6ln%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Stuttgart%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Heidelberg%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Erfurt%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Berlin%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Aachen%22%2C%22country%22%3A%22Germany%22%7D%2C%20%20%20%20%20%20%20%20%20%7B%22name%22%3A%22Hamburg%22%2C%22country%22%3A%22Germany%22%7D%5D&currencies=%5B%22EUR%22%5D"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "cities-cost-of-living1.p.rapidapi.com",
    'x-rapidapi-key': "2c73e79a5amsh17b21f93245545bp167176jsn436aae086a72"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

"""Again there are many towns that are not available with the index data

Since there are the discrepancies between having the data for cost living and salary per website (lack of information sometimes), it was finally decided to use the source https://www.numbeo.com/cost-of-living/country_result.jsp?country=Germany with the searching per each city for instance, https://www.numbeo.com/cost-of-living/in/Erlangen , per cost of living category and use the subsection Average Monthly Net Salary from the section Salaries And Financing.

Numbeo.com was launched in April 2009. The research and available data at Numbeo.com are not influenced by any governmental organization.

This website was mentioned or used as a source by many international newspapers and magazines including BBC, Time, The Week, Forbes, The Economist, Business Insider, San Francisco Chronicle, New York Times, The Telegraph, The Age, The Sydney Morning Herald, China Daily, The Washington Post, USA Today and dozens more.
"""

#mapping with the course data set
#load common dataset without new feature
file='finalupd1.csv'
new= pd.read_csv(file)
print(new.describe())

#add the new columns for computations and alignments:
new['salary'] = 0
new['possible_expences'] = 0

#average Monthly Net Salary, euro

gelsenkirchen = 2216
oberhausen = 2200 
bonn = 2604 
duisburg = 1920
münchen = 3139
bochum = 2617
solingen = 1900
nürnberg = 2858
karlsruhe = 2576
wuppertal = 2039
hagen = 1744
dortmund = 2586
düsseldorf = 2947
essen = 1860
erlangen = 3150
osnabrück = 2027
leipzig = 1840
würzburg = 2144
mannheim = 2325
ulm = 2733
bamberg = 2756
darmstadt = 2700
köln = 2477
stuttgart = 2999
heidelberg = 2860
erfurt = 2124
berlin = 3027
aachen = 2608
hamburg = 2883

#dataset
for i in range(0, len(new)): #iterate
#check and assign the specific salary values above per city
    if "Gelsenkirchen" == new["targetname"].values[i]:
      new["salary"].values[i] = gelsenkirchen
    elif "Oberhausen" == new["targetname"].values[i]:
      new["salary"].values[i] = oberhausen
    elif "Bonn" == new["targetname"].values[i]:
      new["salary"].values[i] = bonn
    elif "Duisburg" == new["targetname"].values[i]:
      new["salary"].values[i] = duisburg 
    elif "München" == new["targetname"].values[i]:
      new["salary"].values[i] = münchen
    elif "Bochum" == new["targetname"].values[i]:
      new["salary"].values[i] = bochum
    elif "Solingen" == new["targetname"].values[i]:
      new["salary"].values[i] = solingen
    elif "Nürnberg" == new["targetname"].values[i]:
      new["salary"].values[i] = nürnberg 

    elif "Karlsruhe" == new["targetname"].values[i]:
      new["salary"].values[i] = karlsruhe
    elif "Wuppertal" == new["targetname"].values[i]:
      new["salary"].values[i] = wuppertal
    elif "Hagen" == new["targetname"].values[i]:
      new["salary"].values[i] = hagen
    elif "Dortmund" == new["targetname"].values[i]:
      new["salary"].values[i] = dortmund
    elif "Düsseldorf" == new["targetname"].values[i]:
      new["salary"].values[i] = düsseldorf
    elif "Essen" == new["targetname"].values[i]:
      new["salary"].values[i] = essen
    elif "Erlangen" == new["targetname"].values[i]:
      new["salary"].values[i] = erlangen

    elif "Osnabrück" == new["targetname"].values[i]:
      new["salary"].values[i] = osnabrück 
    elif "Leipzig" == new["targetname"].values[i]:
      new["salary"].values[i] = leipzig
    elif "Würzburg" == new["targetname"].values[i]:
      new["salary"].values[i] = würzburg
    elif "Mannheim" == new["targetname"].values[i]:
      new["salary"].values[i] = mannheim
    elif "Ulm" == new["targetname"].values[i]:
      new["salary"].values[i] = ulm 
    elif "Bamberg" == new["targetname"].values[i]:
      new["salary"].values[i] = bamberg
    elif "Darmstadt" == new["targetname"].values[i]:
      new["salary"].values[i] = darmstadt

    elif "Köln" == new["targetname"].values[i]:
      new["salary"].values[i] = köln
    elif "Stuttgart" == new["targetname"].values[i]:
      new["salary"].values[i] = stuttgart 
    elif "Heidelberg" == new["targetname"].values[i]:
      new["salary"].values[i] = heidelberg 
    elif "Erfurt" == new["targetname"].values[i]:
      new["salary"].values[i] = erfurt
    elif "Berlin" == new["targetname"].values[i]:
      new["salary"].values[i] = berlin
    elif "Aachen" == new["targetname"].values[i]:
      new["salary"].values[i] = aachen
    elif "Hamburg" == new["targetname"].values[i]:
      new["salary"].values[i] = hamburg

#explore
new.loc[new['targetname'] == 'Gelsenkirchen']#salary 2216

new.loc[new['targetname'] == 'Köln'] #salary 2477

new.targetname.unique()# examine again the 29 cities

"""We assign the ratio per condition, where 4 represents the lowest indicator for possible spendings in a city and 1 the highest.

The cost of living is often used to compare how expensive it is to live in one city versus another. The cost of living is tied to wages. If expenses are higher in a city, such as New York(Munich), for example, salary levels must be higher so that people can afford to live in that city.
https://www.investopedia.com/terms/c/cost-of-living.asp#:~:text=The%20cost%20of%20living%20is%20often%20used%20to%20compare%20how,to%20live%20in%20that%20city.
"""

#populate the dataframe based on condition for the column (net income per month):

for k in range(0, len(new)): #iterate
  if new ["salary"].values[k] < 2000:
    new['possible_expences'][k] = 4 #assign the ratios

  elif new ["salary"].values[k] >= 2000 and new ["salary"].values[k] < 2500:
    new['possible_expences'][k] = 3

  elif new ["salary"].values[k] >= 2500 and new ["salary"].values[k] < 3000:
    new['possible_expences'][k] = 2

  elif new ["salary"].values[k] >= 3000:
    new['possible_expences'][k] = 1

new.loc[new['possible_expences'] == 1] #with the high level of spendings

new.loc[new['possible_expences'] == 4] #with the low level of spendings

new.drop(['Unnamed: 0', 'salary'], axis=1, inplace=True) #drop the redundant column
new

#download final Dataset for sharing with the team
from google.colab import files
new.to_csv('finalast.csv') 
files.download('finalast.csv')

#check the density of values
cc = new.possible_expences
counts = cc.value_counts()
percent = cc.value_counts(normalize=True)
percent100 = cc.value_counts(normalize=True).mul(100).round(1).astype(str) + '%'
pd.DataFrame({'counts': counts, 'per': percent, 'per100': percent100})

"""The highest group is the minority, the largest number of records belongs to the 2nd group, the average net salaries per city are still high"""

#for Mykola to populate the dashboard per 3d and last feature
if best_recommendation_df.possible_expences.to_string(index=False) == 4:
                        st.write(
                            ":money: The cost of living is relatively modest, enjoy your journey without high prices for goods and services")
                    elif best_recommendation_df.possible_expences.to_string(index=False) == 3:
                        st.write(
                            ":money: The cost of living is moderate, prices for goods and services are in the middle range. Most likely you will not find increased prices for goods and services ")
                    elif best_recommendation_df.possible_expences.to_string(index=False) == 2:
                        st.write(
                            ":money: Salaries in this city are quite high, which may directly indicate increased prices for goods and services, be prepared that the expenses may be significant ")
                    elif best_recommendation_df.possible_expences.to_string(index=False) == 1:
                        st.write(
                            ":money: Be prepared to spend spend quite a lot of money in the town of your choice, prices for goods and services will be above average, taking into account the cost of living and average net salaries of city residents ")
