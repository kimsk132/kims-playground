"""
Convert a dec number to binary.
Author: Pairode Jaroensri
Last visited: July 20, 2017
"""

def to_bin(dec):
    """ Convert the given number to a binary string. """
    result = ""
    while dec != 0:
        result = str(dec % 2) + result
        dec = dec // 2
    return result
