arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

string = input()
for i in range(len(string)):
    index = (arr.index(string[i]))
    formula = 21 * (index - 8) % 26
    # print(formula)
    print(arr[formula])
