crypt_mode = input('[E]ncrypt | [D]ecrypt: ').upper()

if crypt_mode not in ['E', 'D']:
    print('Error: mode is not found')
    raise SystemError

start_message = list(input('Write the message: ').upper())
for i in start_message:
    if i not in [chr(x) for x in range(65, 91)]:
        start_message.remove(i)

function_key = lambda x: (x ** 6 + 3 * x ** 5 + x ** 4 + x ** 3 + 4 * x ** 2 + 4 ** x + 5) % 26


def encrypt_decrypt(mode, message, key, final=''):
    for index, symbol in enumerate(message):
        if mode == 'E':
            temp = ord(symbol) + key(index) - 13
        else:
            temp = ord(symbol) - key(index) - 13
        final += chr(temp % 26 + ord('A'))
    return final


print('Final message:', encrypt_decrypt(crypt_mode, start_message, function_key))
