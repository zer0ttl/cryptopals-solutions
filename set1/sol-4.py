from binascii import hexlify, unhexlify
import re

# ord() returns the corresponding ASCII code of a character e.g. ord('s') --> 115
# chr() returns the corresponding ASCII character of a code e.g. chr(97) --> 'a', chr(0x61) --> 'a'


def xor_key_brute_forcer(string):
    bytes = unhexlify(string)
    key = max(bytes, key=bytes.count) ^ ord(' ') # I don't know how this works. Code copied https://stackoverflow.com/questions/41819489/single-byte-xor-cipher-python#41819939
    # print('\nKey is : ' + chr(key))
    return chr(key)


def single_byte_xor(string, single_char):
    return ''.join(chr(char ^ ord(single_char)) for char in unhexlify(string))


def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# def isEnglish(s):
#     try:
#         s.encode(encoding='utf-8').decode('ascii')
#     except UnicodeDecodeError:
#         return False
#     else:
#         return True


with open("4.txt") as file:
    for line in file:
        string = single_byte_xor(line.strip(),xor_key_brute_forcer(line.strip()))
        # if isEnglish(string):
        #     print(string)
        if is_ascii(string):
            print(string)

