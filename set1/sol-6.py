import binascii


# bytes in python3 always return the ascii value of the byte
def to_binary(string):
    return ''.join((format(char, '010b'))for char in string.encode("utf-8"))
    # 010b means pad the output to 10 bits


# hamming_distance is also known as edit_distance
# hamming distance is the number of differing bits
def hamming_distance(string1, string2):
    binary_string1 = to_binary(string1)
    binary_string2 = to_binary(string2)
    data = zip(binary_string1, binary_string2)
    count = 0
    for item in data:
        if item[0] != item[1]:
            count += 1
    return count


s1 = "this is a test"
s2 = "wokka wokka!!!"

count = hamming_distance(s1, s2)

print(count)