"""
A full RSA program for both encryption and decryption.
Author: Pairode Jaroensri
Last visited August 29, 2017
"""


import ast

"======= Utilities ======="

def ext_gcd(x, y):
    """ Calculates the GCD of X and Y using Euclid's Algorithm. """
    if x < y:
        # print("Warning: the first number should be greater than the second number.")
        return ext_gcd(y, x)
    if y == 0:
        return (x, 1, 0)
    (d, a, b) = ext_gcd(y, x % y)
    return (d, b, a - b * (x // y))

def mul_inverse(x, y):
    """ Returns the multiplicative inverse of X mod Y. """
    ans = ext_gcd(y, x)[2]
    if ans >= 0:
        return ans
    return ans + y

def write_file(filename, string):
    """ Write the STRING to a file with the given FILENAME"""
    string = str(string)
    file = open(filename, 'w')
    file.write(string)
    file.close()
    print("File written successfully.")


"======= RSA Core ======="

N = 0x2cf86796c1005d7f131f01a0c39f4709c237b5a69fcc7a61877e918016508b18103f59388a2f56fdf17efa832c3fecdb6bc7ce3631657f255aa157ccde30532ad16ab8aad55846b27da7788c851700c0b1ad8d01396f8c84c81e8eb301e92300844669de125fa183e7a9d45c814bdf734023e16b47e0000990810ae4b65e82f1
p = 0x99cac88930fdb5d19f37a6a74fd40514dc022660d0a1d47db496f37815e092c2f6aa07ad7ce6aa230018967154264076efc5564df78e6afbd334ba3c07c815e1
q = 0x4adb5f201d7b7538c146b2285b0d30150e4a4462dcc68367d928a95587343ca82ed61e46940b35915259b874174c22ffe83fca913ff0240437b07a634aa8ef11
k = (p - 1) * (q - 1)
e = 65537
d = mul_inverse(e, k)

def encrypt(string):
    """ Encrypt the STRING using the defined public keys.
    Returns a Python List of encrypted characters. """
    if type(string) != str:
        string = str(string)
    result = [pow(ord(i), e, N) for i in string]
    return result

def encrypt_to_str(string):
    result = encrypt(string)
    result = [hex(x)[2:] for x in result]
    return "".join(result)

def encrypt_to_file(string, filename):
    """ Encrypt the STRING using the defined public keys,
    then write the encrypted string to a file. """
    encrypted_string = encrypt(string)
    write_file(filename, encrypted_string)
    return encrypted_string

def decrypt(char_list):
    """ Takes in a Python List of encrypted characters, decrypt the characters one-by-one,
    then recombine the characters into a string. """
    result = [chr(pow(x, d, N)) for x in char_list]
    return "".join(result)

def decrypt_from_str(string):
    pass

def decrypt_file(filename):
    """ Read in a file that contains a Python List of encrypted characters, then decrypt it. """
    file = open(filename, 'r')
    encrypted = ast.literal_eval(file.read())
    file.close()
    return decrypt(encrypted)
