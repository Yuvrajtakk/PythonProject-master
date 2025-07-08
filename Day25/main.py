with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)
    line = []
    for name in data:
        stripped_data = name.strip()
        line.append(stripped_data)

    print(line)