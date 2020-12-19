import pandas as pd
import matplotlib.pyplot as plt


def printWinrateByMap(df):
    df_defenders = df.loc[(df['role'] == 'Defender')]
    df_defenders_win = df_defenders.loc[(df['winrole'] == 'Defender')]
    df_defenders = df_defenders.groupby(df_defenders['mapname']).count()
    df_defenders_win = df_defenders_win.groupby(df_defenders_win['mapname']).count()

    df_defenders_ratio = pd.DataFrame(columns=['defender_win_ratio'])
    df_defenders_ratio['defender_win_ratio'] = df_defenders_win['winrole'] / df_defenders[
        'winrole']
    df_defenders_ratio = df_defenders_ratio.sort_values(by='defender_win_ratio', ascending=False)
    print(df_defenders_ratio)
    df_defenders_ratio.plot(kind='bar')

    skillrank = df['skillrank'].iloc[0]
    plt.title('Ratio victoire/défaite des défendeurs de rang ' + str(skillrank) + ' par carte')
    plt.tight_layout()
    plt.show()
