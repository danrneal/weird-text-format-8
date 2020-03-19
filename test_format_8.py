"""Test objects used to test the behavior in part1 of the alpc"""

import unittest
from format_8 import str_to_bin, scramble_bin, bin_to_dec, encode


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


class ScrambleBinTestCase(unittest.TestCase):
    """This class represents the test cases for the scramble_bin function"""

    def test_single_character(self):
        """Test scrambling binary for a single character"""
        scrambled_binary = scramble_bin(
            ['00000000', '00000000', '00000000', '01000001']
        )
        self.assertEqual(
            scrambled_binary,
            ['00000001', '00000000', '00000000', '00000001']
        )

    def test_full_bundle(self):
        """Test scrambling binary for a full 4 characters"""
        scrambled_binary = scramble_bin(
            ['01000100', '01000101', '01010010', '01000110']
        )
        self.assertEqual(
            scrambled_binary,
            ['00001111', '00000010', '00001101', '00110100']
        )

    def test_non_alphanumerics(self):
        """Test scrambling binary for non-alphanumeric characters"""
        scrambled_binary = scramble_bin(
            ['00101001', '01011110', '00111010', '00100000']
        )
        self.assertEqual(
            scrambled_binary,
            ['00000100', '10110110', '11100100', '01101000']
        )


class BinToDecTestCase(unittest.TestCase):
    """This class represents the test cases for the bin_to_dec function"""

    def test_single_character(self):
        """Test conversion to decimal for a single character"""
        decimal = bin_to_dec(['00000001', '00000000', '00000000', '00000001'])
        self.assertEqual(decimal, 16777217)

    def test_full_bundle(self):
        """Test conversion to decimal for a full 4 characters"""
        decimal = bin_to_dec(['00001111', '00000010', '00001101', '00110100'])
        self.assertEqual(decimal, 251792692)

    def test_non_alphanumerics(self):
        """Test conversion from to decimal for non-alphanumeric characters"""
        decimal = bin_to_dec(['00000100', '10110110', '11100100', '01101000'])
        self.assertEqual(decimal, 79094888)


class EncodeTestCase(unittest.TestCase):
    """End to end tests for the encode function"""

    def test_foo(self):
        """End to end test for the string 'foo'"""
        encoded = encode('foo')
        self.assertEqual(encoded, 124807030)

    def test_spacefoo(self):
        """End to end test for the string ' foo'"""
        encoded = encode(' foo')
        self.assertEqual(encoded, 250662636)

    def test_foot(self):
        """End to end test for the string 'foot'"""
        encoded = encode('foot')
        self.assertEqual(encoded, 267939702)

    def test_allcapsbird(self):
        """End to end test for the string 'BIRD'"""
        encoded = encode('BIRD')
        self.assertEqual(encoded, 251930706)

    def test_dotdotdotdot(self):
        """End to end test for the string '....'"""
        encoded = encode('....')
        self.assertEqual(encoded, 15794160)

    def test_carrotcarrotcarrotcarrot(self):
        """End to end test for the string '^^^^'"""
        encoded = encode('^^^^')
        self.assertEqual(encoded, 252706800)

    def test_capwoot(self):
        """End to end test for the string 'Woot'"""
        encoded = encode('Woot')
        self.assertEqual(encoded, 266956663)

    def test_no(self):
        """End to end test for the string 'no'"""
        encoded = encode('no')
        self.assertEqual(encoded, 53490482)


if __name__ == "__main__":
    unittest.main()
