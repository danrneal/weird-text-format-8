"""Part 1 of the Art+Logic Programming Challenge

Takes a 4 character block of text and encodes it using a weird text format
"""


def main():
    """Main function call, runs encode script"""
    string = input("String to process: ")
    while len(string) > 4:
        print("String must be 4 characters or less")
        string = input("String to process: ")

    encoded = encode(string)
    print(encoded)


def str_to_bin(string):
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


def scramble_bin(binary):
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


def bin_to_dec(binary):
    """Converts an array of 4 binary numbers into a single decimal number

    Args:
        binary: A list containing 4 binary numbers

    Returns:
        decimal: An int representation of the 4 binary numbers
    """
    decimal = int(''.join(binary), 2)

    return decimal


def dec_to_bin(decimal):
    """Converts a single decimal number into an array of 4 binary numbers

    Args:
        decimal: An int representation of 4 binary numbers

    Returns:
        binary: A list containing the 4 binary numbers
    """
    return decimal


def encode(string):
    """Encodes bundles of 4 characters using a weird text format

    Args:
        string: The string to be encoded

    Returns:
        encoded: An list of ints representing the encoded string
    """

    encoded = []

    for i in range(0, len(string), 4):
        binary = str_to_bin(string[i:i+4])
        scrambled = scramble_bin(binary)
        decimal = bin_to_dec(scrambled)
        encoded.append(decimal)

    return encoded


if __name__ == "__main__":
    main()
