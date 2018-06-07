from binascii import unhexlify, hexlify
import binascii


def xor_two_hex_strings(string1, string2):
    """

    :param str1: hex encoded string
    :param str2: hex encoded string
    :return: hex encoded xor of string1 and string2
    """
    try:
        return hexlify(
            ''.join(chr(c1 ^ c2) for c1, c2 in zip(
                unhexlify(string1),
                unhexlify(string2)
            )).encode("utf8")).decode("utf-8")
    except binascii.Error:
        print("Input strings should be of equal length.")


def test_solution():
    string1 = '1c0111001f010100061a024b53535009181c'
    string2 = '686974207468652062756c6c277320657965'
    expected_output = '746865206b696420646f6e277420706c6179'
    assert xor_two_hex_strings(string1, string2) == expected_output

if __name__ == "__main__":
    string1 = '1c0111001f010100061a024b53535009181c'
    string2 = '686974207468652062756c6c277320657965'
    print("\n{}\n".format(xor_two_hex_strings(string1, string2)))

# ord() returns the corresponding ASCII code of a character e.g. ord('s') --> 115
# chr() returns the corresponding ASCII character of a code e.g. chr(97) --> 'a', chr(0x61) --> 'a'
