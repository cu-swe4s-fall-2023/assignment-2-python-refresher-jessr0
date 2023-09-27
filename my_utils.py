from enum import Enum
import sys

"""This script returns of list of integers that correspond
    to forest fires attributed to a country of interest."""


class ErrorCode(Enum):
    """Sets error codes for exceptions"""
    NO_FILE = 1001
    NO_PERM = 999
    VALUE = 998


def get_column(file_name, country, country_column, fires_column):
    """get_column converts each column in a
    specified file to a comma-separated array,
    and compiles these into one large array.

    Parameters
    ----------
    file_name: file of interest
    country: country of interest
    country_column: column number in array that contains countries
    fires_column: column number in array that contains forest fires

    Returns
    -------
    array_con
        Array containing comma-seperated values from file

    """
    array_con = []
    try:
        with open(file_name, 'r') as f:
            for line in f:
                columns = line.strip().split(",")
                array_con.append(columns)
    except FileNotFoundError:
        print(
            f"Error Code:{ErrorCode.NO_FILE.value} - Could not find "
            + file_name)
    except PermissionError:
        print(
            f"Error Code:{ErrorCode.NO_PERM.value} - Could not open "
            + file_name)
    finally:
        return array_con


def filter_array(array_con, country, fires_column):
    """Generates new array that only contains values
        in the fires column that correspond to country
        query.

    Parameters
    ----------
    array_con : Non-empty array containing values from specified file
    country : Country of interest
    fires_column : column number in array that contains forest fires

    Returns
    -------
    new_array
        Non-empty array containing values from fires column that
        correspond to country of interest.

    """
    new_array = []
    for i in array_con:
        for j in i:
            if j == country:
                new_array.append(i[fires_column])

    return new_array


def modify_array(new_array):

    """Converts values in new_array to a list of integers."""

# must convert list values to floats first since they are decimals
    try:
        fires_lst = list(new_array)
        fires_lst_float = [float(item) for item in fires_lst]
        fires_lst_int = [int(item) for item in fires_lst_float]
    except ValueError:
        print(
            f"Error Code:{ErrorCode.VALUE.value} List must be numbers")
    finally:
        if 'fires_lst_int' in locals():
            return fires_lst_int
        else:
            sys.exit(1)
