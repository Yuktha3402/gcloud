from random import *
y = str(randint(1000,9999))
L=[]
for i in y:
    L.append(i)
x = input('enter a 4 digit number')
while x!=y:
    cows = 0
    bulls =0
    for i in range(4):
        if x[i]==y[i]:
            cows=cows+1
        if x[i]!=y[i] and x[i] in L:
            bulls=bulls+1
    print('no of cows:',cows,'no of bulls:',bulls,sep='\n')
    x = input('enter a 4 digit number')
print('game over','the random number generated is:',y,sep='\n')
    



    
