import pandas as pd
import matplotlib.pyplot as plt


def primaryWeaponByOperator(df, operatorName):
    df_operator = df.loc[(df['operator'] == operatorName)]
    print("Nombre d'occurence d'armes par opérateur " + operatorName + ": \n" + str(
        df_operator['primaryweapon'].value_counts()))


def winrateByPrimaryWeaponChoice(df, operatorName):
    df_operator = df.loc[(df['operator'] == operatorName)]

    weapon_occurences = df_operator['primaryweapon'].value_counts()

    df_operator_haswon = df_operator.loc[(df_operator['haswon'] == 1)]
    df_operator_haswon = df_operator_haswon.groupby(by=["primaryweapon"]).count()
    weapon_occurences_haswon = pd.Series(data=df_operator_haswon['dateid'], index=df_operator_haswon.index)

    weapon_haswon_ratio = weapon_occurences_haswon.div(weapon_occurences).sort_values(ascending=False)

    weapon_haswon_ratio.plot(kind='bar', ylim=[0.45, 0.55])
    plt.title("ratio victoire/défaite par arme pour l'opérateur " + operatorName)
    plt.tight_layout()
    plt.show()

    print("ratio victoire/défaite par arme pour l'opérateur " + operatorName + ": \n" + str(
        weapon_haswon_ratio))

def winrateByPrimaryWeaponAndMaps(df, operatorName):
    df_operator = df.loc[(df['operator'] == operatorName)]
    for mapname in df['mapname'].unique():
        #print(df_operator[df_operator.index.duplicated()])
        df_iteration_map = df_operator.loc[(df['mapname'] == mapname)]
        weapon_occurences = df_iteration_map['primaryweapon'].value_counts()

        df_iteration_map_haswon = df_iteration_map.loc[(df_iteration_map['haswon'] == 1)]
        df_iteration_map_haswon = df_iteration_map_haswon.groupby(by=["primaryweapon"]).count()
        weapon_occurences_haswon = pd.Series(data=df_iteration_map_haswon['dateid'], index=df_iteration_map_haswon.index)

        weapon_haswon_ratio = weapon_occurences_haswon.div(weapon_occurences).sort_values(ascending=False)

        weapon_haswon_ratio.plot(kind='bar', ylim=[0.43, 0.6])
        plt.title("ratio victoire/défaite par arme pour l'opérateur " + operatorName + " et la carte " + mapname)
        plt.tight_layout()
        plt.show()

        print("ratio victoire/défaite par arme pour l'opérateur " + operatorName + " et la carte " + mapname + ": \n" + str(
            weapon_haswon_ratio))



def roundEndReason(df):
    print(df['endroundreason'].value_counts())
