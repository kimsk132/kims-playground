"""
An RSA client for encrypting strings. The encrypted message can then be sent to the host.
Author: Pairode Jaroensri
Last visited August 29, 2017
"""

"========== RSA Core =========="

def encrypt(string):
    N = 0x2cf86796c1005d7f131f01a0c39f4709c237b5a69fcc7a61877e918016508b18103f59388a2f56fdf17efa832c3fecdb6bc7ce3631657f255aa157ccde30532ad16ab8aad55846b27da7788c851700c0b1ad8d01396f8c84c81e8eb301e92300844669de125fa183e7a9d45c814bdf734023e16b47e0000990810ae4b65e82f1
    e = 65537
    string = str(string)
    result = [pow(ord(i), e, N) for i in string]
    return result

def write_file(filename, string):
    string = str(string)
    file = open(filename + ".txt", 'w')
    file.write(string)
    file.close()
    print("Encrypted message written successfully.")

"========== User Interface =========="

def is_yes(string):
    return string == 'y' or string == 'Y'

def confirm_exit():
    choice = input("Are you sure you want to exit? (y/N): ")
    if is_yes(choice):
        exit()

while True:
    print("Welcome to Kim's RSA encryptor!")
    message = input("Enter the message you wish to encrypt: ")
    encrypted = encrypt(message)
    choice = input("Would you like to see the encrypted message? (y/N): ")
    if is_yes(choice):
        print(encrypted)
    choice = input("Would you like to save the encrypted message to a file? (y/N): ")
    if is_yes(choice):
        name = input("Enter file name: ")
        write_file(name, encrypted)
    choice = input("Would you like to encrypt another message? (y/N): ")
    if not is_yes(choice):
        break

