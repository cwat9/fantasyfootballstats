# fantasyfootballstats

A project I have been working on during football off season. The program collects
data from https://www.pro-football-reference.com/ and runs statistical analysis.

## Installation

You will need Python 3.x.x or later. Was written in 3.8.x and tested until 3.10.x, 
but should support any Python 3 version.

To install, clone or download repo. Then in terminal run:
```
pip install -r requirements.txt
```

## Usage

The main.py should have everything needed to run properly. You will need to run this
every Tuesday or Wednesday (noon or later PST) during the season. You will also need
to modify the ```year``` and ```week``` variables to the current.

If you want to see an individual players stats as a plot, you can run the 
```updated_plot_stats.py```. You will need to modify ```year```, ```week```, and ```player```
variables.

There is also a web version: https://fantasyfootball.streamlit.app/