import unittest
from unittest import TestCase,main
from lesson_16_testing import average_exam_score
from lesson_16_testing import red_or_blue
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

class TestStdGrades(TestCase):

    def test_calculate_average(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', 'mark': 8},
            {'name': 'Zac', 'mark': '8'},
        ]
        expected = 7.25  # (8+8+6+7) / 4

        result = average_exam_score(my_input)
        self.assertEqual(expected, result)

    def test_calculate_average_missing(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', 'mark': 8},
            {'name': 'Zac'}
        ]
        expected = 7.25  # (8+8+6+7) / 4

        result = average_exam_score(my_input)
        self.assertEqual(expected, result)

    def test_calculate_average_invalid_mark(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', 'mark': 8},
            {'name': 'Zac', 'mark': 28},
        ]
        with self.assertRaises(ValueError):
            average_exam_score(my_input)


if __name__ == '__main__':
    main()
