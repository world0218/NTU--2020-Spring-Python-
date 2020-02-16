d = dict(zip(('P','M','H'), ('Pikachu', 'Mickey Mouse', 'Hello kitty')))

qkey = input()
if qkey in d:
    print(d[qkey])
