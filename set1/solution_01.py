import base64


def hex_to_base64(string):
    """
    :param string: Hex encoded string as input
    :return: returns a base64 encoded string output
    """
    try:
        return base64.b64encode(bytes.fromhex(string)).decode("utf8")
    except ValueError:
        print("Input not a valid hex string.")


def test_solution():
    string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    final_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    assert hex_to_base64(string) == final_output


if __name__ == '__main__':
    print('\n{}\n'.format(hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')))