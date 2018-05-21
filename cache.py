import json
from os.path import exists


class JsonSerializer:

    @staticmethod
    def country_data(country):
        """
        :param country: country code
        :return: json data of the country if cached, otherwise None
        """

        if JsonSerializer.cached(country):
            path = "./data/cache/{}.json".format(country)
            with open(path, 'r') as file:
                return json.load(file)
        return None

    @staticmethod
    def persist_country_data(country, data):
        path = "./data/cache/{}.json".format(country)
        with open(path, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def cached(country):
        """
        :param country:
        :return: True if data for country is cached, otherwise False
        """

        path = "./data/cache/{}.json".format(country)
        return exists(path)


if __name__ == "__main__":
    from constants.country_codes import codes
    from api import redlist_api
    for code in codes.values():
        if not JsonSerializer.cached(code):
            data = redlist_api.species_by_country(code)
            if data["count"] != len(data["result"]):   # testing to see if we need to implement pagination
                print(data)
            JsonSerializer.persist_country_data(code, data)
