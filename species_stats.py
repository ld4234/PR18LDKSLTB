from constants.country_codes import codes
from api.redlist_api import species_by_country
from cache import JsonSerializer


class SpeciesStatistics:

    def number_of_endangered_by_country(self):
        """

        :return: dict of country: number_of_species pairs
        """

        data = dict()

        for code in codes.values():
            if JsonSerializer.cached(code):
                fetch = JsonSerializer.country_data(code)  # fast local cache
            else:
                fetch = species_by_country(code)  # slow API fetch

            # data for the country does not exist
            if not fetch.get('result'):
                print("No data for", code)
                continue

            if not JsonSerializer.cached(code):
                JsonSerializer.persist_country_data(code, fetch)
            data[code] = fetch.get('count')

        return data
