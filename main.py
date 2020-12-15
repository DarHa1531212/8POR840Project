import pandas as pd
from _datetime import datetime
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Our original data took 19 GB of storage and even more in memory, so we decided to filter it to only keep
# the players that were the best rank, Diamond. We also only kept the main game mode which is BOMB. That reduces our
# data size to 83 MB, which is very acceptable.
# The commented code below is the one used to create our csv file with the filtered data.
'''
path = r'data'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df = df.loc[(df['skillrank'] == 'Diamond') & (df['gamemode'] == 'BOMB')]
    print(df.head())
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)
'''
# df.to_csv(r"C:\Users\vince\Documents\8POR840Project\dataDiamond.csv", index=False)

'''
path = r'data'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df = df.loc[(df['skillrank'] == 'Gold') & (df['gamemode'] == 'BOMB')]
    print(df.head())
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)
'''
# df.to_csv(r"C:\Users\vince\Documents\8POR840Project\dataDiamond.csv", index=False)

df_diamond = pd.read_csv('dataDiamond.csv')
# print(df_diamond.info())
# print(df_diamond.describe())

df_gold = pd.read_csv('dataGold.csv')
# print(df_gold.info())
# print(df_gold.describe())

'''
pairplot_df_diamond = df_diamond.drop(['matchid', 'dateid', 'roundnumber'], axis=1)
sns.pairplot(data=pairplot_df_diamond)
plt.subplots(figsize=(14, 10))
sns.heatmap(pairplot_df_diamond.corr(), annot=True)
plt.tight_layout()
plt.show()
# ATTENTION PREND BEAUCOUP DE RAM ~10GB ET DE TEMPS ~5min
pairplot_df_gold = df_gold.drop(['matchid', 'dateid', 'roundnumber'], axis=1)
sns.pairplot(data=pairplot_df_gold)
plt.subplots(figsize=(14, 10))
sns.heatmap(pairplot_df_gold.corr(), annot=True)
plt.tight_layout()
plt.show()
'''
'''
plt.subplots(figsize=(14,10))
sns.boxplot(x='roundduration', data=df_diamond)
plt.title("Dispersion du temps par manche")
plt.tight_layout()
plt.show()
'''
'''
plt.subplots(figsize=(14,10))
sns.boxplot(x='roundduration', data=df_gold)
plt.title("Dispersion du temps par manche")
plt.tight_layout()
plt.show()
'''
'''
# filtrer les valeurs aberrantes des durations de manches
df_diamond = df_diamond.loc[(df_diamond['roundduration'] < 270)]

df_diamond_SWAT_ASH = df_diamond.loc[(df_diamond['operator'] == 'SWAT-ASH')]

df1 = pd.DataFrame()
df1['usedR4-C'] = df_diamond_SWAT_ASH['primaryweapon'].apply(lambda x: 1 if x == 'R4-C' else 0)
print(df1['usedR4-C'].value_counts())
'''
'''
df_gold = df_gold.loc[(df_gold['roundduration'] < 270)]

df_gold_SWAT_ASH = df_gold.loc[(df_gold['operator'] == 'SWAT-ASH')]

df2 = pd.DataFrame()
df2['usedR4-C'] = df_gold_SWAT_ASH['primaryweapon'].apply(lambda x: 1 if x == 'R4-C' else 0)
print(df2['usedR4-C'].value_counts())
'''

'''
# pourcentage de victoire des d/fendeurs selon la carte pour les joueurs diamonds
df_diamond_defenders = df_diamond.loc[(df_diamond['role'] == 'Defender')]
df_diamond_defenders_win = df_diamond_defenders.loc[(df_diamond['winrole'] == 'Defender')]
df_diamond_defenders = df_diamond_defenders.groupby(df_diamond_defenders['mapname']).count()
df_diamond_defenders_win = df_diamond_defenders_win.groupby(df_diamond_defenders_win['mapname']).count()
df_diamond_defenders_ratio = pd.DataFrame(columns=['defender_win_ratio'])
df_diamond_defenders_ratio['defender_win_ratio'] = df_diamond_defenders_win['winrole'] / df_diamond_defenders['winrole']
print(df_diamond_defenders_ratio)
df_diamond_defenders_ratio = df_diamond_defenders_ratio.sort_values(by='defender_win_ratio', ascending=False)
df_diamond_defenders_ratio.plot(kind='bar')
plt.title('Ratio victoire/défaite des défendeurs de rang Diamond par carte')
plt.tight_layout()
plt.show()
'''
'''
# pourcentage de victoire des d/fendeurs selon la carte pour les joueurs gold
df_gold_defenders = df_gold.loc[(df_gold['role'] == 'Defender')]
df_gold_defenders_win = df_gold_defenders.loc[(df_gold['winrole'] == 'Defender')]
df_gold_defenders = df_gold_defenders.groupby(df_gold_defenders['mapname']).count()
df_gold_defenders_win = df_gold_defenders_win.groupby(df_gold_defenders_win['mapname']).count()
df_gold_defenders_ratio = pd.DataFrame(columns=['defender_win_ratio'])
df_gold_defenders_ratio['defender_win_ratio'] = df_gold_defenders_win['winrole'] / df_gold_defenders['winrole']
print(df_gold_defenders_ratio)
df_gold_defenders_ratio = df_gold_defenders_ratio.sort_values(by='defender_win_ratio', ascending=False)
df_gold_defenders_ratio.plot(kind='bar')
plt.title('Ratio victoire/défaite des défendeurs de rang Gold par carte')
plt.tight_layout()
plt.show()
'''

# test khi2 sur le choix des cartes
df_diamond_gold = pd.concat([df_diamond, df_gold])
df_maps = df_diamond_gold.groupby(df_diamond_gold['mapname']).count()
total_games = df_maps.winrole.sum()

df_maps_array = df_maps['winrole'].to_numpy()
print(df_maps_array)
total_games_array = np.array(
    [int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index))
        , int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index))
        , int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index)),
     int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index))
        , int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index)), int(total_games / len(df_maps.index))
        , int(total_games / len(df_maps.index))])
print(total_games_array)

print(scipy.stats.chisquare(df_maps_array))

print(df_maps)
print(total_games)
