"""
utils
"""

def split_arr(s, l):
    """split arr"""
    parts = []
    for i in range(0, len(s), l):
        parts.append(s[i:i+l])
    return parts

def rotate_char(char, n=1):
    """rotate char"""
    n = (int(char, base=16) + n) % 16
    return hex(n)[2:]

def rotate_chars(string, n=1):
    """rotate chars"""
    rotated_string = ''
    for c in string:
        rotated_string += rotate_char(c, n)
    return rotated_string

def hex2chars(hex_str):
    """hex2chars"""
    string = ""
    parts = split_arr(hex_str, 2)
    for char in parts:
        string += chr(int(char, base=16))
    return string
