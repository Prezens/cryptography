# Квадрат Полибия:
#
#   +  1  2  3  4  5  6
#   1  a  b  c  d  e  f
#   2  g  h  i  j  k  l
#   3  m  n  o  p  q  r
#   4  s  t  u  v  w  x
#   5  y  z  0  1  2  3
#   6  4  5  6  7  8  9
#


text = 'helloworld'

keys = {
    'a': '11', 'i': '23', 'q': '35',
    'b': '12', 'j': '24', 'r': '36',
    'c': '13', 'k': '25', 's': '41',
    'd': '14', 'l': '26', 't': '42',
    'e': '15', 'm': '31', 'u': '43',
    'f': '16', 'n': '32', 'v': '44',
    'g': '21', 'o': '33', 'w': '45',
    'h': '22', 'p': '34', 'x': '46',
    'y': '51', 'z': '52', '0': '53',
    '1': '54', '2': '55', '3': '56',
    '4': '61', '5': '62', '6': '63',
    '7': '64', '8': '65', '9': '66'
}

# Encrypt

crypt = ''
for i in text:
    if i in keys:
        crypt += keys[i]
        crypt += ' '

print(crypt)

# Decrypt
temp = ''
decrypt = ''
for i in crypt:
    if i != ' ':
        temp += i
    else:
        for j in keys:
            if keys[j] == temp:
                decrypt += j
        temp = ''
print(decrypt)
