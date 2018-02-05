from binascii import hexlify, unhexlify
import binascii


def generate_key(plaintext, key):
    if len(plaintext) % len(key) == 0:
        key = key * (int(len(plaintext) / len(key)))
    else:
        key = key * (int(len(plaintext) / len(key)) + int(len(plaintext) % len(key)))
    return key


def xor_two_raw_strings(string, key):
    if len(string) == len(key):
        try:
            ''.join(chr(c1 ^ c2) for c1, c2 in zip(string.encode("utf-8"), key.encode("utf-8")))
        except binascii.Error as e:
            print("\nSomething went wrong! %" %e)
            return None
        return ''.join(chr(c1 ^ c2) for c1, c2 in zip(string.encode("utf-8"), key.encode("utf-8")))
    else:
        key = generate_key(string, key)
        try:
            ''.join(chr(c1 ^ c2) for c1, c2 in zip(string.encode("utf-8"), key.encode("utf-8")))
        except binascii.Error as e:
            print("\nSomething went wrong! %" %e)
            return None
        return ''.join(chr(c1 ^ c2) for c1, c2 in zip(string.encode("utf-8"), key.encode("utf-8")))


string = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"


xor = xor_two_raw_strings(string, key)
print(hexlify(xor.encode("utf-8")))