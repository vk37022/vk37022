a=[]
b=0
c=1
e=0
for i in range(int(input())):
    e=b
    b=e+c
    c=e
    a.append(c)
print(a)
