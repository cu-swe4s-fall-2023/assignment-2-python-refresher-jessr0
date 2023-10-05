import unittest
import sys
import os
import my_utils


class TestGetColumn(unittest.TestCase):

    def setUp(self):
        with open('readtest.txt', 'w') as f:
            f.write("col3,col4\n")
            f.write("data3,data4\n")

        with open('permtest.txt', 'w') as f:
            f.write("test\n")
        os.chmod('permtest.txt', 0o000)

    def tearDown(self):
        os.remove('readtest.txt')
        os.chmod('permtest.txt', 0o777)
        os.remove('permtest.txt')

    def test_file_found(self):
        readarray = []
        with open('readtest.txt', 'r') as f:
            for line in f:
                column = line.strip().split(",")
                readarray.append(column)
        self.assertEqual(readarray, [['col3', 'col4'], ['data3', 'data4']])

    def test_file_not_found(self):
        self.assertRaises(
            FileNotFoundError,
            my_utils.get_column
            'notreal.txt',
            "United States of America",
            0,
            3
        )

    def test_no_perm(self):
        self.assertRaises(
            PermissionError,
            my_utils.get_column,
            'permtest.txt',
            "United States of America",
            0,
            3
        )


class TestFilterArray(unittest.TestCase):

    def setUp(self):
        data = [
            ['USA', 78],
            ['Azerbaijan', 94],
            ['Lesotho', 12]
        ]

    def tearDown(self):
        os.remove(data)

    def country_present(self):
        result = filter_array(data, 'Lesotho')
        self.assertEqual(result, [])

    def country_not_present(self):
        result = filter_array(data, 'Russia')
        self.assertEqual(result, [])


class TestArrayMods(unittest.TestCase):

    def setUp(self):

        integers = [1, 2, 3, 4, 5]
        with open('integers.txt', 'w') as f:
            for integer in integers:
                f.write(str(integer) + '\n')
        with open('valuetestbad.txt', 'w') as f:
            f.write("0.1, 0.2, 0.3")

    def tearDown(self):
        os.remove('integers.txt')
        os.remove('valuetestbad.txt')

    def test_right_value(self):
        self.assertTrue

    def test_wrong_value(self):
        self.assertRaises(
            ValueError,
            my_utils.modify_array,
            'valuetestbad.txt'
        )


class TestStatArray(unittest.TestCase):

    def setUp(self):
        self.values = [1, 2, 3, 4, 5]
        self.novalues = []

    def tearDown(self):
        self.values = []
        self.novalues = []

    def test_mean(self):
        self.assertEqual(my_utils.mean_array(self.values), 3)
        self.assertRaises(
            ZeroDivisionError,
            my_utils.mean_array,
            self.novalues
        )

    def test_median(self):
        self.assertEqual(my_utils.median_array(self.values), 3)
        self.assertRaises(ValueError, my_utils.median_array, self.novalues)

    def test_statdev(self):
        self.assertEqual(round(float(my_utils.sd_array(self.values)), 2), 1.41)
        self.assertRaises(ZeroDivisionError, my_utils.sd_array, self.novalues)


if __name__ == "__main__":
    unittest.main()
