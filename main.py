# Importing libraries
import pandas as pd
import numpy as np


def read():
    # Read csv file into a pandas dataframe
    df = pd.read_csv("Mall_Customers.csv")

    return df


def check_missing_data(csv):

    # Checking is has any missing values
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

    # listing all data types from pandas library
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
    check_missing_data(csv)

    # Take a look at the first few rows
    # print(csv.head())
    # print(" ")

    list_of_headers = list_of_headers(csv)  # list of all headers
    print("")
    print("Hearders of the dataset: "+str(list_of_headers))

    first_filter = first_filter_of_data(csv)  # list of types of data

    # first data types cleaned in format
    first_data_types = []
    for type_data in first_filter:
        first_data_types.append(str(type_data))
        #print(type_data,type(type_data))
    #print(type(first_data_types[0]))


    print("")
    print("Here we have the first filter of data:")
    print_data(list_of_headers, first_data_types)

    print("First filter list: ", first_data_types)

    """
    second_filter = second_filter_of_data(csv)
    print("")
    print("Here we have the second filter of data:")
    print_data(list_of_headers, second_filter)
    """


    print(" ")
    # print(csv['Genres'])


