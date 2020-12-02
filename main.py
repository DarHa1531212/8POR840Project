import pandas as pd
from _datetime import datetime
import glob

before = datetime.now()

path = r'data' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    df = df.loc[(df['skillrank'] == 'Diamond') & (df['gamemode'] == 'BOMB')]
    print(df.head())
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

after = datetime.now()

print(df.info())

# TODO: write dataframe in csv file

print(after - before)
