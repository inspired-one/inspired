def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    ciphertext = ''
    for symbol in plaintext:
        if symbol.isalpha():
            num = ord(symbol)
            num += 3
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
            ciphertext += chr(num)
        else:
            ciphertext += symbol

#    print(ciphertext)
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    plaintext = ''
    for symbol in ciphertext:
        if symbol.isalpha():
            num = ord(symbol)
            num -= 3
            if symbol.isupper():
                if num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num < ord('a'):
                    num += 26
            plaintext += chr(num)
        else:
            plaintext += symbol

#    print(plaintext)
    return plaintext