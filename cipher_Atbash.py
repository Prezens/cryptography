arr1 = [chr(x) for x in range(65, 91)]
arr2 = [x for x in arr1]
arr2.reverse()

text = 'HELLO'

encrypt = ''
for i in text:
    for j, k in enumerate(arr1):
        if i == k:
            encrypt += arr2[j]

print(encrypt)

decrypt = ''
for i in encrypt:
    for j, k in enumerate(arr2):
        if i == k:
            decrypt += arr1[j]

print(decrypt)
