#y=x/3
x=[0]*11
y=[0]*11
x1=0
y1=0

for i in range (len(x)):
    x[i]=y1*3
    y1+=1

for j in range (len(y)):
    y[j]=(x1//3)
    x1+=3

y=y[::-1]
s=''+'\t'

for i in range (len(y)):
    s+=str(y[i])+'\t'
    for j in range (len(x)):

        if i==(len(x)-1)-j:
            s+='*'+'\t'
        else:
            s+='-'+'\t'

    s+='\n'+'\t'

for i in range (len(x)):
    s+='\t'+str(x[i])


print(s)        
