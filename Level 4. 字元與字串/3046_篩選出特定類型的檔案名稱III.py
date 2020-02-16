st = []
n = input()

while n != '-1':
    st.append(n)
    n = input()

t = ['T00_'+k.capitalize() for k in st if k.endswith('.txt')]
print(t)

p = ['P00_'+f.rpartition('.')[0].upper()+'.py' for f in st if f.endswith('.py')]
print(p)
