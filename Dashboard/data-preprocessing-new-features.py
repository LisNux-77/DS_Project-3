import pandas as pd

df = pd.read_csv(r"final.csv")

df.info()


# dropping unnecessary columns

df.drop(['Unnamed: 0', 'objective', 'col', 'final', 'finiteautomaton',  'totalnumberofchanges', 'numtravelto', 'numtravelfrom', 'travelto', 'travelfrom',
         'consideredpreferences'], inplace = True, axis = 1)


df.drop_duplicates(inplace=True)


df['totalwalkingdistance'] = (df['totalwalkingdistance'] * 1000).round(2).astype(int)

df.rename({'totalwalkingdistance': 'Total Walking Distance',
           'totalwaitingtime': 'Total Waiting Time',
           'totaltraveltimeinhours': 'Total Travel Time',
           'totalprice': 'Price',
           }, axis=1, inplace=True)

df.info()

df.to_csv("../data.csv", index=False)
