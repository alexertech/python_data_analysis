# Lets import CSV
import csv
from datetime import datetime

# For graphics
from matplotlib import pyplot as plt

# Wich file we need to read?
filename = 'sitka_weather_2014.csv'

# Open the file as f
with open(filename) as f:
    # Get up the reader
    reader = csv.reader(f)
    header_row = next(reader)

    # This plot with be of several values
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        t = int(row[1])
        highs.append(t)

        t = int(row[3])
        lows.append(t)


    # Plot data.
    fig = plt.figure(dpi=128, figsize=(8, 5))

    # What must be ploted

    # Lets do a double graph with the highs and low temps
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')

    # Add a shade between them
    plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)


    # Format plot.
    plt.title("Daily temperatures from 2014", fontsize=24)

    # Axis labels
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)

    # Show the graph
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.show()
