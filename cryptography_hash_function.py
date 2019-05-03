from hashlib import sha256


def encrypt(string):
    signature = sha256(string.encode()).hexdigest()
    return signature


static_password = encrypt('secret')
dynamic_password = encrypt(input('Write the password: '))

if static_password == dynamic_password:
    print('Password is True')
else:
    print('Password is False')
