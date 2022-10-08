n=int(input())
a=input().split()
b=input().split()
c=[]
for i in range(n):
    c.append(int(a[i])+int(b[i]))
print(" ".join([str(i) for i in c]))