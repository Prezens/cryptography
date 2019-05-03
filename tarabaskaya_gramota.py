# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#
# Open message: HELLO WORLD
#
# Encrypted:
#  Split equals two groups 'soglasnye' symbols in alphabet:
#   One group symbols in begin alphabet
#   Two group symbols in end alphabet
#
#   B C D F G H J K L M
#   | | | | | | | | | |
#   Z X W V T S R Q P N
#
#  'Glasnye' symbols stay not changed
#
# Encrypted message: SEPPO DOJPW
#

message = list(input('Write the text: ').upper())
keys = {
    'B': 'Z', 'C': 'X', 'D': 'W', 'F': 'V', 'G': 'T',
    'H': 'S', 'J': 'R', 'K': 'Q', 'L': 'P', 'M': 'N'
}

for symbol in range(len(message)):
    for key in keys:
        if message[symbol] == key:
            message[symbol] = keys[key]
        elif message[symbol] == keys[key]:
            message[symbol] = key
        else:
            pass

print('Final message:', ''.join(message))
