import pandas as pd
from util import resource_path


def get_data():
    return pd.read_csv(resource_path("data/co2.csv"), delimiter=";")


if __name__ == "__main__":
    pass
