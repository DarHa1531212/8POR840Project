import pandas as pd
from _datetime import datetime
import glob

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
