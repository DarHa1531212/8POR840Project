import pandas as pd

from Chi2 import Chi2MapChoice
from DatasetFilter import GenerateCSVBySkillrank
from DecisionTree import decisionTreeKFold
from statistics import printStats, dispersionGraph
from occurencesStats import primaryWeaponByOperator, roundEndReason, winrateByPrimaryWeaponChoice, \
    winrateByPrimaryWeaponAndMaps
from winrateByMap import printWinrateByMap

# À NOTER, LE CODE PREND ÉNORMÉMENT DE TEMPS À EXÉCUTER EN ENTIER, ON VOUS CONSEILLE DONC DE SEULEMENT EXÉCUTER BOUT PAR BOUT

# On met les options pour afficher plus de lignes et de colonnes dans la console
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Pour générer les fichiers csv contenant seulement les joueurs Diamond et Gold,
# il n'est pas nécessaire d'exécuter ce code nous l'avons seulement ajouté pour vous montrer comment nous avons filtré les données
'''
GenerateCSVBySkillrank('Diamond')
GenerateCSVBySkillrank('Gold')
'''

# On lit les fichiers csv et on les places dans des dataframes
df_diamond = pd.read_csv('dataDiamond.csv')
df_gold = pd.read_csv('dataGold.csv')

# Impression graph de dispersion de la colonne du temps du ronde
'''
dispersionGraph(df_diamond, 'roundduration')
dispersionGraph(df_gold, 'roundduration')
'''

# filtrer les valeurs aberrantes des durations de manches
df_diamond = df_diamond.loc[(df_diamond['roundduration'] < 270)]
df_gold = df_gold.loc[(df_gold['roundduration'] < 270)]

# On imprime des statistiques sur les données et de matrices de corrélations
'''
printStats(df_diamond)
printStats(df_gold)  # ATTENTION PREND BEAUCOUP DE RAM ~10GB ET DE TEMPS ~5min
'''

# impression des armes les plus utilisées par chaque opérateur
'''
df_diamond_gold = pd.concat([df_diamond, df_gold])
for operator in df_diamond_gold['operator'].unique():
    primaryWeaponByOperator(df_diamond_gold, operator)
'''

# impression du ratio de victoire selon les armes pour les opérateurs
'''
df_diamond_gold = pd.concat([df_diamond, df_gold])
for operator in df_diamond_gold['operator'].unique():
    winrateByPrimaryWeaponChoice(df_diamond_gold, operator)
'''

# impression du ratio de victoire selon la carte et les armes pour les opérateurs
# Va prendre beaucoup de temps à rouler, si vous voulez le tester on vous conseille de
# remplacer la ligne "winrateByPrimaryWeaponAndMaps(df_diamond_gold, operator)" par
# "winrateByPrimaryWeaponAndMaps(df_diamond_gold, "SWAT-ASH")" qui va effectuer l'opération sur seulement
# l'opérateur du nom de Ash.
'''
df_diamond_gold = pd.concat([df_diamond, df_gold], ignore_index=True)
for operator in df_diamond_gold['operator'].unique():
    winrateByPrimaryWeaponAndMaps(df_diamond_gold, operator)
'''

# On imprime les statistiques sur les occurences des raisons de fin de ronde
'''
roundEndReason(df_diamond)
roundEndReason(df_gold)
'''

# impression des ratio victoires de défendeurs pour les différentes cartes
'''
printWinrateByMap(df_diamond)
printWinrateByMap(df_gold)
'''

# test de Khi2 sur le choix des cartes
'''
df_diamond_gold = pd.concat([df_diamond, df_gold])
Chi2MapChoice(df_diamond_gold)
'''

# On exécute tout ce qui a rapport avec le modèle d'arbre de classification
'''
# decisionTreeTrainTest(pd.concat([df_diamond, df_gold]), .3)
# decisionTreeTrainTest(pd.concat([df_diamond, df_gold]), .4)
# decisionTreeTrainTest(pd.concat([df_diamond, df_gold]), .5)
# decisionTreeTrainTest(pd.concat([df_diamond, df_gold]), .6)
# decisionTreeKFold(pd.concat([df_diamond, df_gold]), 5)
# decisionTreeKFold(pd.concat([df_diamond, df_gold]), 10)
'''
