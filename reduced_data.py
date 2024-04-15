import pandas as pd

def reduced_stats(year):
    cols = ["Player","Tm","FantPos","G","GS","FantPt","PPR","DKPt","FDPt","PosRank","OvRank"]

    filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/{}playerstats.csv".format(year, year)

    df = pd.read_csv(filename, usecols=cols,keep_default_na=False)
    df["PPR"] = pd.to_numeric(df["PPR"], errors='coerce').fillna(0)
    x = df.sort_values(by="Player")
    x.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/reduced-stats.csv".format(year), index=False)