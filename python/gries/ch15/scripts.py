import unittest

def above_freezing(celsius: float) -> bool:
    """Return True iff temperature celsius degrees is above freezing
    
    >>> above_freezing(5.2)
    True
    >>> above_freezing(-2)
    False
    """

    return celsius > 0

class TestAboveFreezing(unittest.TestCase):
    """Tests for temperature.above_freezing"""

    def test_above_freezing_above(self):
        """Test a temperature that is above freezing."""

        expected = True
        actual = above_freezing(4.2)
        self.assertEqual(expected, actual, "The temperature is above freezing")

    def test_above_freezing_below(self):
        """Test a temperature that is below freezing."""

        expected = False
        actual = above_freezing(-2)
        self.assertEqual(expected, actual, "The temperature is below freezing")

    def test_above_freezing_at_zero(self):
        """Test a temperature that is at the freezing."""

        expected = False
        actual = above_freezing(0)
        self.assertEqual(expected, actual, "The temperature is at the freezing mark")

unittest.main()
    

