from get_data import player_csv
from math_data import calculate
from reduced_data import reduced_stats
from weekly_stats import get_weekly_stats

week = 15
year = 2023

if __name__ == "__main__":
    player_csv(year) #gets data from website
    reduced_stats(year) #removes certain columns of data
    get_weekly_stats(week, year) #calculates and adds the weekly data
    calculate(week, year) #calculates statistical data
    print("Finished Week " + str(week))

    # x=1
    # while x in range(19):
    #     reduced_stats(year) #removes certain columns of data
    #     get_weekly_stats(x, year) #calculates and adds the weekly data
    #     calculate(x, year) #calculates statistical data
    #     x= x+1

    # 2021 completed stats:
    # tom brady, cooper kupp, justin herbert, justin jefferson, travis kelce
    # aj brown, dandre swift, saquon barkley, darren waller, 
    # josh allen, jonathan taylor, russell wilson, christian mccaffrey, 
    # alvin kamara, jamarr chase, deebo samuel, joe burrow, 
    # davante adams, derrick henry, mark andrews, aaron rodgers

    # patrick mahomes, austin ekeler, stefon diggs, george kittle
    