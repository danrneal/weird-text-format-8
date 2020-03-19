"""Test objects used to test the behavior in part1 of the alpc"""

import unittest
from format_8 import str_to_bin


class StrToBinTestCase(unittest.TestCase):
    """This class represents the test cases for the str_to_bin function"""

    def test_single_character(self):
        """Test conversion to binary for a single character"""
        binary = str_to_bin('A')
        self.assertEqual(
            binary,
            ['00000000', '00000000', '00000000', '01000001']
        )

    def test_full_bundle(self):
        """Test conversion to binary for a full 4 characters"""
        binary = str_to_bin('FRED')
        self.assertEqual(
            binary,
            ['01000100', '01000101', '01010010', '01000110']
        )

    def test_non_alphanumerics(self):
        """Test conversion to binary for non-alphanumeric characters"""
        binary = str_to_bin(' :^)')
        self.assertEqual(
            binary,
            ['00101001', '01011110', '00111010', '00100000']
        )


if __name__ == "__main__":
    unittest.main()
