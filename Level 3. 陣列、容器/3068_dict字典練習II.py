d = dict(zip(('P','M','H'), ('Pikachu', 'Mickey Mouse', 'Hello kitty')))

qkey = input()
while qkey != str(-1):
    if qkey in d:
        print(d[qkey])
    else:
        print(qkey,'does not exist. Enter a new one:')
        q = input()
        d[qkey] = q

        
    qkey = input()
