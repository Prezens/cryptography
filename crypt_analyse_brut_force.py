arr1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']


def change_arr2():
    for i in range(number):
        arr2.append(arr2[0])
        arr2.remove(arr2[0])


msg = input('Write the crypted text: ')
print('All possible variants of decoding: ')
for number in range(len(arr1)):
    arr2 = list(map(lambda x: x, arr1))
    change_arr2()
    msgd = ''
    for i in msg:
        if i == ' ':
            msgd += ' '
        else:
            for j in range(len(arr1)):
                if i == arr2[j]:
                    msgd += arr1[j]
    print('[Possible variant] ' + str(msgd) + ' -> ' + str(number))
