import math
import pandas as pd
import numpy as np
from personal_functions import math_cols_case, math_list_case

def median(year):
    filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year)
    df = pd.read_csv(filename, usecols= lambda col: col not in ["Player", "PPR", "G", "FantPos", "Tm"])
    
    group = []

    for i in range(len(df)):
        stats = df.iloc[i]

        median = [y for y in stats]
        median.sort()
        true_median = len(median) // 2
        median = (median[true_median] + median[~true_median]) / 2
        group.append(round(median,4))
        
    return (group)

def standard_deviation(week, year, data, df):
    filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year)
    filename2 = "/Users/cw2/Desktop/fantasy football 5/csv/{}/reduced-stats.csv".format(year)
    df2 = pd.read_csv(filename, usecols= lambda col: col not in ["Player", "PPR"])
    df3 = pd.read_csv(filename2)

    sig_games = week - df3["G"]

    mean = sum(data) / df3["G"]
    bonus = sig_games*(mean)**2
    list = [(x-mean)**2 for x in data]
    variance = (sum(list)-bonus) / df3["G"]
    sd = np.sqrt(abs(variance))

    cv = sd / mean

    df["Consistency"] = round(abs(cv), 4)
    df["Average"] = round(mean, 4)
    df["Median"] = median(year)
    df["Team"] = df3["Tm"]
    df["Position"] = df3["FantPos"]
    df["Games Played"] = df3["G"]
    df["Value"] = (df['Average'] * 0.75) + ((1 - df['Consistency']) * 0.25)
    # "G", "FantPos", "Tm",

    df.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/consistency-stats.csv".format(year), index=False)

def calculate(week, year):

    filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year)

    cols2 = ["Player"]
    cols = math_cols_case(week)

    df2 = pd.read_csv(filename, usecols=cols2,keep_default_na=False)

    list = math_list_case(week, filename, cols)

    standard_deviation(week, year, list, df2)

def fix(year):
    filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year)
    filename2 = "/Users/cw2/Desktop/fantasy football 5/csv/{}/storage.csv".format(year)
    df = pd.read_csv(filename, usecols= lambda col: col not in ["Player", "PPR"])
    df2 = pd.read_csv(filename2)

    addi = df["Week 1"] + df["Week 2"]

    # df2["Player"] = df["Player"]
    # df2["PPR"] = df["PPR"]
    df2["storage"] = addi

    df2.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/storage.csv".format(year), index=False)

# fix(2022)

# l = [4,3,5,2,1,0,0]
# m = [y for y in l]
# m.sort()

# s=0
# for i in range(len(m)):
#     if m[i]==0:
#      s+=1
# print(s)

# if week > game_started:
#     to_remove = week - game_started

# for x in range(to_remove):
#     m.remove(0.0)

# print(m)
