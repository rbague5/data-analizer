# Importing libraries
import pandas as pd
import numpy as np


def read():
    # Read csv file into a pandas dataframe
    df = pd.read_csv("Mall_Customers.csv")

    return df


def check_data(csv):

    if not (csv.isnull().values.any()):
        print("|-----------------|")
        print("|  Data is clean  |")
        print("|-----------------|")

    else:
        print("Need to check this data:")
        print(csv.isnull().sum())
        total_values_missing = csv.isnull().sum().sum()
        print("Total values to check: "+str(total_values_missing))


def list_of_headers(csv):
    return csv.columns.values.tolist()


def first_filter_of_data(csv):
    first_data_types = csv.dtypes.tolist()

    return first_data_types


def second_filter_of_data(csv):
    second_data_types = csv.dtypes.tolist()

    return second_data_types


def print_data(headers, filter):
    for x, y in zip(headers, filter):
        # print("Header:    " + x + "      has value type:    " + str(y))
        print('Header: {:<30s} has value type:{:^10s}'.format(str(x), str(y)))


if __name__ == "__main__":
    csv = read()
    check_data(csv)

    # Take a look at the first few rows
    # print(csv.head())
    # print(" ")

    headers = list_of_headers(csv)
    print("")
    print("Hearders of the dataset: "+str(headers))
    # print(type(headers))

    first_filter = first_filter_of_data(csv)
    print("")
    print("Here we have the first filter of data:")
    print_data(headers, first_filter)

    second_filter = second_filter_of_data(csv)
    print("")
    print("Here we have the first filter of data:")
    print_data(headers, second_filter)

    print(" ")
    # print(csv['Genres'])


