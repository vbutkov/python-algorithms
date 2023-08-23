def generate_alphabet():
    alphabet = ""
    for i in range(ord('a'), ord('z') + 1):
        alphabet += chr(i)

    return alphabet


def crypt2(data, alphabet, offset):
    result = ""
    for ch in data:
        position = alphabet.find(ch)
        result += alphabet[(position + offset) % len(alphabet)]

    return result


def decrypt2(data, alphabet, offset):
    return crypt2(data, alphabet, -offset)


# def crypt(data, alphabet):
#     data_crypt = ""
#     for ch in data:
#         position = alphabet.find(ch)
#         data_crypt += alphabet[(position + 1) % len(alphabet)]
#
#     return data_crypt
#
#
# def decrypt(data, alphabet):
#     data_decrypt = ""
#     for ch in data:
#         position = alphabet.find(ch)
#         data_decrypt += alphabet[(position - 1) % len(alphabet)]
#
#     return data_decrypt
#

def cipher_cesar(data):
    alphabet = generate_alphabet()

    data_crypt = crypt2(data, alphabet, 56)
    print(data_crypt)

    data_decrypt = decrypt2(data_crypt, alphabet, 56)
    print(data_decrypt)


if __name__ == '__main__':
    cipher_cesar("abcdzzaz")
