from unittest import removeResult

import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add_1(self):
        data.Time.time1 = (3,25,45)
        data.Time.time2 = (1,5,20)
        expected = data.Time(4,31,5)
        result = lab5.time_add((3,25,45),(1,5,20))
        self.assertEqual(expected,result)

    def test_time_add_2(self):
        data.Time.time1 = (2,25,45)
        data.Time.time2 = (3,1,10)
        expected = (5,26,55)
        result = lab5.time_add((2,25,45),(3,1,10))
        self.assertEqual(expected,result)

    # Part 4

    def test_is_descending_1(self):
        list1 = [5.0,6.0,7.0]
        expected = False
        result = lab5.is_descending(list1)
        self.assertEqual(expected,result)

    def test_is_descending_2(self):
        list1 = [7.5,7.4,7.3]
        expected = True
        result = lab5.is_descending(list1)
        self.assertEqual(expected,result)

    # Part 5

    def test_largest_between_1(self):
        list1 = [5,4,7,6,8]
        lower = 0
        upper = 3
        expected = 2
        result = lab5.largest_between(list1)
        self.assertEqual(expected,result)

    def test_largest_between_2(self):
        list1 = [5,4,7,6,8]
        lower = 0
        upper = 4
        expected = 4
        result = lab5.largest_between(list1)
        self.assertEqual(expected,result)

    # Part 6

    def test_furthest_from_origin_1(self):
        list1 = [data.Point(5.0,6.0),data.Point(4.0,3.0), data.Point(10.0,20.0)]
        expected = 2
        result = lab5.furthest_from_origin(list1)
        self.assertEqual(expected,result)

    def test_furthest_from_origin_2(self):
        list1 = [data.Point(10.0,20.0),data.Point(4.0,3.0), data.Point(5.0,6.0)]
        expected = 0
        result = lab5.furthest_from_origin(list1)
        self.assertEqual(expected,result)


if __name__ == '__main__':
    unittest.main()
