import my_utils
import argparse

"""Creates user-defined arguments and
    executes my_utils functions"""


def get_args():
    parser = argparse.ArgumentParser(
        description="Get information from CSV file")

    parser.add_argument(
        '--file_name', required=True, help='CSV file name')

    parser.add_argument(
        '--country', required=True, help='Name of country in CSV')

    parser.add_argument(
        '--country_column', type=int, required=True,
        help='Column in which countries are reported')

    parser.add_argument(
        '--fires_column', type=int, required=True,
        help='Column in which fires are reported')

    args = parser.parse_args()

    return args


def main():
    args = get_args()

    bigarr = my_utils.get_column(
        args.file_name, args.country,
        args.country_column, args.fires_column)

    smallarr = my_utils.filter_array(
        bigarr, args.country, args.fires_column)

    fires = my_utils.modify_array(smallarr)

    print(fires)


if __name__ == '__main__':
    main()
