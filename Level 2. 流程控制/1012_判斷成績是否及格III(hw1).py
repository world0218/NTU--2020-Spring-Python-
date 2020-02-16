x = int(input())
 
if x!=1 and x!=2:
    print('roll error')
else:
    y = int(input())
 
    if y>100 or y<0:
        print('score error')
    else:
        if x==1 and y>=60 or x==2 and y>=70:
            print('pass')
        else:
            print('fail')
