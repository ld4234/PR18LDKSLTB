import pandas as pd
from datetime import datetime

from util import resource_path

GLOBAL_TEMPERATURES_DATASET = "data/temperatures_by_country"

NORMAL_DATE = datetime(year=1900, month=1, day=1)

data = None

def get_data():
    data = pd.read_csv(resource_path(GLOBAL_TEMPERATURES_DATASET))
    data.dt = pd.to_datetime(data.dt)

    return data


def temperatures():
    #kgkagsfkaª
    return get_data()


def average_normal():
    """
    :return: pandas Series with countries as indexes and 'normal' average temperatures as values
    """

    data = get_data()
    subdata = data[data.dt < NORMAL_DATE]

    return subdata.groupby("Country").AverageTemperature.agg("mean")


def average_21_century():
    data = get_data()
    subdata = data[data.dt > datetime(year=2000, month=1, day=1)]

    return subdata.groupby("Country").AverageTemperature.agg("mean")


def temperature_deviation():
    data = abs(average_21_century() - average_normal())
    data.name = "deviation"

    return data


if __name__ == "__main__":
    data = get_data()
    print(data)
