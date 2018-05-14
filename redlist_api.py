import requests

TOKEN = "bc123e331bb7f28f737b916d77cc7fa3c7b776e44fadf60508564a5a8f382e79"
API = "http://apiv3.iucnredlist.org/api/v3/"


def species_by_country(country):
    """
        :param country str country code
    """

    link = _request_link("country/getspecies/{}".format(country))
    return requests.get(link).json()


def _request_link(request):
    return API + "{}?token={}".format(request, TOKEN)


if __name__ == "__main__":
    print(species_by_country("AZ"))
