crypt_mode = input('[E]ncrypt | [D]ecrypt: ').upper()
if crypt_mode not in ['E', 'D']:
    print('Error: mode is not found')
    raise SystemExit

start_message = input('Write the message: ').upper()
number_keys = int(input('How much keys: '))

list_keys = []
for index in range(number_keys):
    list_keys.append(input('Write the keyWord[' + str(index) + ']: '))


def encrypt_decrypt(mode, message, keys):
    for key in list_keys:
        final = ''
        key *= len(message) // len(key) + 1
        for index, symbol in enumerate(message):
            if mode == 'E':
                temp = ord(symbol) + ord(key[index]) - 13
            else:
                temp = ord(symbol) - ord(key[index]) - 13
            final += chr(temp % 26 + ord('A'))
        message = final
        print(message)
    return final
print('Final message:', encrypt_decrypt(crypt_mode, start_message, list_keys))
