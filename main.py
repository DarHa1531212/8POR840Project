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
# df.to_csv(r"C:\Users\vince\Documents\8POR840Project\data.csv", index=False)

df = pd.read_csv('data.csv')
print(df.info())
print(df.describe())
'''
pairplot_df = df.drop(['matchid', 'dateid', 'roundnumber'], axis=1)
sns.pairplot(data=pairplot_df)
plt.show()
'''
'''
plt.subplots(figsize=(14,10))
sns.boxplot(x='roundduration', data=df)
plt.title("Dispersion du temps par manche")
plt.tight_layout()
plt.show()
'''
'''
plt.subplots(figsize=(14,10))
sns.boxplot(x='nbkills', data=df)
plt.title("Dispersion du nombre de kills par manche")
plt.tight_layout()
plt.show()
'''

# filtrer les valeurs aberrantes des durations de manches
df = df.loc[(df['roundduration'] < 270)]

