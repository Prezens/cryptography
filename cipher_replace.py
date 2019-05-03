# Encrypt

# message = 'hello world'
# keys = {
#     'a': '!', 'i': '(', 'q': '<',
#     'b': '@', 'j': ')', 'r': '>',
#     'c': '#', 'k': '-', 's': '/',
#     'd': '$', 'l': '=', 't': '[',
#     'e': '%', 'm': '+', 'u': ']',
#     'f': '^', 'n': '?', 'v': '{',
#     'g': '&', 'o': ':', 'w': '}',
#     'h': '*', 'p': ';', 'x': '|',
#     'y': '.', 'z': ',', ' ': '~'
# }

# crypt = ''
# for i in message:
#     if i in keys:
#         crypt += keys[i]

# print('Crypt text:\n'+crypt+'\n')


# Decrypt

message = '*%==:~}:>=$'
keys = {
    '!': 'a', '(': 'i', '<': 'q',
    '@': 'b', ')': 'j', '>': 'r',
    '#': 'c', '-': 'k', '/': 's',
    '$': 'd', '=': 'l', '[': 't',
    '%': 'e', '+': 'm', ']': 'u',
    '^': 'f', '?': 'n', '{': 'v',
    '&': 'g', ':': 'o', '}': 'w',
    '*': 'h', ';': 'p', '|': 'x',
    '.': 'y', ',': 'z', '~': ' '
}
decrypt = ''
for i in message:
    if i in keys:
        decrypt += keys[i]

print('Decrypted message:\n' + decrypt + '\n')
