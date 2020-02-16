sum = 0
ct = 0

n = int(input())

MaxVal = 0
MaxPos = 0

while n!=-1:
    sum += n
    ct += 1

    if n>MaxVal:
        MaxVal = n
        MaxPos = ct

    n = int(input())

else:
    print(sum)
    print(sum/ct)
    print(MaxVal)
    print(MaxPos)
