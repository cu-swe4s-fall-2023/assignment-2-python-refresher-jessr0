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
            my_utils.get_column,
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


class TestStatArray(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(my_utils.stat_array([1, 2, 3, 4, 5], 'mean'), 3)
        with self.assertRaises(ZeroDivisionError):
            my_utils.stat_array([], 'mean')

    def test_median_even(self):
        self.assertEqual(my_utils.stat_array([1, 2, 3, 4], 'median'), 2.5)

    def test_median_odd(self):
        self.assertEqual(my_utils.stat_array([1, 2, 3, 4, 5], 'median'), 3)

    def test_median_empty(self):
        self.assertIsNone: (my_utils.stat_array([]))

    def test_statdev(self):
        self.assertAlmostEqual(
            my_utils.stat_array([1, 2, 3, 4, 5], 'standard deviation'),
            1.41,
            places=2
        )
        self.assertIsNone: (my_utils.stat_array([]))


if __name__ == "__main__":
    unittest.main()
