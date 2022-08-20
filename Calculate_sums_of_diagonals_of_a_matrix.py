a=int(input())
p=s=0
for i in range(a):
    arr=list(map(int,input().split()))
    for j in range(a):
        if i==j:
            p+=arr[j]
        if i+j==a-1:
            s+=arr[j]
print("Principal Diagonal:",end="")
print(p)
print("Secondary Diagonal:",end="")
print(s)