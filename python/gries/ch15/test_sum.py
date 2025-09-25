import unittest
import sums
from sums import running_sum

class TestRunningSum(unittest.TestCase):
    """Tests for sums.running_sum"""

    def test_running_sum_empty(self):
        """Test an empty list"""

        argument = []
        expected = []
        running_sum(argument)
        self.assertEqual(expected, argument, "The list contains one item")

    def test_running_sum_one_item(self):
        """Test a one-item list."""

        argument = [5]
        expected = [5]
        running_sum(argument)
        self.assertEqual(argument, expected)

    def test_running_sum_two_items(self):
        """Test two-item list"""

        argument = [2, 5]
        expected = [2, 7]
        running_sum(argument)
        self.assertEqual(expected, argument, "The list contains two tiems")

    
    def test_running_sum_multi_negative(self):
        """The list of negataive values."""

        argument = [-1, -5, -3, -4]
        expected = [-1, -6, -9, -13]
        running_sum(argument)
        self.assertEqual(expected, argument, "The list contains only negative items")

    def test_running_sum_multi_zeroes(self):
        """The list of zeroes"""

        argument = [0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0]
        running_sum(argument)
        self.assertEqual(expected, argument, "The list contains only zeroes.")

    def test_running_sum_multi_positives(self):
        """The list of zeroes"""

        argument = [4, 2, 3, 6]
        expected = [4, 6, 9, 15]
        running_sum(argument)
        self.assertEqual(expected, argument, "The list contains only positive numbers")

    def test_running_sum_multi_mix(self):
        """The list of zeroes"""

        argument = [4, 0, 2, -5, 0]
        expected = [4, 4, 6, 1, 1]
        running_sum(argument)
        self.assertEqual(expected, argument, "The list contains a mixture of negative values, zeroes, and positive values")

unittest.main()
    