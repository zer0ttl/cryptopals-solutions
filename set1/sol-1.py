import base64
import sys


data = input("\nEnter the string: ")
string_data = bytes.fromhex(data) # converting the hex string to raw bytes
string_base64 = base64.encodebytes(string_data) # encoding the raw bytes to base64 bytes

print("String : ")
sys.stdout.buffer.write(string_data + '\n'.encode(encoding='utf-8'))
print("Base64 encoded String : ")
sys.stdout.buffer.write(string_base64 + '\n'.encode(encoding='utf-8'))