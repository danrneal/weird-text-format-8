"""Test objects used to test the behavior in part1 of the alpc"""

import unittest
from WeirdTextFormat8 import (
    strToBin, binToStr, scrambleBin, unscrambleBin, binToDec,
    decToBin, encode, decode
)


class AStrToBinTestCase(unittest.TestCase):
    """This class represents the test cases for the strToBin function"""

    def testSingleCharacter(self):
        """Test conversion to binary for a single character"""
        binary = strToBin('A')
        self.assertEqual(
            binary,
            ['00000000', '00000000', '00000000', '01000001']
        )

    def testFullBundle(self):
        """Test conversion to binary for a full 4 characters"""
        binary = strToBin('FRED')
        self.assertEqual(
            binary,
            ['01000100', '01000101', '01010010', '01000110']
        )

    def testNonAlphanumerics(self):
        """Test conversion to binary for non-alphanumeric characters"""
        binary = strToBin(' :^)')
        self.assertEqual(
            binary,
            ['00101001', '01011110', '00111010', '00100000']
        )


class ABinToStrTestCase(unittest.TestCase):
    """This class represents the test cases for the binToStr function"""

    def testSingleCharacter(self):
        """Test conversion from binary for a single character"""
        string = binToStr(['00000000', '00000000', '00000000', '01000001'])
        self.assertEqual(string, 'A')

    def testFullBundle(self):
        """Test conversion from binary for a full 4 characters"""
        string = binToStr(['01000100', '01000101', '01010010', '01000110'])
        self.assertEqual(string, 'FRED')

    def testNonAlphanumerics(self):
        """Test conversion from binary for non-alphanumeric characters"""
        string = binToStr(['00101001', '01011110', '00111010', '00100000'])
        self.assertEqual(string, ' :^)')


class AScrambleBinTestCase(unittest.TestCase):
    """This class represents the test cases for the scrambleBin function"""

    def testSingleCharacter(self):
        """Test scrambling binary for a single character"""
        scrambled_binary = scrambleBin(
            ['00000000', '00000000', '00000000', '01000001']
        )
        self.assertEqual(
            scrambled_binary,
            ['00000001', '00000000', '00000000', '00000001']
        )

    def testFullBundle(self):
        """Test scrambling binary for a full 4 characters"""
        scrambled_binary = scrambleBin(
            ['01000100', '01000101', '01010010', '01000110']
        )
        self.assertEqual(
            scrambled_binary,
            ['00001111', '00000010', '00001101', '00110100']
        )

    def testNonAlphanumerics(self):
        """Test scrambling binary for non-alphanumeric characters"""
        scrambled_binary = scrambleBin(
            ['00101001', '01011110', '00111010', '00100000']
        )
        self.assertEqual(
            scrambled_binary,
            ['00000100', '10110110', '11100100', '01101000']
        )


class AUncrambleBinTestCase(unittest.TestCase):
    """This class represents the test cases for the unscrambleBin function"""

    def testSingleCharacter(self):
        """Test unscrambling binary for a single character"""
        unscrambled_binary = unscrambleBin(
            ['00000001', '00000000', '00000000', '00000001']
        )
        self.assertEqual(
            unscrambled_binary,
            ['00000000', '00000000', '00000000', '01000001']
        )

    def testFullBundle(self):
        """Test unscrambling binary for a full 4 characters"""
        unscrambled_binary = unscrambleBin(
            ['00001111', '00000010', '00001101', '00110100']
        )
        self.assertEqual(
            unscrambled_binary,
            ['01000100', '01000101', '01010010', '01000110']
        )

    def testNonAlphanumerics(self):
        """Test unscrambling binary for non-alphanumeric characters"""
        unscrambled_binary = unscrambleBin(
            ['00000100', '10110110', '11100100', '01101000']
        )
        self.assertEqual(
            unscrambled_binary,
            ['00101001', '01011110', '00111010', '00100000']
        )


class ABinToDecTestCase(unittest.TestCase):
    """This class represents the test cases for the binToDec function"""

    def testSingleCharacter(self):
        """Test conversion to decimal for a single character"""
        decimal = binToDec(['00000001', '00000000', '00000000', '00000001'])
        self.assertEqual(decimal, 16777217)

    def testFullBundle(self):
        """Test conversion to decimal for a full 4 characters"""
        decimal = binToDec(['00001111', '00000010', '00001101', '00110100'])
        self.assertEqual(decimal, 251792692)

    def testNonAlphanumerics(self):
        """Test conversion from to decimal for non-alphanumeric characters"""
        decimal = binToDec(['00000100', '10110110', '11100100', '01101000'])
        self.assertEqual(decimal, 79094888)


class ADecToBinTestCase(unittest.TestCase):
    """This class represents the test cases for the decToBin function"""

    def testSingleCharacter(self):
        """Test conversion from decimal for a single character"""
        binary = decToBin(16777217)
        self.assertEqual(
            binary,
            ['00000001', '00000000', '00000000', '00000001']
        )

    def testFullBundle(self):
        """Test conversion to decimal for a full 4 characters"""
        binary = decToBin(251792692)
        self.assertEqual(
            binary,
            ['00001111', '00000010', '00001101', '00110100']
        )

    def testNonAlphanumerics(self):
        """Test conversion from to decimal for non-alphanumeric characters"""
        binary = decToBin(79094888)
        self.assertEqual(
            binary,
            ['00000100', '10110110', '11100100', '01101000']
        )


