import glob
import pandas as pd

# Les fichiers CSV originaux(20GB) doivent être dans le répertoire pour que cette fonction fonctionne
def GenerateCSVBySkillrank(skillrank):
    path = r'data'
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        df = df.loc[(df['skillrank'] == skillrank) & (df['gamemode'] == 'BOMB')]
        print(df.head())
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    df.to_csv(r"C:\Users\vince\Documents\8POR840Project\dataDiamond.csv", index=False)
