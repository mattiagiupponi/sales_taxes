from utils.helper import sales_round
import unittest


class TestHelper(unittest.TestCase):
    def test_helper_round_up_function(self):
        expected = 7.15
        actual = sales_round(7.14)
        self.assertEqual(expected, actual)

