from random import randint

text = 'hello world'

keys = {
    'a': ['Q', '1', '!', '`', 'Я', 'М', 'Ь', 'З'],
    'b': ['W', '2'],
    'c': ['E', '3', '@'],
    'd': ['R', '4', '#', ':'],
    'e': ['T', '5', '$', ';', 'Ц', 'Е', 'Ш', 'Ж', ',', 'ф', 'ч', 'ш'],
    'f': ['Y', '6'],
    'g': ['U', '7'],
    'h': ['I', '8', '%', '"', 'Ы', 'П'],
    'i': ['O', '9', '^', '/', 'Ч', 'И'],
    'j': ['P'],
    'k': ['A'],
    'l': ['S', '0', '&', '?'],
    'm': ['D', '*'],
    'n': ['F', '(', '<', 'У', 'Н', 'Л'],
    'o': ['G', ')', '>', 'В', 'Р', 'Б', 'Х'],
    'p': ['H', '-'],
    'q': ['J'],
    'r': ['K', '_', '|', 'C', 'Т', 'Щ'],
    's': ['L', '+', '№', 'К', 'Г', 'Д'],
    't': ['M', '=', 'Й', 'А', 'О', 'Ю', 'Ъ', '.', 'й'],
    'u': ['N', '[', 'Ф'],
    'v': ['B'],
    'w': ['V', ']'],
    'x': ['C'],
    'y': ['X', '{'],
    'z': ['Z'],
    ' ': ['}'],
}

# Шифрование
crypt = ''
for i in text:
    if i in keys:
        length = len(keys[i])
        crypt += keys[i][randint(0, length - 1)]

print(crypt)

# Расшифрование

decrypt = ''
for i in crypt:
    for j in keys:
        if i in keys[j]:
            decrypt += j

print(decrypt)