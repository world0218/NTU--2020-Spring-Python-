n = int(input())
 
for k in range(2,n+1):
    for i in range(2,k):
        if k%i==0:
            break
    else:
        print(k,"is prime")
