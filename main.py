import pandas as pd
from _datetime import datetime
import glob
import seaborn as sns
import matplotlib.pyplot as plt

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
plt.show()
'''
'''
# ATTENTION PREND BEAUCOUP DE RAM ~10GB ET DE TEMPS ~5min
pairplot_df_gold = df_gold.drop(['matchid', 'dateid', 'roundnumber'], axis=1)
sns.pairplot(data=pairplot_df_gold)
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

# filtrer les valeurs aberrantes des durations de manches
df_diamond = df_diamond.loc[(df_diamond['roundduration'] < 270)]

df_gold = df_gold.loc[(df_gold['roundduration'] < 270)]

df_diamond_SWAT_ASH = df_diamond.loc[(df_diamond['operator'] == 'SWAT-ASH')]

df_gold_SWAT_ASH = df_gold.loc[(df_gold['operator'] == 'SWAT-ASH')]

df1 = pd.DataFrame()
df1['usedR4-C'] = df_diamond_SWAT_ASH['primaryweapon'].apply(lambda x: 1 if x == 'R4-C' else 0)
print(df1['usedR4-C'].value_counts())

df2 = pd.DataFrame()
df2['usedR4-C'] = df_gold_SWAT_ASH['primaryweapon'].apply(lambda x: 1 if x == 'R4-C' else 0)
print(df2['usedR4-C'].value_counts())

