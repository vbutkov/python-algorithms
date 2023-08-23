def generate_alphabet():
    alphabet = ""
    for i in range(ord('a'), ord('z') + 1):
        alphabet += chr(i)

    return alphabet


def crypt(data, alphabet):
    data_crypt = ""
    for ch in data:
        position = alphabet.find(ch)
        data_crypt += alphabet[(position + 1) % len(alphabet)]

    return data_crypt


def decrypt(data, alphabet):
    data_decrypt = ""
    for ch in data:
        position = alphabet.find(ch)
        data_decrypt += alphabet[(position - 1) % len(alphabet)]

    return data_decrypt


def cipher_cesar(data):
    alphabet = generate_alphabet()

    data_crypt = crypt(data, alphabet)
    print(data_crypt)

    data_decrypt = decrypt(data_crypt, alphabet)
    print(data_decrypt)


if __name__ == '__main__':
    cipher_cesar("abcdzzaz")