class AEncodeTestCase(unittest.TestCase):
    """End to end tests for the encode function"""

    def testFoo(self):
        """End to end test for the string 'foo'"""
        encoded = encode('foo')
        self.assertEqual(encoded, [124807030])

    def testSpaceFoo(self):
        """End to end test for the string ' foo'"""
        encoded = encode(' foo')
        self.assertEqual(encoded, [250662636])

    def testFoot(self):
        """End to end test for the string 'foot'"""
        encoded = encode('foot')
        self.assertEqual(encoded, [267939702])

    def testAllCapsBird(self):
        """End to end test for the string 'BIRD'"""
        encoded = encode('BIRD')
        self.assertEqual(encoded, [251930706])

    def testDotDotDotDot(self):
        """End to end test for the string '....'"""
        encoded = encode('....')
        self.assertEqual(encoded, [15794160])

    def testCarrotCarrotCarrotCarrot(self):
        """End to end test for the string '^^^^'"""
        encoded = encode('^^^^')
        self.assertEqual(encoded, [252706800])

    def testCapWoot(self):
        """End to end test for the string 'Woot'"""
        encoded = encode('Woot')
        self.assertEqual(encoded, [266956663])

    def testNo(self):
        """End to end test for the string 'no'"""
        encoded = encode('no')
        self.assertEqual(encoded, [53490482])

    def testTacocat(self):
        """End to end test for the string 'tacocat'"""
        encoded = encode('tacocat')
        self.assertEqual(encoded, [267487694, 125043731])

    def testNeverOddOrEven(self):
        """End to end test for the string 'never odd or even'"""
        encoded = encode('never odd or even')
        self.assertEqual(
            encoded,
            [267657050, 233917524, 234374596, 250875466, 17830160]
        )

    def testLagerCommaSitCommaIsRegal(self):
        """End to end test for the string 'lager, sir, is regal'"""
        encoded = encode('lager, sir, is regal')
        self.assertEqual(
            encoded,
            [267394382, 167322264, 66212897, 200937635, 267422503]
        )

    def testGoHangASalamiCommaImALasagnaHog(self):
        """End to end test for the str 'go hang a salami, I'm a lasagna hog'"""
        encoded = encode("go hang a salami, I'm a lasagna hog")
        self.assertEqual(
            encoded,
            [
                200319795, 133178981, 234094669, 267441422, 78666124, 99619077,
                267653454, 133178165, 124794470
            ]
        )

    def testEgadCommaABaseToneDenotesABadAge(self):
        """End to end test for the str 'egad, a base tone denotes a bad age'"""
        encoded = encode('egad, a base tone denotes a bad age')
        self.assertEqual(
            encoded,
            [
                267389735, 82841860, 267651166, 250793668, 233835785,
                267665210, 99680277, 133170194, 124782119
            ]
        )


class ADecodeTestCase(unittest.TestCase):
    """End to end tests for the decode function"""

    def testFoo(self):
        """End to end test for the string 'foo'"""
        decoded = decode([124807030])
        self.assertEqual(decoded, 'foo')

    def testSpaceFoo(self):
        """End to end test for the string ' foo'"""
        decoded = decode([250662636])
        self.assertEqual(decoded, ' foo')

    def testFoot(self):
        """End to end test for the string 'foot'"""
        decoded = decode([267939702])
        self.assertEqual(decoded, 'foot')

    def testAllCapsBird(self):
        """End to end test for the string 'BIRD'"""
        decoded = decode([251930706])
        self.assertEqual(decoded, 'BIRD')

    def testDotDotDotDot(self):
        """End to end test for the string '....'"""
        decoded = decode([15794160])
        self.assertEqual(decoded, '....')

    def testCarrotCarrotCarrotCarrot(self):
        """End to end test for the string '^^^^'"""
        decoded = decode([252706800])
        self.assertEqual(decoded, '^^^^')

    def testCapWoot(self):
        """End to end test for the string 'Woot'"""
        decoded = decode([266956663])
        self.assertEqual(decoded, 'Woot')

    def testNo(self):
        """End to end test for the string 'no'"""
        decoded = decode([53490482])
        self.assertEqual(decoded, 'no')

    def testTacocat(self):
        """End to end test for the string 'tacocat'"""
        decoded = decode([267487694, 125043731])
        self.assertEqual(decoded, 'tacocat')

    def testNeverOddOrEven(self):
        """End to end test for the string 'never odd or even'"""
        decoded = decode(
            [267657050, 233917524, 234374596, 250875466, 17830160]
        )
        self.assertEqual(decoded, 'never odd or even')

    def testLagerCommaSitCommaIsRegal(self):
        """End to end test for the string 'lager, sir, is regal'"""
        decoded = decode(
            [267394382, 167322264, 66212897, 200937635, 267422503]
        )
        self.assertEqual(decoded, 'lager, sir, is regal')

    def testGoHangASalamiCommaImALasagnaHog(self):
        """End to end test for the str 'go hang a salami, I'm a lasagna hog'"""
        decoded = decode([
            200319795, 133178981, 234094669, 267441422, 78666124, 99619077,
            267653454, 133178165, 124794470
        ])
        self.assertEqual(decoded, "go hang a salami, I'm a lasagna hog")

    def testEgadCommaABaseToneDenotesABadAge(self):
        """End to end test for the str 'egad, a base tone denotes a bad age'"""
        decoded = decode([
            267389735, 82841860, 267651166, 250793668, 233835785, 267665210,
            99680277, 133170194, 124782119
        ])
        self.assertEqual(decoded, 'egad, a base tone denotes a bad age')


if __name__ == "__main__":
    unittest.main()
