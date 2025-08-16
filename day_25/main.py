#
# with open("weather_data.csv", mode="r") as report:
#     data = report.readlines()
#     print(data)

import csv
import pandas

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)
