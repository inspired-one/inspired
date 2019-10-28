def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    import string
    ciphertext = ''
    subkey = []
    for k in keyword:
        subkey.append((string.ascii_letters.find(k)) % 26)  # ключи для каждой буквы
    # print(subkey)  # проверка на правильность
    i = 0
    for c in plaintext:
        if i == len(subkey):  # цикл повторения ключа
            i = 0
        char_ord = (string.ascii_letters.find(c) % 26) + subkey[i]
        if char_ord > 25:
            char_ord -= 26
        #  print(char_ord)  # проверка на правильность
        if c.isupper():
            ciphertext += string.ascii_letters[char_ord].capitalize()
        elif c.islower():
            ciphertext += string.ascii_letters[char_ord]
        i += 1
    # print(ciphertext)  # проверка на правильность
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    import string
    plaintext = ''
    subkey = []
    for k in keyword:
        subkey.append((string.ascii_letters.find(k)) % 26)  # нащел
    # print(subkey)  # проверка на правильность
    i = 0
    for c in ciphertext:
        if i == len(subkey):
            i = 0
        char_ord = (string.ascii_letters.find(c) % 26) - subkey[i]
        if char_ord < 1:
            char_ord += 26
        #  print(char_ord)  # проверка на правильность
        if c.isupper():
            plaintext += string.ascii_letters[char_ord].capitalize()
        elif c.islower():
            plaintext += string.ascii_letters[char_ord]
        i += 1
    # print(plaintext)  # проверка на правильность
    return plaintext