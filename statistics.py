import seaborn as sns
import matplotlib.pyplot as plt


def printStats(df):
    print(df.info())
    print(df.describe())

    pairplot_df_diamond = df.drop(['matchid', 'dateid', 'roundnumber'], axis=1)
    sns.pairplot(data=pairplot_df_diamond)
    plt.subplots(figsize=(14, 10))
    sns.heatmap(pairplot_df_diamond.corr(), annot=True)
    plt.tight_layout()
    plt.show()

def dispersionGraph(df, columnName):
    plt.subplots(figsize=(14, 10))
    sns.boxplot(x=columnName, data=df)
    plt.title("Dispersion de la variable " + columnName)
    plt.tight_layout()
    plt.show()
