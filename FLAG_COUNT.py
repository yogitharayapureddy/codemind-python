a=int(input())
ar=[]
f1=f2=2
f=0
for i in range(a):
    ar.append(f1)
    f=f1+f2
    f1=f2
    f2=f
print(ar[a-1])