def cCipher(msg_str,shift):
    """ (str,int) --> (str)

    Return the msg_str parameter equivalent by converting the string to Unicode
    and outputting the value of the input_str + shift (type int) in Unicode back
    to a string with the shift.

    Some examples:

    cCipher('abc', 1)
    >>> 'bcd'
    cCipher('123', 3)
    >>> '456'
    cCipher(44, 3)
    >>> 'The input is not a string' 
    cCipher('143Hg!)>#', 2)
    >>> '365Ji#+@%'
    cCipher("Here's 2 U MRS Robinson", 1)
    >>> 'Ifsf(t!3!V!NST!Spcjotpo'
    """

    cipher_conv = ''

    for i in range(len(str(msg_str))):
        if type(msg_str) == str:
            cipher_conv = cipher_conv + chr(ord(msg_str[i]) + shift)
        else:
            #print('This input is not a string')
            cipher_conv = 'This input is not a string'
    return cipher_conv

print(cCipher('abc', 1))
print(cCipher('123', 3))
print(cCipher("Here's 2 U MRS Robinson", 1))
print(cCipher('143Hg!)>#', 2))
print(cCipher(44, 3))

   



