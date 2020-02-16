x = []
n = int(input())

for i in range(n,0,-1):
    print("data",i)
    x.append("data "+str(i))

print()
for j in range(n):
    print(x.pop())
    
