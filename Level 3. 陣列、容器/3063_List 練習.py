x = []


n = int(input())
while n != -1:
    x.append(n)
    n = int(input())

x.sort()
print(x)

x.insert(3,10)
print(x)
print(x.count(10))
x.sort()
x.reverse()
print(x)
