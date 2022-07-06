import warnings
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

warnings.filterwarnings("ignore")

valve_df = pd.read_csv('C:\\Users\\PC\\Downloads\\valve_games.csv')
valve_df['Release'] = pd.to_datetime(valve_df['Release'], format = '%B %d, %Y')
# print(valve_df)

blizzard_df = pd.read_csv('C:\\Users\\PC\\Downloads\\blizzard_games.csv')
# changes the format of the Release dates of the games to a format like 1992-03-19 (at least i think so)
blizzard_df['Release'] = pd.to_datetime(blizzard_df['Release'], format = '%B %d, %Y')
# print(blizzard_df.head())

# General insight on what Genre each game company creates
# On what platform they mostly base their games
# And what mode the games are played in
'''
print(valve_df['Genre(s)'].value_counts().head(3))
print('------------------------------')
print(blizzard_df['Genre(s)'].value_counts().head(3))
print('------------------------------')
print(valve_df['Platform(s)'].value_counts().head(3))
print('------------------------------')
print(blizzard_df['Platform(s)'].value_counts().head(3))
print('------------------------------')
print(valve_df['Mode(s)'].value_counts().head(3))
print('------------------------------')
print(valve_df['Mode(s)'].value_counts().head(3))
'''

score_data_valve = valve_df[['Name', 'Metascore', 'User Score', 'Release']]

score_data_blizzard = blizzard_df[['Name', 'Metascore', 'User Score', 'Release']]

score_data_valve['Game Company'] = 'Valve'
score_data_blizzard['Game Company'] = 'Blizzard'
score_data = pd.concat([score_data_valve, score_data_blizzard], ignore_index=True)
#print(score_data)
#print(score_data.head())

# removes the row if theres NaN value in Metascore and User Score (since technically the game is not out yet)
score_data = score_data.dropna(subset = ['Metascore', 'User Score'], thresh=1)
score_data = score_data.reset_index(drop=True)
# print(score_data.tail())

score_data['Metascore filled'] = [uscore * 10 if np.isnan(score_data['Metascore'][i])
                    else score_data['Metascore'][i] for i, uscore in enumerate(score_data['User Score'])]




data_for_cluster = score_data[['Metascore filled', 'User Score']]
kmeans = KMeans(n_clusters=4, random_state=0).fit(data_for_cluster)
clusters = kmeans.predict(data_for_cluster)
score_data['Cluster'] = clusters
# print(score_data)

valve_games = score_data[score_data['Game Company'] == 'Valve']
blizzard_games = score_data[score_data['Game Company'] == 'Blizzard']
print(valve_games.head())