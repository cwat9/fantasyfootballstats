import pandas as pd
import numpy as np

def weekly_case(week):
    switch = {
        # ["Player", "PPR", "G", "FantPos", "Tm"]
        1:["Player", "PPR", ],
        2:["Player", "PPR",  "Week 1"],
        3:["Player", "PPR",  "Week 1", "Week 2"],
        4:["Player", "PPR",  "Week 1", "Week 2", "Week 3"],
        5:["Player", "PPR",  "Week 1", "Week 2", "Week 3", "Week 4"],
        6:["Player", "PPR",  "Week 1", "Week 2", "Week 3", "Week 4", "Week 5"],
        7:["Player", "PPR",  "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"],
        8:["Player", "PPR",  "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7"],
        9:["Player", "PPR",  "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8"], 
        10:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9"],
        11:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10"],
        12:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11"],
        13:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12"], 
        14:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13"],
        15:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14"],
        16:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15"],
        17:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15", "Week 16"], 
        18:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15", "Week 16", "Week 17"],
    }
    return switch.get(week, "Invalid Input")

def math_cols_case(week):
    switch = {
        1:["Player", "PPR", "Week 1"],
        2:["Player", "PPR", "Week 1", "Week 2"],
        3:["Player", "PPR", "Week 1", "Week 2", "Week 3"],
        4:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4"],
        5:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5"],
        6:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"],
        7:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7"],
        8:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8"], 
        9:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9"],
        10:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10"],
        11:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11"],
        12:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12"], 
        13:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13"],
        14:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14"],
        15:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15"],
        16:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15", "Week 16"], 
        17:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15", "Week 16", "Week 17"],
        18:["Player", "PPR", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15", "Week 16", "Week 17", "Week 18"],
    }
    return switch.get(week, "Invalid Input")

def math_list_case(week, filename, cols):
    df = pd.read_csv(filename, usecols=cols)
    df.replace(np.nan, 0.0)
    df.to_csv(filename, index=False)

    if (week == 1):
        return [df["Week 1"]]
    elif (week == 2):
        return [df["Week 1"], df["Week 2"]]
    elif (week == 3):
        return [df["Week 1"], df["Week 2"], df["Week 3"]]
    elif (week == 4):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"]]
    elif (week == 5):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"]]
    elif (week == 6):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"]]
    elif (week == 7):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"]]
    elif (week == 8):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"]]
    elif (week == 9):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"]]
    elif (week == 10):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"], df["Week 10"]]
    elif (week == 11):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"], df["Week 10"], df["Week 11"]]
    elif (week == 12):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"], df["Week 10"], df["Week 11"], df["Week 12"]]
    elif (week == 13):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"], df["Week 10"], df["Week 11"], df["Week 12"], df["Week 13"]]
    elif (week == 14):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"], df["Week 10"], df["Week 11"], df["Week 12"], df["Week 13"], df["Week 14"]]
    elif (week == 15):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"], df["Week 10"], df["Week 11"], df["Week 12"], df["Week 13"], df["Week 14"], df["Week 15"]]
    elif (week == 16):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"], df["Week 10"], df["Week 11"], df["Week 12"], df["Week 13"], df["Week 14"], df["Week 15"], df["Week 16"]]
    elif (week == 17):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"], df["Week 10"], df["Week 11"], df["Week 12"], df["Week 13"], df["Week 14"], df["Week 15"], df["Week 16"], df["Week 17"]]
    elif (week == 18):
        return [df["Week 1"], df["Week 2"], df["Week 3"], df["Week 4"], df["Week 5"], df["Week 6"], df["Week 7"], df["Week 8"], df["Week 9"], df["Week 10"], df["Week 11"], df["Week 12"], df["Week 13"], df["Week 14"], df["Week 15"], df["Week 16"], df["Week 17"], df["Week 18"]]

def plot_header_case(week):
    switch = {
        1:["Player", "Week 1"],
        2:["Player", "Week 1", "Week 2"],
        3:["Player", "Week 1", "Week 2", "Week 3"],
        4:["Player", "Week 1", "Week 2", "Week 3", "Week 4"],
        5:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5"],
        6:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"],
        7:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7"],
        8:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8"], 
        9:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9"],
        10:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10"],
        11:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11"],
        12:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12"], 
        13:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13"],
        14:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14"],
        15:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15"],
        16:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15", "Week 16"], 
        17:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15", "Week 16", "Week 17"],
        18:["Player", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13", "Week 14", "Week 15", "Week 16", "Week 17", "Week 18"],
    }
    return switch.get(week, "Invalid Input")