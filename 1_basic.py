# Lets import CSV
import csv

# For graphics
from matplotlib import pyplot as plt

# Wich file we need to read?
filename = 'florida_07_2017.csv'

# Open the file as f
with open(filename) as f:
    # Get up the reader
    reader = csv.reader(f)
    header_row = next(reader)

    # Enumerate will automatically create a number ID for each row
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    print("--------------------------------------")

    # Print temperatures
    temps = []
    for row in reader:
        # convert this to int so we can put it in matplot
        t = float(row[1])
        temps.append(t)

    print(temps)

    # Plot data.
    fig = plt.figure(dpi=128, figsize=(8, 5))

    # What must be ploted, and use a red marker please
    plt.plot(temps, c='red')

    # Format plot.
    plt.title("Daily temperatures from July 2017", fontsize=24)

    # Axis labels
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (C)", fontsize=16)

    # Show a nice, pretty, graphic
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
