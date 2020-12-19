import scipy.stats


def Chi2MapChoice(df):
    df_maps = df.groupby(df['mapname']).count()
    df_maps_array = df_maps['winrole'].to_numpy()
    print(scipy.stats.chisquare(df_maps_array))
