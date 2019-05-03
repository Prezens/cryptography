from re import findall

list_word = ['AND', 'THE', 'OR', 'ALL', 'ANY', 'WHAT', 'WHY', 'YES', 'NO', 'ONE', 'YOU', 'HE', 'SHE', 'USE', 'IF', 'ELSE', 'THIS', 'YOUR', 'ON', 'HOW', 'ARE', 'ME', 'IT', 'IS', 'THAT', 'WAS', 'OF', 'BE', 'OK', 'NOT']
list_code = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '/', '?', '<', '>', ';', ':', '{', '}', '[', ']', '~', ',', '.', '"', '|', '\\', '`']

keys = dict(zip(list_word, list_code))

crypt_mode = input('[E]ncrypt | [D]ecrypt: ').upper()
if crypt_mode not in ['E', 'D']:
    print('Error: mode is not found')
    raise SystemExit

start_message = input('Write the message: ').upper()
template = r"\w+"


def encrypt_decrypt(mode, message):
    if mode == 'E':
        for symbol in message:
            if symbol not in [chr(x) for x in range(65, 91)]:
                message = message.replace(symbol, ' ')
        for word in findall(template, message):
            for key in keys:
                if word == key:
                    message = message.replace(key, keys[key])
    else:
        for key in keys:
            if keys[key] in message:
                message = message.replace(keys[key], key)

    return message


print('Final message: ', encrypt_decrypt(crypt_mode, start_message))
