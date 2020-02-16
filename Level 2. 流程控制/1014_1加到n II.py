sum = 0
n = int(input())

for i in range(1,n+1):
    sum += i
    print(i,end='')
    if i < n:
        print("+",end='')
else:
    print(" =",sum)
