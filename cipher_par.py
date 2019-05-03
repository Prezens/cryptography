text = 'HELLO'
encrypt = 'GFKKP'

keys = {
    'A': 'B', 'C': 'D', 'E': 'F',
    'G': 'H', 'I': 'J', 'K': 'L',
    'M': 'N', 'O': 'P', 'Q': 'R',
    'S': 'T', 'U': 'V', 'W': 'X',
    'Y': 'Z'
}


def encrypt_decrypt(message, couple):
    text = ''
    for symbol in message:
        for key in couple:
            if symbol == key:
                text += couple[key]
            elif symbol == couple[key]:
                text += key
            else:
                pass
    return text

print(encrypt_decrypt(text, keys))
print(encrypt_decrypt(encrypt, keys))
