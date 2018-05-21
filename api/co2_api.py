import pandas as pd
from os.path import join, abspath, pardir

def get_data():
    return pd.read_csv(abspath(join(pardir, "data", "co2.csv")), delimiter=";")


if __name__ == "__main__":
    data = get_data()
    print(data)
