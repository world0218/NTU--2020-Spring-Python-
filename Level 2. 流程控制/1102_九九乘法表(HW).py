n1 = int(input())
n2 = int(input())

for i in range(1,n1+1):
    for f in range(1,n2+1):
        print('%d*%d=%2d'%(i,f,i*f),end=' ')
    print()
    
