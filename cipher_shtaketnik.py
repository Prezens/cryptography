# Cipher Shtaketnik
#               0123456789
# Open message: HELLOWORLD
# Encrypting:
#  H L O O L - Четные
#   E L W R D - Нечетные
# Encrypting message: HLOOLELWRD
# Decrypting
#  HLOOL - ELWRD
# ------------------------------
# H . L . O . O . L .
# . E . L . W . R . D
# ------------------------------
# H E L L O W O R L D
# Encrypted message: HELLOWORLD

crypt_mode = input('[E]ncrypt | [D]ecrypt: ').upper()
if crypt_mode not in ['E', 'D']:
    print('Error: mode is not Found!')
    raise SystemExit
start_message = input('Write the message: ')


def encrypt_decrypt(mode, message, final = ''):
    if mode == 'E':
        encrypt_list = [
            [message[x] for x in range(len(message)) if x % 2 == 0],
            [message[x] for x in range(len(message)) if x % 2 != 0]
        ]

        for index in range(len(encrypt_list)):
            final += ''.join(encrypt_list[index])
    else:
        if len(message) % 2 != 0:
            message += ' '
        length, half = len(message), len(message) // 2
        decrypt_list = [
            [message[x] for x in range(half)],
            [message[x] for x in range(half, length)]
        ]

        for index in range(half):
            final += decrypt_list[0][index] + decrypt_list[1][index]
    return final
print('Final message:', encrypt_decrypt(crypt_mode, start_message))
