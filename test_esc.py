RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
# print(f"{WHITE}{'*'*10}{END}")
# print(f"{BLUE}{'*'*10}{END}")
# print(f"{RED}{'*'*10}{END}")
for i in range(6):
    if i < 3:
        print(f'{BLUE}{"  " * (2 * i + 2)}{WHITE}{"  " * (14 - 2 * i)}{END}')
    else:
        print(f'{BLUE}{"  " * (12 - 2 * i)}{RED}{"  " * (4 + 2 * i)}{END}')

# file = open('sequence.txt', 'r')
# list = []
# for number in file:
#     list.append(float(number))
# file.close()
# print(list)