def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    count = 0


    for letters in plaintext:
        character = ord(keyword[count % len(keyword)])
        count += 1
        if 65 <= character <= 91:
            character -= 65
        elif 97 <= character <= 122:
            character -= 97
        else:
            continue
        if 65 <= ord(letters) <= 90:
            ciphertext += chr((ord(letters) - 65 + character + 26) % 26 + 65)
        elif 97 <= ord(letters) <= 122:
            ciphertext += chr((ord(letters) - 97 + character + 26) % 26 + 97)
        else:
            ciphertext += letters


    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    plaintext = ''
    count = 0


    for letters in ciphertext:
        character = ord(keyword[count % len(keyword)])
        count += 1
        if 65 <= character <= 90:
            character -= 65
        elif 97 <= character <= 122:
            character -= 97
        else:
            continue
        if 65 <= ord(letters) <= 90:
            plaintext += chr((ord(letters) - 65 - character + 26) % 26 + 65)
        elif 97 <= ord(letters) <= 122:
            plaintext += chr((ord(letters) - 97 - character + 26) % 26 + 97)
        else:
            plaintext += letters


    return plaintext