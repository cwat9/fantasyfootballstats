import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
import seaborn as sns
from personal_functions import plot_header_case


def plot_bar(week, year, player):
    filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}*/weekly-stats.csv".format(year)
    filename2 = "/Users/cw2/Desktop/fantasy football 5/csv/{}*/plotting-data.csv".format(year)

    df = pd.read_csv(filename, usecols= lambda col: col not in ["PPR"])

    header = plot_header_case(week)

    select = df.loc[df['Player'].str.replace('[^\w\s]','').str.lower().str.contains(player.lower())]
    select = select.iloc[0]

    with open('test.csv', 'w', newline ='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(select)

    df2 = pd.read_csv('test.csv', usecols= lambda col: col not in ["Player"])

    stats = df2.iloc[0]

    data_color = [x for x in stats]

    median = [y for y in stats]
    median.sort()
    true_median = len(median) // 2
    median = (median[true_median] + median[~true_median]) / 2
    print(median)

    avg = sum(data_color) / week
    good = max(stats) - (max(stats) * 0.2)
    print(avg)
    colors = ['lime' if t >= avg else ('gold' if t >= avg - (avg * 0.25) and t < avg else 'r') for t in data_color]
    # was avg + (avg * 0.35) and avg - (avg * 0.25) ^

    row = df2.iloc[0]
    # row.plot(marker='o', color='navy', label='_nolegend_')
    row.plot.bar(width=0.8, figsize = (10,6), color = colors, label='_nolegend_')
    for i, v in enumerate(data_color):
        plt.text(i, v//2, str(v), ha='center')
    plt.axhline(avg, color='purple', label = "average {}".format(round(avg, 4)))
    plt.axhline(median, color='navy', label = "median {}".format(round(median, 4)))
    plt.xlabel("Weeks")
    plt.ylabel("Points Per Game")
    plt.title(player.upper() + " | " + "WEEK {} - YEAR {}".format(week, year))
    plt.legend()
    plt.show()

# plot_bar(week, year, player)

def plot_scatter(week, year, player):
    filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}*/weekly-stats.csv".format(year)
    filename2 = "/Users/cw2/Desktop/fantasy football 5/csv/{}*/plotting-data.csv".format(year)

    df = pd.read_csv(filename, usecols= lambda col: col not in ["PPR"])

    select = df.loc[df['Player'].str.replace('[^\w\s]','').str.lower().str.contains(player.lower())]
    select = select.iloc[0]

    data = []
    header = ["Weeks", "Points"]

    for x in range(week):
        stats = select.iloc[x+1]
        data.append([x+1, stats])

    with open('test.csv', 'w', newline ='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    df3 = pd.read_csv('test.csv')

    weeks = df3["Weeks"]
    points = df3["Points"]

    x_data = []
    y_data = []

    x_data = list(weeks)
    y_data = list(points)

    z = np.polyfit(x_data, y_data, 1)
    p = np.poly1d(z)
    plt.figure(figsize = (10,6))
    plt.plot(x_data, p(x_data), "r--", label="trendline")
    sns.regplot(x=x_data, y=y_data, order = 6, color="orange", label="trendline (poly reg degree 3)")
    
    plt.scatter(x_data, y_data)
    plt.axhline(0, color='purple', label = "zero line")
    plt.xticks(x_data)
    plt.ylim([-10, max(y_data)+10])
    plt.xlabel("Weeks")
    plt.ylabel("Points Per Game")
    plt.title(player.upper() + " | " + "WEEK {} - YEAR {}".format(week, year))
    plt.legend()
    plt.show()

# plot_scatter(week, year, player)

if __name__ == "__main__":
    #aj brown, tom brady, cooper kupp, travis kelce, justin herbert

    week = 18
    year = 2021
    player = "a.j. brown"

    bar = False
    scatter = True

    if bar == True:
        plot_bar(week, year, player)
    if scatter == True:
        plot_scatter(week, year, player)