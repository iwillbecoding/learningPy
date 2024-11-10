import csv

with open("weather_data.csv") as data_file:
    info = csv.reader(data_file)
    for row in info:
        print(row[1])
