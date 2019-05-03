from random import choice

print('1) Encrypted message')
print('2) Decrypted message')

answer = input('Write the number: ')
if answer == '1':
    file_name = input('Book-key name: ')  # Для работы ключа, необходим какой-то текст
    text = input('Write the text: ')
    encrypt = []
    k = 0
    with open(file_name, 'r') as file:
        read = file.read()
        for g in read:
            temp = []
            for i, j in enumerate(read):
                if text[k] == j:
                    temp.append(i)
            try:
                encrypt.append(choice(temp) + 1)
            except:
                pass
            finally:
                if k < len(text) - 1:
                    k += 1
                else:
                    break
    print('Encrypted message: ')
    for i in encrypt:
        print(i, end='/')
    print()
elif answer == '2':
    file_name = input('Book-key name: ')
    keys = input('Encrypted text: ')
    keys = [i for i in keys]
    encrypt = []
    k = ''
    for i in keys:
        if i != '/':
            k += i
        else:
            encrypt.append(int(k) - 1)
            k = ''
            continue
    decrypt = ''
    k = 0
    with open(file_name, 'r') as file:
        read = file.read()
        for g in read:
            for i, j in enumerate(read):
                try:
                    if i == encrypt[k]:
                        if k <= len(encrypt) - 1:
                            k += 1
                            decrypt += j
                except:
                    break
    print('Decrypted message:\n' + decrypt)
else:
    print('Number is not found.')
