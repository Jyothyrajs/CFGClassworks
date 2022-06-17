import unittest
from unittest import TestCase,main
from Foundation_less_16_testing import red_or_blue

class TestRedOrBlueFun(TestCase):

    def test_odd_number(self):
        expected = 'Red'
        result = red_or_blue(num = 3)
        self.assertEqual(expected,result)

    def test_even_gt_twenty(self):
        expected = 'Blue'
        result = red_or_blue(num=28)
        self.assertEqual(expected, result)

    def test_even_range_6_20(self):
        expected = 'Red'
        result = red_or_blue(num=12)
        self.assertEqual(expected, result)

    def test_even_range_2_5(self):
        expected = 'Blue'
        result = red_or_blue(num=4)
        self.assertEqual(expected,result)

    if __name__ == '__main__':
        main()
