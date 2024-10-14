RED = '\u001b[41m'
BLUE = '\u001b[44m'
END = '\u001b[0m'


file = open('sequence.txt', 'r')
lot=0
lot1=0

for number in file:
    lot+=1
    if -3<=float(number)<=3:
        lot1+=1
file.close()

procent=lot/100
print('Подходящие числа:' + '\t' + str(lot1/procent)+'\t'+f'{BLUE}{" "*(lot1//2)}{END}')
print('Оставшиеся числа:' + '\t' + str((lot-lot1)/procent)+'\t'+f'{RED}{" "*((lot-lot1)//2)}{END}')