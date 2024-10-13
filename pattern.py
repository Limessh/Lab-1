WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK='\u001b[40m'

diametr=6
radius=diametr//2

def draw_pattern(k,n):
#узор будет выводиться k раз в длину
#узор будет выводиться n раз в высоту
    for i in range (n):
        print((f"{WHITE}{'   '*(radius-1)}{BLACK}{'   '*2}{WHITE}{'   '*(radius-1)}{WHITE}{'   '*(radius-1)}{BLACK}{'   '*2}{WHITE}{'   '*(radius-1)}{END}")*k)
        print((f"{WHITE}{'   '*(radius-2)}{BLACK}{'   '*1}{WHITE}{'   '*2}{BLACK}{'   '*1}{WHITE}{'   '*(radius-2)}{WHITE}{'   '*(radius-2)}{BLACK}{'   '*1}{WHITE}{'   '*2}{BLACK}{'   '*1}{WHITE}{'   '*(radius-2)}{END}")*k)
        print((f"{BLACK}{'   '*1}{WHITE}{'   '*4}{BLACK}{'   '*1}{BLACK}{'   '*1}{WHITE}{'   '*4}{BLACK}{'   '*1}{END}")*k)
        print((f"{BLACK}{'   '*1}{WHITE}{'   '*4}{BLACK}{'   '*1}{BLACK}{'   '*1}{WHITE}{'   '*4}{BLACK}{'   '*1}{END}")*k)
        print((f"{WHITE}{'   '*(radius-2)}{BLACK}{'   '*1}{WHITE}{'   '*2}{BLACK}{'   '*1}{WHITE}{'   '*(radius-2)}{WHITE}{'   '*(radius-2)}{BLACK}{'   '*1}{WHITE}{'   '*2}{BLACK}{'   '*1}{WHITE}{'   '*(radius-2)}{END}")*k)
        print((f"{WHITE}{'   '*(radius-1)}{BLACK}{'   '*2}{WHITE}{'   '*(radius-1)}{WHITE}{'   '*(radius-1)}{BLACK}{'   '*2}{WHITE}{'   '*(radius-1)}{END}")*k)

if __name__=="__main__":       
    draw_pattern(4,4)