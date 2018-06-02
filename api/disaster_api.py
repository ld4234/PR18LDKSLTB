import pandas as pd
from util import resource_path


def get_data():
    """

    :return: DataFrame(kyear, co2, sigma_mean)
    """
    data = pd.read_csv(resource_path("data/disaster_continent.csv"), delimiter=",")

    return data

if __name__ == "__main__":
    data = get_data()
    print(data)
