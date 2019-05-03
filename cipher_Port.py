from re import findall

ONE = 1

stage_one = ['00' + str(x) for x in range(ONE, 10)]
stage_two = ['0' + str(x) for x in range(10, 100)]
stage_three = [str(x) for x in range(100, 676 + ONE)]

keys = tuple(stage_one + stage_two + stage_three)

del stage_one, stage_two, stage_three, ONE

coordinate_x = tuple([chr(alpha) for alpha in range(65, 91)])
coordinate_y = tuple([chr(alpha) for alpha in range(65, 91)])

crypt_keys = {x: None for x in keys}

counter = 0
for x in coordinate_x:
    for y in coordinate_y:
        crypt_keys[keys[counter]] = x + y
        counter += 1

del coordinate_x, coordinate_y, counter, keys

crypt_mode = input('[E]ncrypt | [D]ecrypt: ').upper()
if crypt_mode not in ['E', 'D']:
    print('Error: mode is not (E/D)')
    raise SystemExit

start_message = input('Write the message: ').upper()


def regular(mode, text):
    if mode == 'E':
        template = r'[A-Z]{2}'
    else:
        template = r'[0-9]{3}'
    return findall(template, text)


def encrypt_decrypt(mode, message, final=''):
    if mode == 'E':
        for symbol in message:
            if symbol not in [chr(x) for x in range(65, 91)]:
                message = message.replace(symbol, '')
        if len(message) % 2 != 0:
            message += 'Z'
        for symbols in regular(mode, message):
            for key in crypt_keys:
                if symbols == crypt_keys[key]:
                    final += key + '.'
    else:
        for number in regular(mode, message):
            if number in crypt_keys:
                final += crypt_keys[number]
    return final


print('Final message:', encrypt_decrypt(crypt_mode, start_message))
