from country_codes import codes
from redlist_api import species_by_country


class SpeciesStatistics:

    def number_of_endangered_by_country(self):
        """

        :return: dict of country: number_of_species pairs
        """

        data = dict()

        for code in codes.values():
            fetch = species_by_country(code)

            # data for the country does not exist
            if not fetch.get('result'):
                print("No data for", code)
                continue

            data[code] = fetch.get('count')

        return data
