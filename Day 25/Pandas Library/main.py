# using pandas for extract and data analysis

import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data)) ## Dataframe
# print(type(data["temp"])) ## Series

#converts the data into a dictionary
# data_dict = data.to_dict()
# print(data_dict)

#converts the data into a list but it can only convert the series into a list such as "temp":

#temp_list = data["temp"].to_list()
# print(temp_list)
#avg_temp = round((sum(temp_list) / len(temp_list)),2)
# print(avg_temp)

#alternative using the series method
avg_temp = data["temp"].mean()
#print(avg_temp)

#gets the max value
max_temp = data["temp"].max()
#print(max_temp)

#gets the data by calling column
# here it is being called via the "condition" key
# print(data["condition"])

# pandas convert the names of the data frame as an attribute by which they can be called
# print(data.condition)

# get the row
# provides the column name retrieve via the name of the row
print(data[data.day == "Monday"])

# Challenge: Pulling data where temp was max
# print(data[data.temp == data["temp"].max()])

#only retrieving some values instead of the whole
monday = data[data.day == "Monday"]
print(monday.condition)

# Challenge: Convert monday's temp to farhenheit.
# Formula : (0°C × 9/5) + 32
# monday_temp = (monday.temp * 9/5) + 32
# print(monday_temp)

#create a data frame from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")