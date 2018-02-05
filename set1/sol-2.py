from binascii import unhexlify, hexlify
import binascii


# for hex encoded strings of same length
def xor_two_hex_strings(str1, str2):
    try:
        ''.join(chr(c1 ^ c2) for c1, c2 in zip(unhexlify(str1), unhexlify(str2)))
    except binascii.Error as e:
        print("\nSomething went wrong! %" %e)
        return None
    return ''.join(chr(c1 ^ c2) for c1, c2 in zip(unhexlify(str1), unhexlify(str2)))

a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

print(hexlify(xor_two_hex_strings(a, b).encode('utf-8')).decode('utf-8'))


# ord() returns the corresponding ASCII code of a character e.g. ord('s') --> 115
# chr() returns the corresponding ASCII character of a code e.g. chr(97) --> 'a', chr(0x61) --> 'a'

