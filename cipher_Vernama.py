from random import randint

text = 'HELLO WORLD'

crypt = ''
keys = ''

for c in text:
    key = randint(0, 25)
    keys += str(key) + ' '
    if ord(c) < 65 or ord(c) > 90:
        crypt += ' '
    else:
        g = ord(c) + key - 13
        crypt += chr((g % 26) + ord('A'))

print(crypt)
print(keys)

arr = []
key = ''
for k in keys:
    if k != ' ':
        key += k
    else:
        arr.append(key)
        key = ''
        continue

decrypt = ''

for k, c in enumerate(crypt):
    if ord(c) < 65 or ord(c) > 90:
        decrypt += ' '
    else:
        g = ord(c) - int(arr[k]) - 13
        decrypt += chr((g % 26) + ord('A'))

print(decrypt)
