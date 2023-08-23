def crypt_symbol(ch):
    if ch == 'z':
        return 'a'
    else:
        return chr(ord(ch) + 1)


def decrypt_symbol(ch):
    if ch == 'a':
        return 'z'
    else:
        return chr(ord(ch) - 1)


def cipher_cesar(data):
    crypt_data = ""
    for ch in data:
        crypt_data += str(crypt_symbol(ch))

    print(f"Data {data} crypt: {crypt_data}")

    decrypt_data = ""
    for ch in crypt_data:
        decrypt_data += str(decrypt_symbol(ch))

    print(f"Data {crypt_data} decrypt: {decrypt_data}")


if __name__ == '__main__':
    cipher_cesar("abcdzaz")
