from random import randint, choice

traps = ('"', '\\', '{', '}', '`', '№', ' ')

keys = {
    'A': '!', 'I': '(', 'Q': '<',
    'B': '@', 'J': ')', 'R': '>',
    'C': '#', 'K': '-', 'S': '/',
    'D': '$', 'L': '=', 'T': '[',
    'E': '%', 'M': '+', 'U': ']',
    'F': '^', 'N': '?', 'V': '{',
    'G': '&', 'O': ':', 'W': '}',
    'H': '*', 'P': ';', 'X': '|',
    'Y': '.', 'Z': ','
}

crypt_mode = input('[E]ncrypt | [D]ecrypt: ').upper()
if crypt_mode not in ['E', 'D']:
    print('Error: mode is not found!')
    raise SystemError

start_message = input('Write the message: ').upper()


def encrypt_decrypt(mode, message, final=''):
    message = list(message)

    if mode == 'E':
        length = len(message) // 4  # Сколько будет ложных символов, т.е. если символов 20 // 4 = 5
        for _ in range(length):
            message.insert(randint(0, len(message)), choice(traps))

        for symbol in message:
            if symbol in keys:
                final += keys[symbol]
            else:
                final += symbol
    else:
        for symbol in message:
            for key in keys:
                if symbol == keys[key]:
                    final += key

    return final

print('Final message:', encrypt_decrypt(crypt_mode, start_message))
