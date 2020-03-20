"""Test objects used to test the behavior in part1 of the alpc"""

import unittest
from WeirdTextFormat8 import (
    str_to_bin, bin_to_str, scramble_bin, unscramble_bin, bin_to_dec,
    dec_to_bin, encode, decode
)


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


class BinToStrTestCase(unittest.TestCase):
    """This class represents the test cases for the bin_to_str function"""

    def test_single_character(self):
        """Test conversion from binary for a single character"""
        string = bin_to_str(['00000000', '00000000', '00000000', '01000001'])
        self.assertEqual(string, 'A')

    def test_full_bundle(self):
        """Test conversion from binary for a full 4 characters"""
        string = bin_to_str(['01000100', '01000101', '01010010', '01000110'])
        self.assertEqual(string, 'FRED')

    def test_non_alphanumerics(self):
        """Test conversion from binary for non-alphanumeric characters"""
        string = bin_to_str(['00101001', '01011110', '00111010', '00100000'])
        self.assertEqual(string, ' :^)')


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


class UncrambleBinTestCase(unittest.TestCase):
    """This class represents the test cases for the unscramble_bin function"""

    def test_single_character(self):
        """Test unscrambling binary for a single character"""
        unscrambled_binary = unscramble_bin(
            ['00000001', '00000000', '00000000', '00000001']
        )
        self.assertEqual(
            unscrambled_binary,
            ['00000000', '00000000', '00000000', '01000001']
        )

    def test_full_bundle(self):
        """Test unscrambling binary for a full 4 characters"""
        unscrambled_binary = unscramble_bin(
            ['00001111', '00000010', '00001101', '00110100']
        )
        self.assertEqual(
            unscrambled_binary,
            ['01000100', '01000101', '01010010', '01000110']
        )

    def test_non_alphanumerics(self):
        """Test unscrambling binary for non-alphanumeric characters"""
        unscrambled_binary = unscramble_bin(
            ['00000100', '10110110', '11100100', '01101000']
        )
        self.assertEqual(
            unscrambled_binary,
            ['00101001', '01011110', '00111010', '00100000']
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


class DecToBinTestCase(unittest.TestCase):
    """This class represents the test cases for the dec_to_bin function"""

    def test_single_character(self):
        """Test conversion from decimal for a single character"""
        binary = dec_to_bin(16777217)
        self.assertEqual(
            binary,
            ['00000001', '00000000', '00000000', '00000001']
        )

    def test_full_bundle(self):
        """Test conversion to decimal for a full 4 characters"""
        binary = dec_to_bin(251792692)
        self.assertEqual(
            binary,
            ['00001111', '00000010', '00001101', '00110100']
        )

    def test_non_alphanumerics(self):
        """Test conversion from to decimal for non-alphanumeric characters"""
        binary = dec_to_bin(79094888)
        self.assertEqual(
            binary,
            ['00000100', '10110110', '11100100', '01101000']
        )


class EncodeTestCase(unittest.TestCase):
    """End to end tests for the encode function"""

    def test_foo(self):
        """End to end test for the string 'foo'"""
        encoded = encode('foo')
        self.assertEqual(encoded, [124807030])

    def test_spacefoo(self):
        """End to end test for the string ' foo'"""
        encoded = encode(' foo')
        self.assertEqual(encoded, [250662636])

    def test_foot(self):
        """End to end test for the string 'foot'"""
        encoded = encode('foot')
        self.assertEqual(encoded, [267939702])

    def test_allcapsbird(self):
        """End to end test for the string 'BIRD'"""
        encoded = encode('BIRD')
        self.assertEqual(encoded, [251930706])

    def test_dotdotdotdot(self):
        """End to end test for the string '....'"""
        encoded = encode('....')
        self.assertEqual(encoded, [15794160])

    def test_carrotcarrotcarrotcarrot(self):
        """End to end test for the string '^^^^'"""
        encoded = encode('^^^^')
        self.assertEqual(encoded, [252706800])

    def test_capwoot(self):
        """End to end test for the string 'Woot'"""
        encoded = encode('Woot')
        self.assertEqual(encoded, [266956663])

    def test_no(self):
        """End to end test for the string 'no'"""
        encoded = encode('no')
        self.assertEqual(encoded, [53490482])

    def test_tacocat(self):
        """End to end test for the string 'tacocat'"""
        encoded = encode('tacocat')
        self.assertEqual(encoded, [267487694, 125043731])

    def test_never_odd_or_even(self):
        """End to end test for the string 'never odd or even'"""
        encoded = encode('never odd or even')
        self.assertEqual(
            encoded,
            [267657050, 233917524, 234374596, 250875466, 17830160]
        )

    def test_lagercomma_sircomma_is_regal(self):
        """End to end test for the string 'lager, sir, is regal'"""
        encoded = encode('lager, sir, is regal')
        self.assertEqual(
            encoded,
            [267394382, 167322264, 66212897, 200937635, 267422503]
        )

    def test_go_hang_a_salamicomma_capiapostrophem_a_lasagna_hog(self):
        """End to end test for the str 'go hang a salami, I'm a lasagna hog'"""
        encoded = encode("go hang a salami, I'm a lasagna hog")
        self.assertEqual(
            encoded,
            [
                200319795, 133178981, 234094669, 267441422, 78666124, 99619077,
                267653454, 133178165, 124794470
            ]
        )

    def test_egadcomma_a_base_tone_denotes_a_bad_age(self):
        """End to end test for the str 'egad, a base tone denotes a bad age'"""
        encoded = encode('egad, a base tone denotes a bad age')
        self.assertEqual(
            encoded,
            [
                267389735, 82841860, 267651166, 250793668, 233835785,
                267665210, 99680277, 133170194, 124782119
            ]
        )


class DecodeTestCase(unittest.TestCase):
    """End to end tests for the decode function"""

    def test_foo(self):
        """End to end test for the string 'foo'"""
        decoded = decode([124807030])
        self.assertEqual(decoded, 'foo')

    def test_spacefoo(self):
        """End to end test for the string ' foo'"""
        decoded = decode([250662636])
        self.assertEqual(decoded, ' foo')

    def test_foot(self):
        """End to end test for the string 'foot'"""
        decoded = decode([267939702])
        self.assertEqual(decoded, 'foot')

    def test_allcapsbird(self):
        """End to end test for the string 'BIRD'"""
        decoded = decode([251930706])
        self.assertEqual(decoded, 'BIRD')

    def test_dotdotdotdot(self):
        """End to end test for the string '....'"""
        decoded = decode([15794160])
        self.assertEqual(decoded, '....')

    def test_carrotcarrotcarrotcarrot(self):
        """End to end test for the string '^^^^'"""
        decoded = decode([252706800])
        self.assertEqual(decoded, '^^^^')

    def test_capwoot(self):
        """End to end test for the string 'Woot'"""
        decoded = decode([266956663])
        self.assertEqual(decoded, 'Woot')

    def test_no(self):
        """End to end test for the string 'no'"""
        decoded = decode([53490482])
        self.assertEqual(decoded, 'no')

    def test_tacocat(self):
        """End to end test for the string 'tacocat'"""
        decoded = decode([267487694, 125043731])
        self.assertEqual(decoded, 'tacocat')

    def test_never_odd_or_even(self):
        """End to end test for the string 'never odd or even'"""
        decoded = decode(
            [267657050, 233917524, 234374596, 250875466, 17830160]
        )
        self.assertEqual(decoded, 'never odd or even')

    def test_lagercomma_sircomma_is_regal(self):
        """End to end test for the string 'lager, sir, is regal'"""
        decoded = decode(
            [267394382, 167322264, 66212897, 200937635, 267422503]
        )
        self.assertEqual(decoded, 'lager, sir, is regal')

    def test_go_hang_a_salamicomma_capiapostrophem_a_lasagna_hog(self):
        """End to end test for the str 'go hang a salami, I'm a lasagna hog'"""
        decoded = decode([
            200319795, 133178981, 234094669, 267441422, 78666124, 99619077,
            267653454, 133178165, 124794470
        ])
        self.assertEqual(decoded, "go hang a salami, I'm a lasagna hog")

    def test_egadcomma_a_base_tone_denotes_a_bad_age(self):
        """End to end test for the str 'egad, a base tone denotes a bad age'"""
        decoded = decode([
            267389735, 82841860, 267651166, 250793668, 233835785, 267665210,
            99680277, 133170194, 124782119
        ])
        self.assertEqual(decoded, 'egad, a base tone denotes a bad age')


if __name__ == "__main__":
    unittest.main()
