RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

def draw_flag(size):
    #для любого нечетного размера флага
    center = size//2
    length=size-2
    k=(size-center-1)
    for i in range(size):
        if i==center: print(f'{RED}{"   "*1}{WHITE}{"   "*length}{RED}{"   "*1}{END}')
        elif 0<i<center or center<i<(size-1): print(f'{RED}{"   "*k}{WHITE}{"   "}{RED}{"   "*k}{END}')
        else: print(f'{RED}{"   "*size}{END}')

if __name__=="__main__": 
    draw_flag(5)