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

y=[x*x*x for x in a]
print("squring of fibonacci series = ")
for i in y:
    print(i,end=' ')
    
    
