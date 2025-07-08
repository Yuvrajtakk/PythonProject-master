with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)
    for name in data:
        stripped_data = name.strip()
