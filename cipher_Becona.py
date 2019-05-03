text = 'hello world'
keys = {
    'a': 'AAAAA', 'i': 'ABAAA', 'q': 'BAAAA',
    'b': 'AAAAB', 'j': 'ABAAB', 'r': 'BAAAB',
    'c': 'AAABA', 'k': 'ABABA', 's': 'BAABA',
    'd': 'AAABB', 'l': 'ABABB', 't': 'BAABB',
    'e': 'AABAA', 'm': 'ABBAA', 'u': 'BABAA',
    'f': 'AABAB', 'n': 'ABBAB', 'v': 'BABAB',
    'g': 'AABBA', 'o': 'ABBBA', 'w': 'BABBA',
    'h': 'AABBB', 'p': 'ABBBB', 'x': 'BABBB',
    'y': 'BBAAA', 'z': 'BBAAB', ' ': 'BBABA'
}

encrypt = ''
for i in text:
    for j in keys:
        if i == j:
            encrypt += keys[i]

print(encrypt)

decrypt = ''
k = ''
for i in encrypt:
    k += i
    if len(k) == 5:
        for j in keys:
            if k == keys[j]:
                decrypt += j
                k = ''    

print(decrypt)
