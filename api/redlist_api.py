from cache import JsonSerializer
import requests
from constants import country_codes

TOKEN = "bc123e331bb7f28f737b916d77cc7fa3c7b776e44fadf60508564a5a8f382e79"
API = "http://apiv3.iucnredlist.org/api/v3/"


def species_by_country(country, can_be_cached=True):
    """
        :param can_be_cached:
        :param country str country code
    """
    if can_be_cached:
        if JsonSerializer.cached(country):
            return JsonSerializer.country_data(country)

    link = _request_link("country/getspecies/{}".format(country))
    data = requests.get(link).json()
    if can_be_cached:
        JsonSerializer.persist_country_data(country, data)
    return data


def _request_link(request):
    return API + "{}?token={}".format(request, TOKEN)


all_country_codes = country_codes.codes.values()

if __name__ == "__main__":
    print(species_by_country("AZ"))
