n=int(input())
a=[]
for i in range(0,n):
    m=int(input())
    a.append(m)
for i in range(0,n):
    c=0
    for j in range(0,a[i]):
        if j*j==a[i]:
            c+=1
    if c>0:
        print("True")
    else:
        print("False")