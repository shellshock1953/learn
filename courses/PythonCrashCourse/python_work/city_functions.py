def city_country(city, country, population=None):
    formated_city = f"{city}, {country}".title()
    if population:
        return f"{formated_city} - population {population}"
    else:
        return formated_city

print(city_country('Lviv', 'Ukraine', 1_200_00))

