a=int(input())
f1=0
f2=1
f=f1+f2
for i in range(a):
    print(f1,end=" ")
    f=f1+f2
    f1=f2
    f2=f