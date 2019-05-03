mode = input()
start_message = input()

rotors = (
    (18, 23, 24, 24, 19, 10, 8, 16, 7, 7, 11, 7, 14, 6, 8, 17, 20, 22, 19, 23, 26, 12, 24, 22, 19, 15),
    (2, 23, 14, 13, 17, 24, 13, 15, 19, 11, 24, 6, 21, 5, 10, 2, 18, 16, 21, 2, 18, 18, 21, 5, 5, 5),
    (4, 9, 15, 5, 23, 2, 20, 17, 5, 12, 21, 6, 9, 12, 24, 9, 1, 24, 5, 1, 26, 25, 15, 9, 7, 11)
)


# 18 + 2 + 4 = 24


def encrypt_decrypt(mode, message):
    x, y, z = 0, 0, 0
    final_message = ''
    for symbol in start_message:
        rotor = rotors[0][x] + rotors[1][y] + rotors[2][z]
        if mode == 'E':
            # 65 == 'A'
            # 65 - 13 = 52
            # 52 + 24 = 76
            # 76 % 26 = 24
            # 24 + 65 = 89
            # 89 == 'Y' - ASCII
            final_message += chr((ord(symbol.upper()) - 13 + rotor) % 26 + ord('A'))
        elif mode == 'D':
            final_message += chr((ord(symbol) - 13 - rotor) % 26 + ord('A'))
        else:
            print('Error: mode is not found!')
            raise SystemExit
        if x != 25:
            x += 1
        else:
            x = 0
            if y != 25:
                y += 1
            else:
                y = 0
                if z != 25:
                    z += 1
                else:
                    z = 0
    return final_message


print('Final message:', encrypt_decrypt(mode, start_message))
