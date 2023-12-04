import json

countries = [
    {"Україна": {"населення": 44.03, "площа": 603.5}},
    {"Португалія": {"населення": 10.4, "площа": 92.3}},
    {"Китай": {"населення": 125.78, "площа": 377.9}},
    {"США": {"населення": 328.2, "площа": 9831.7}},
    {"Японія": {"населення": 1380.00, "площа": 3287}},
    {"Бразилія": {"населення": 210.14, "площа": 8515}},
    {"Франція": {"населення": 67.34, "площа": 551.7}},
    {"Німеччина": {"населення": 83.02, "площа": 357.5}},
    {"Канада": {"населення": 37.59, "площа": 9984}},
    {"Австралія": {"населення": 25.41, "площа": 2968.7}}
]

jsonData = json.dumps(countries)

with open("data.json", "wt") as file:
    file.write(jsonData)

while True:
    print(
        "Select an option:\n 1 - Add data\n 2 - View data\n 3 - Find the country with the maximum population density\n 4 - Exit")
    x = input("Choose an option:\n")
    x = int(x)

    if x == 1:
        with open("data.json", "wt") as file:
            countries = json.loads(jsonData)

            def add_country(data):
                country_name = input("Enter the country name: ")
                population = float(input("Enter the population (in millions): "))
                area = float(input("Enter the area (in thousands of square km): "))

                for country_dict in data:
                    if country_name in country_dict:
                        print(f"{country_name} already exists in the list.")
                        ans = input("If you want to update the information, press 1, otherwise press any other key: ")
                        if ans == "1":
                            data.append({country_name: {"населення": population, "площа": area}})
                            print(f"Information for {country_name} has been updated.")
                        return data

                data.append({country_name: {"населення": population, "площа": area}})
                print(f"Country {country_name} has been added to the list.")
                return data
            countries = add_country(countries)
            jsonData = json.dumps(countries)
            file.write(jsonData)
            file.close()

    if x == 2:
        with open("data.json", "rt") as file:
            countries = json.loads(jsonData)
            print(*countries, sep='\n')
    if x == 3:
        with open("data.json", "rt") as file:
            countries = json.loads(jsonData)
            def find_max_density_country(data):
                max_density_country = max(data, key=lambda x: x[list(x.keys())[0]]["населення"] / x[list(x.keys())[0]][
                    "площа"])
                return list(max_density_country.keys())[0]
            max_density_country_name = find_max_density_country(countries)
            print(f'The country with the maximum population density is: {max_density_country_name}')
    if x == 4:
        quit(0)