d = dict(zip(('P','M','H'), ('Pikachu', 'Mickey Mouse', 'Hello kitty')))

qkey = input()
while qkey != str(-1):
    if qkey in d:
        print(d[qkey])
    elif qkey == '-2':
        print('keys:',sorted(d.keys()))
        ans = []
        for k in sorted(d.keys()):
            ans.append(d[k])        
        print('values:',ans)
    else:
        print(qkey,'does not exist. Enter a new one:')
        q = input()
        d[qkey] = q
    
        
    qkey = input()
