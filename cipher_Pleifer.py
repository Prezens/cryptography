# Шифр Плейфера
# Принцип работы данного метода шифрования:
# Есть исходное сообщение: HELL
# Если в сообщении есть символ 'J' - заменить его на символ 'I'
# Если в сообщении есть рядом стоящие одинаковые символы:
# Между ними поставить символ 'X':
# Получим сообщение: HELXL
# Далее раздедяем сообщение по 2 символа
# Получим сообщение: HE LX L
# Если сообщение нечетное - добавить в конец символ 'X'
# Получим сообщение: HE LX LX
# Далее создаем какой-либо ключ и заносим его в  матрицу алфавита
# (Используем ключ SOMETHING)
# МАТРИЦА:
#   ['S', 'O', 'M', 'E', 'T']
#   ['H', 'I', 'N', 'G', 'A']
#   ['B', 'C', 'D', 'F', 'K']
#   ['L', 'P', 'Q', 'R', 'U']
#   ['V', 'W', 'X', 'Y', 'Z']
# Если в матрице появляются одинаковые символы:
# Удалять одинаковые символы с конца матрицы
# Далее идет два способа шифрования:
# 1) Если пара символов находится на одной строке матрицы:
#  Передвинуть индекс значений на +1
# 2) Если пара символов находятся на разных строках матрицы:
#  Если находятся на разных строках, значит может получится прямоугольник
#  Создать соответственно этот прямоугольник
#  И поменять значения символов на противоположные ушлы пряугольника
# В итоге получаем следующее сообщение: SG VQ VQ
# Складываем все символы в одну строчку и получаем зашифрованное сообщение:
# SGVQVQ

text = 'HELLO'

text = [x for x in text]
for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        text.insert(i, 'X')

if len(text) % 2 != 0:
    text.append('X')

for i in range(len(text)):
    if text[i] == 'J':
        text[i] = 'I'

matrix = [
    ['S', 'O', 'M', 'E', 'T'],
    ['H', 'I', 'N', 'G', 'A'],
    ['B', 'C', 'D', 'F', 'K'],
    ['L', 'P', 'Q', 'R', 'U'],
    ['V', 'W', 'X', 'Y', 'Z']
]

binary = []
k = ''
for i in text:
    k += i
    if len(k) == 2:
        binary.append(k)
        k = ''

# Encrypt
encrypt = ''
switch = 0
for i in range(len(binary)):
    for k in range(2):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == binary[i][k]:
                    if binary[i][0] in matrix[x] and binary[i][1] in matrix[x]:
                        if matrix[x][y] != matrix[x][-1]:
                            encrypt += matrix[x][y + 1]
                        else:
                            encrypt += matrix[x][y - 4]
                    else:
                        for a in range(len(matrix)):
                            for b in range(len(matrix[a])):
                                if matrix[a][b] == binary[i][0]:
                                    x0 = a
                                if matrix[a][b] == binary[i][1]:
                                    x1 = a
                        if switch == 0:
                            encrypt += matrix[x1][y]
                            switch = 1
                        else:
                            encrypt += matrix[x0][y]
                            switch = 0

print('Encrypted message:', encrypt)

binary = []
k = ''
for i in encrypt:
    k += i
    if len(k) == 2:
        binary.append(k)
        k = ''

# Decrypt
decrypt = []
switch = 0
for i in range(len(binary)):
    for k in range(2):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == binary[i][k]:
                    if binary[i][0] in matrix[x] and binary[i][1] in matrix[x]:
                        if matrix[x][y] != matrix[x][0]:
                            decrypt.append(matrix[x][y - 1])
                        else:
                            decrypt.append(matrix[x][y + 4])
                    else:
                        for a in range(len(matrix)):
                            for b in range(len(matrix[a])):
                                if matrix[a][b] == binary[i][0]:
                                    x0 = a
                                if matrix[a][b] == binary[i][1]:
                                    x1 = a
                        if switch == 0:
                            decrypt += matrix[x1][y]
                            switch = 1
                        else:
                            decrypt += matrix[x0][y]
                            switch = 0

for i in range(len(decrypt) - 1):
    if decrypt[i] == 'X':
        if decrypt[i] != decrypt[-1]:
            if decrypt[i - 1] == decrypt[i + 1]:
                decrypt.remove(decrypt[i])
        else:
            decrypt.remove(decrypt[i])

print('Decrypted message:', ''.join(decrypt))
