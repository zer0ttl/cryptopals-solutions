from binascii import hexlify, unhexlify

# ord() returns the corresponding ASCII code of a character e.g. ord('s') --> 115
# chr() returns the corresponding ASCII character of a code e.g. chr(97) --> 'a', chr(0x61) --> 'a'


def xor_key_brute_forcer(string):
    bytes = unhexlify(string)
    key = max(bytes, key=bytes.count) ^ ord(' ') # I don't know how this works. Code copied https://stackoverflow.com/questions/41819489/single-byte-xor-cipher-python#41819939
    print('\nKey is : ' + chr(key))
    return chr(key)


def single_byte_xor(string, single_char):
    return ''.join(chr(char ^ ord(single_char)) for char in unhexlify(string))

hex_encoded_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
print('\n' + single_byte_xor(hex_encoded_string,xor_key_brute_forcer(hex_encoded_string)) + '\n')

