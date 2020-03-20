"""Encode and decode strings in Weird Text Format-8

Part of the Art+Logic Programming Challenge

    usage: WeirdTextFormat8.py [-h] [-e | -d] [-i [INFILE]] [-o [OUTFILE]]
"""
import argparse
import json
import sys


def main():
    """Main function call, runs encode script"""
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-e', '--encode',
        action='store_true',
        help=(
            'Encode a string into the corresponding list of integer values'
            'using Weird Text Format-8'
        )
    )
    group.add_argument(
        '-d', '--decode',
        action='store_true',
        help=(
            'Decode a list of integer values encoded with Weird Text Format-8'
            'back into its original string'
        )
    )
    parser.add_argument(
        '-i', '--infile',
        nargs='?',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help='Specify a file to read input from (default: stdin)'
    )
    parser.add_argument(
        '-o', '--outfile',
        nargs='?',
        type=argparse.FileType('w'),
        default=sys.stdout,
        help='Specity a file to write output to (default: stdout)'
    )
    args = parser.parse_args()

    while not args.encode and not args.decode:
        encodeOrDecode = input('(E)ncode or (D)ecode? ')
        if encodeOrDecode.lower() in ('e', 'encode'):
            args.encode = True
        elif encodeOrDecode.lower() in ('d', 'decode'):
            args.decode = True

    if args.infile == sys.stdin:
        string = input("String to process: ")
    else:
        with args.infile as infile:
            string = infile.read()

    if args.encode:

        encoded = encode(string)
        output = json.dumps(encoded)

    else:

        try:
            decimals = json.loads(string)
        except json.decoder.JSONDecodeError:
            print('String to decode was not properly formatted')
            print('e.g. [266395138, 158874521, 267541809, 1048577]')
            sys.exit(1)

        output = decode(decimals)

    with args.outfile as outfile:
        print(f'Writing output to {outfile.name}')
        outfile.write(output)
        print('\nDone!')


def strToBin(string):
    """Converts a 4 character string to binary

    Args:
        string: A str consisting of 4 characters or less

    Returns:
        binary: A list of 4 elements representing each character in binary
            format
    """

    binary = ['00000000', '00000000', '00000000', '00000000']

    n = -1
    for char in string:
        bits = bin(ord(char))[2:]
        bits = '00000000'[:8-len(bits)] + bits
        binary[n] = bits
        n -= 1

    return binary


def binToStr(binary):
    """Converts a 4 element list of binary to a 4 character string

    Args:
        binary: A list of 4 elements representing each character in binary
            format

    Returns:
        string: A str consisting of 4 characters or less
    """

    string = ''

    while len(binary) > 0:
        string += chr(int(binary.pop(), 2))

    string = string.strip('\x00')

    return string


def scrambleBin(binary):
    """Scrambles a 4 element list representing the binary of 4 character

    Args:
        binary: A list containing 4 elements that are the binary representation
            of characters

    Returns:
        scrambled: A list containing 4 elements which are the result of
            scrambling the input
    """

    scrambled = ['', '', '', '']

    n = 0
    for i in range(len(scrambled)):
        while len(scrambled[i]) < len(binary[i]):

            for char in binary:
                scrambled[i] += char[n]

            n += 1

    return scrambled


def unscrambleBin(binary):
    """Unscrambles a 4 element list representing the binary of 4 characters

    Args:
        binary: A list containing 4 elements which are the scrambled
            representation of 4 characters

    Returns:
        unscrambled: A list containing 4 elements that are the binary
            representation of characters
    """

    unscrambled = ['', '', '', '']

    n = 0
    for scrambledBinary in binary:
        for char in scrambledBinary:
            unscrambled[n % 4] += char
            n += 1

    return unscrambled


def binToDec(binary):
    """Converts an array of 4 binary numbers into a single decimal number

    Args:
        binary: A list containing 4 binary numbers

    Returns:
        decimal: An int representation of the 4 binary numbers
    """
    decimal = int(''.join(binary), 2)

    return decimal


def decToBin(decimal):
    """Converts a single decimal number into an array of 4 binary numbers

    Args:
        decimal: An int representation of 4 binary numbers

    Returns:
        binary: A list containing the 4 binary numbers
    """

    binary = ['00000000', '00000000', '00000000', '00000000']
    allBits = bin(decimal)[2:]

    for i in range(len(binary), 0, -1):

        if len(allBits) > 8:
            binary[i-1] = allBits[len(allBits) - 8:]
        else:
            binary[i-1] = '00000000'[:8-len(allBits)] + allBits

        allBits = allBits[:len(allBits) - 8]

    return binary


def encode(string):
    """Encodes bundles of 4 characters using a weird text format

    Args:
        string: The string to be encoded

    Returns:
        encoded: An list of ints representing the encoded string
    """

    encoded = []

    for i in range(0, len(string), 4):
        binary = strToBin(string[i:i+4])
        scrambled = scrambleBin(binary)
        decimal = binToDec(scrambled)
        encoded.append(decimal)

    return encoded


def decode(decimals):
    """Decodes decimals representing bundles of 4 chars in a weird text format

    Args:
        decimals: A list of decimals representing bundles of 4 characters

    Returns:
        decoded: A str represending the decoded string
    """

    decoded = ''

    for decimal in decimals:
        binary = decToBin(decimal)
        unscrambled = unscrambleBin(binary)
        string = binToStr(unscrambled)
        decoded += string

    return decoded


if __name__ == "__main__":
    main()
