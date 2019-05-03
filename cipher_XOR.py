text = str(input('Write the crypt message:\n> '))
key = int(input('Write the key:\n> '))

# Encrypt
crypt = ''
for i in text:
    try:
        crypt += chr(ord(i) ^ ord(key))
    except TypeError:
        crypt += chr(ord(i) ^ key)

print(crypt)

# Decrypt
decrypt = ''
for j in crypt:
    try:
        decrypt += chr(ord(j) ^ ord(key))
    except TypeError:
        decrypt += chr(ord(j) ^ key)

print(decrypt)
