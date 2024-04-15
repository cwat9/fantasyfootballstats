# /Users/cw2/Desktop/sleeper fantasy scripts/players_filtered.csv

import csv

# def filter_rankings(year):
#     filename = "/Users/cw2/Desktop/fantasy football 5/csv/{}/consistency-stats.csv".format(year)
#     filename2 = "/Users/cw2/Desktop/sleeper fantasy scripts/players_filtered.csv"

#     with open(filename2, "r") as f:
#         # Create a CSV reader
#         csv_reader = csv.reader(f)

#         # Skip the header row
#         next(csv_reader)

#         # Extract and print the list of players
#         players = [row[0] for row in csv_reader]
#         print(players)

# filter_rankings(2023)

import csv

def filter_rankings(year):
    # Read players from CSV 2 into a set for efficient membership testing
    players_to_keep = set()
    with open('/Users/cw2/Desktop/sleeper fantasy scripts/players_filtered.csv', mode='r') as csv2_file:
        csv2_reader = csv.reader(csv2_file)
        next(csv2_reader)  # Skip the header row
        for row in csv2_reader:
            player = row[0]
            players_to_keep.add(player)

    # Create a new CSV file to store the filtered data
    with open('filtered_data.csv', mode='w', newline='') as filtered_file:
        fieldnames = ['Player', 'Consistency', 'Average', 'Median', 'Team', 'Position', 'Games Played']
        writer = csv.DictWriter(filtered_file, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()

        # Read and filter data from CSV 1
        with open('/Users/cw2/Desktop/fantasy football 5/csv/{}/consistency-stats.csv'.format(year), mode='r') as csv1_file:
            csv1_reader = csv.DictReader(csv1_file)
            for row in csv1_reader:
                player = row['Player']
                if player in players_to_keep:
                    writer.writerow(row)

    print("Filtered data saved to 'filtered_data.csv'")

filter_rankings(2023)