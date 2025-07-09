# with open("weather_data") as file:
#     data = file.readlines()
#     print(data)
#     line = []
#     for name in data:
#         stripped_data = name.strip()
#         line.append(stripped_data)
#
#     print(line)

import csv

with open("weather_data") as data_file:
    data =csv.reader(data_file)
    tempareture = []
    for row in data:
        print(row)
        if row[1] != "temp":
            tempareture.append(int(row[1]))
        print(tempareture)