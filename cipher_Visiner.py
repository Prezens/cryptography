# arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print('')
#
#
# def switch(n):
#     while n < 26:
#         for e in arr:
#             if e == arr[0]:
#                 print(end='|')
#             print(e, end='|')
#         arr.append(arr[0])
#         arr.remove(arr[0])
#         print('')
#         n += 1
# switch(0)
# print('')

# В ключевом слове, которое используется для зашифровки, берем символом(идем последовательно через каждый символ), находим его в первой строке, далее в первом столбце находим соответсвующий символ, их пересечение и будет зашифрованный символ

# Encrypt
m = 'HELLO'  # Слово, которое необходимо зашифровать
k = 'WORLD'  # Ключевое слово
k *= len(m) // len(k) + 1
c = ''
for i, j in enumerate(m):
    g = (ord(j) + ord(k[i]))
    c += chr(g % 26 + 65)

print('Encrypted message: ' + str(c))

# Decrypt
# c = 'DSCWR'
# k = 'WORLD'
# d = ''
# for i, j in enumerate(c):
#     g = (ord(j) - ord(k[i]))
#     d += chr(g % 26 + 65)
#
# print('Decrypt message: ' + str(d))
