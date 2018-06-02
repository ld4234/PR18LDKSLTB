import pandas as pd
from util import resource_path


def get_data():
    """

    :return: DataFrame(kyear, co2, sigma_mean)
    """
    data = pd.read_csv(resource_path("data/co2.csv"), delimiter=";")
    data.yearBP = data.yearBP * -1
    data.yearBP = data.yearBP - data.yearBP.max()
    data['kyear'] = data.yearBP / 1000
    del data['yearBP']

    data = data[data.kyear > - 380]

    return data

if __name__ == "__main__":
    data = get_data()
    print(data)
