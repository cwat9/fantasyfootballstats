from calendar import week
import pandas as pd
import numpy as np
from personal_functions import weekly_case
import csv
from csv import writer
import os

def keep_up_to_date(week, year, cols, cols2):
    filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/reduced-stats.csv".format(year)
    filename2 = "/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year)
    filename4 = "/Users/cw2/Desktop/fantasy football 5/csv/{}/storage.csv".format(year)

    # Check if the 'storage.csv' file exists
    if not os.path.isfile(filename4):
        # Create an empty DataFrame with the desired columns
        empty_df = pd.DataFrame(columns=["Player", "PPR", "storage"])

        # Save the empty DataFrame as 'storage.csv'
        empty_df.to_csv(filename4, index=False)

    df = pd.read_csv(filename, usecols=cols,keep_default_na=False)
    df2 = pd.read_csv(filename2, usecols=cols2, keep_default_na=False)
    df4 = pd.read_csv(filename4, usecols=["Player", "PPR", "storage"])

    id_keys = df["Player"]

    rows = []
    for id in id_keys:
        rows.append([id])
                
    with open("temp.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Player"])
        writer.writerows(rows)

    df3 = pd.read_csv("temp.csv")

    x = pd.merge(df2, df3, on=["Player"], how="right").fillna({'Week {}'.format(week-1): 0.0})
    x.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year), index=False)

    x2 = pd.merge(df4, df3, on=["Player"], how="right").fillna({'PPR': 0.0})
    x2.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/storage.csv".format(year), index=False)

def auto_store(week, year, column1, column2, column3):
    filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/reduced-stats.csv".format(year)
    filename2 = "/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year)
    filename3 = "/Users/cw2/Desktop/fantasy football 5/csv/{}/storage.csv".format(year)

    df = pd.read_csv(filename, usecols=column1,keep_default_na=False)
    df2 = pd.read_csv(filename2, usecols=column2, keep_default_na=False)
    df3 = pd.read_csv(filename3, usecols=column3, keep_default_na=False)
    
    df3["storage"] = df["PPR"]

    df2["Week {}".format(week)] = round(df["PPR"].apply(np.float64) - df3["PPR"].apply(np.float64), 2)

    df3["PPR"] = df["PPR"]
    df3.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/storage.csv".format(year), index=False)

    df2["PPR"] = df["PPR"]
    df2.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year), index=False)

def get_weekly_stats(week, year):
    if (week == 1):
        cols = ["Player", "PPR"]

        filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/reduced-stats.csv".format(year)

        df = pd.read_csv(filename, usecols=cols,keep_default_na=False)

        df["Week 1"] = df["PPR"]

        df.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year), index=False)

    elif (week == 2):
        cols = ["Player", "PPR"]
        cols2 = weekly_case(week)

        filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/reduced-stats.csv".format(year)
        filename2 = "/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year)

        df = pd.read_csv(filename, usecols=cols,keep_default_na=False, na_values="N/A")
        df2 = pd.read_csv(filename2, usecols=cols2)

        # new
        keep_up_to_date(week, year, cols, cols2)

        df2["Week 2"] = round(df["PPR"] - df2["Week 1"].apply(np.float64), 2)
        
        df["storage"] = df["PPR"]
        df.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/storage.csv".format(year), index=False)

        df2["PPR"] = df["PPR"]
        df2.to_csv("/Users/cw2/Desktop/fantasy football 5/csv/{}/weekly-stats.csv".format(year), index=False)

    else:
        cols = ["Player", "PPR"]
        cols2 = weekly_case(week)
        cols3 = ["Player", "PPR", "storage"]

        # new
        keep_up_to_date(week, year, cols, cols2)

        auto_store(week, year, cols, cols2, cols3)
