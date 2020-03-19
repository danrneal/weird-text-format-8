"""Part 1 of the Art+Logic Programming Challenge

Takes a 4 character block of text and encodes it using a weird text format
"""


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
