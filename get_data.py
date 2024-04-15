import urllib.request
import bs4 as bs
import pandas as pd
import os

def player_csv(year):

    newpath = '/Users/cw2/Desktop/fantasy football 5/csv/{}'.format(year)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    url = "https://www.pro-football-reference.com/years/{}/fantasy.htm".format(year)
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')

    headers = [th.getText() for th in soup.findAll('tr')[1].findAll('th')] #Find the second table row tag, find every table header column within it and extract the html text via the get_text method.
    headers = headers[1:] #Do not need the first (0 index) column header
    
    rows = soup.findAll('tr', class_ = lambda table_rows: table_rows != "thead") #Here we grab all rows that are not classed as table header rows - football reference throws in a table header row everyy 30 rows 
    player_stats = [[td.getText() for td in rows[i].findAll('td')] #get the table data cell text from each table data cell
                    for i in range(len(rows))] #for each row
    player_stats = player_stats[2:]

    stats = pd.DataFrame(player_stats, columns = headers)
    
    stats = stats.replace(r'', 'N/A', regex=True)
    stats['Year'] = year
    
    stats.to_csv('csv/{}/{}playerstats.csv'.format(year, year)) #add your desired path to the function
    
    print("Player data for year {} has been created.".format(year))

if __name__ == '__main__':
    player_csv(2021)