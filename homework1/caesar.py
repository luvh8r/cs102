def encrypt_caesar(plaintext):
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''


    for letters in plaintext:
        if 120 <= ord(letters) <= 122 or 88 <= ord(letters) <= 90:
            ciphertext += chr(ord(letters) + 3 - 26)
        elif 65 <= ord(letters) < 89 or 97 <= ord(letters) < 120:
            ciphertext += chr(ord(letters) + 3)
        else:
            ciphertext += letters


    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''


    for letters in ciphertext:
        if 65 <= ord(letters) <= 67 or 97 <= ord(letters) <= 98:
            plaintext += chr(ord(letters) + 26 - 3)
        elif 67 < ord(letters) <= 90 or 98 < ord(letters) <= 122:
            plaintext += chr(ord(letters) - 3)
        else:
            plaintext += (letters)


    return plaintext

