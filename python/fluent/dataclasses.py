"""
ch5 - Data Class Builders - a collection of fields
"""

import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City("Asia", "Tokyo", "JP"),
    City("Asia", "Delhi", "IN"),
    City("North America", "Mexico City", "MX"),
    City("North America", "New York", "US"),
    City("South America", "São Paulo", "BR"),
]


"""
def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)

    return results
"""


def main():
    print(cities)
    # print(match_asian_cities)

    return


if __name__ == "__main__":
    main()
