'''
H  E  L  L  O
72 69 76 76 79

K  H  O  O  R
75 72 79 79 82

HELLO = (1 3) => KHOOR [3 3 3 3 3]
'''

'''
H  E  L  L  O
72 69 76 76 79

Y  P  K  K  T
89 80 75 75 84

HELLO = (3 3) => YPKKT [17 11 -1 -1 5]
'''

# Делители 26: 1 3 5 7 9 11 15 17 19 21 23 25
# Правило для делителя: -x * x % 26 == 1

'''
H  E  L  L  O
72 69 76 76 79

M  X  G  G  V
77 88 71 71 86

HELLO = (5 3) => MXGGV [5 19 -5 -5 7]
'''

print('Possible key[a]: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25')
crypt_mode = input('[E]ncrypt | [D]ecrypt: ').upper()
if crypt_mode not in ['E', 'D']:
    print('Error: mode is not found')
    raise SystemExit
start_message = input('Write the message: ').upper()

try:
    main_key = input('Write the key: ').split()
except ValueError:
    print('Only int numbers!')
    raise SystemExit

if len(main_key) != 2:
    print('Error: qualitity keys must be 2')
    raise SystemExit


def encrypt_decrypt(mode, message, key, final=''):
    for symbol in message:
        if mode == 'E':
            final += chr((int(key[0]) * ord(symbol) + int(key[1]) - 13) % 26 + ord('A'))
        else:
            final += chr(pow(int(key[0]), 11) * ((ord(symbol) + 26 - int(key[1]) - 13)) % 26 + ord('A'))
    return final

print('Final message:', encrypt_decrypt(crypt_mode, start_message, main_key))
