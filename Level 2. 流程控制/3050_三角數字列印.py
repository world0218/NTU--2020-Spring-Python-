n = int(input())
num = 1

for i in range(n):
    for f in range(i+1):
        print(num,end=' ')
        num += 1
    print()
