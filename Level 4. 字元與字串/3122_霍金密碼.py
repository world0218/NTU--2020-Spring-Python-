intab = "013457"
outtab = "OIEAST"
trantab = str.maketrans(intab,outtab)

s1 = input()
print(s1.translate(trantab))
