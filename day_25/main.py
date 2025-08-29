
# with open("weather_data.csv", mode="r") as report:
#     data = report.readlines()
#     print(data)

import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)



def celcius_to_fahrenheit(celcius):
    return celcius * 1.8 + 32

print(celcius_to_fahrenheit(100))
# #
#
# data = pandas.read_csv("weather_data.csv")
# #print(data)
# # series datatype
# print(type(data["temp"]))
# # type is dataframe
# # print(type(data))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# # temp_list = data["temp"].to_list()
# # print(temp_list)
#
# avg_temp = data["temp"].mean()
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# # get data by column
# data["conditions"]
# data.conditions

#get data by row
# print(data[data.day == "Monday"])
# # pulling out the row where the temperature was at a maximum
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp[0])
# print(celcius_to_fahrenheit(monday.temp[0]))

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# create a new csv from the dataframe
# data.to_csv("new_data.csv", index=False)

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrels, black_squirrels, red_squirrels)

# lookup how to save a new file using pandas
data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels, black_squirrels, red_squirrels]
}
# creating new dataFrame and csv file using pandas
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')