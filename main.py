import pandas as pd
from _datetime import datetime
import glob

import pydotplus as pydotplus
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

from Chi2 import Chi2MapChoice
from DatasetFilter import GenerateCSVBySkillrank
from DecisionTree import decisionTreeTrainTest, decisionTreeKFold
from statistics import printStats, dispersionGraph
from occurencesStats import primaryWeaponByOperator, roundEndReason, winrateByPrimaryWeaponChoice, \
    winrateByPrimaryWeaponAndMaps
from winrateByMap import printWinrateByMap

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Our original data took 19 GB of storage and even more in memory, so we decided to filter it to only keep
# the players that were the best rank, Diamond. We also only kept the main game mode which is BOMB. That reduces our
# data size to 83 MB, which is very acceptable.
# The commented code below is the one used to create our csv file with the filtered data.

# GenerateCSVBySkillrank('Diamond')
# GenerateCSVBySkillrank('Gold')


df_diamond = pd.read_csv('dataDiamond.csv')
df_gold = pd.read_csv('dataGold.csv')

# impression des statistiques sur les données et de matrices de corrélations
# printStats(df_diamond)
# printStats(df_gold) # ATTENTION PREND BEAUCOUP DE RAM ~10GB ET DE TEMPS ~5min

# impression graph de dispersion de la colonne du temps du ronde
# dispersionGraph(df_diamond, 'roundduration')
# dispersionGraph(df_gold, 'roundduration')

# filtrer les valeurs aberrantes des durations de manches
df_diamond = df_diamond.loc[(df_diamond['roundduration'] < 270)]
df_gold = df_gold.loc[(df_gold['roundduration'] < 270)]

# impression du ratio de victoire selon les armes pour les opérateurs
# df_diamond_gold = pd.concat([df_diamond, df_gold])
# for operator in df_diamond_gold['operator'].unique():
#     winrateByPrimaryWeaponChoice(df_diamond_gold, operator)

# impression du ratio de victoire selon la carte et les armes pour les opérateurs
df_diamond_gold = pd.concat([df_diamond, df_gold], ignore_index=True)
# for operator in df_diamond_gold['operator'].unique():
winrateByPrimaryWeaponAndMaps(df_diamond_gold, "SWAT-ASH")

# roundEndReason(df_diamond)
# roundEndReason(df_gold)

# impression des ratio victoires de défendeurs pour les différentes cartes
# printWinrateByMap(df_diamond)
# printWinrateByMap(df_gold)

# test de Khi2 sur le choix des cartes
# df_diamond_gold = pd.concat([df_diamond, df_gold])
# Chi2MapChoice(df_diamond_gold)


# decisionTreeKFold(pd.concat([df_diamond, df_gold]), 10)
