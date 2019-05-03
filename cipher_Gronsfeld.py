crypt_mode = input('[E]ncrypt | [D]ecrypt: ').upper()
if crypt_mode not in ['E', 'D']:
    print('Error: mode is not found')
    raise SystemError

start_message = input('Write the message: ').upper()
key_message = input('Write the keyNumber: ')


def encrypt_decrypt(mode, message, key, final=''):
    key *= len(message) // len(key) + 1
    for index, symbol in enumerate(message):
        if mode == 'E':
            temp = ord(symbol) + int(key[index]) - 13
        else:
            temp = ord(symbol) - int(key[index]) - 13

        final += chr(temp % 26 + ord('A'))
    return final


print('Final message:', encrypt_decrypt(crypt_mode, start_message, key_message))
