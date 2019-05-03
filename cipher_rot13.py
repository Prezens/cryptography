text = input('Message: ')


def encrypt_decrypt(message):
    encrypt = ''
    for i in range(len(message)):
        encrypt += chr((ord(message[i]) - 13) % 26 + ord('A'))
    return encrypt

print(encrypt_decrypt(text))
