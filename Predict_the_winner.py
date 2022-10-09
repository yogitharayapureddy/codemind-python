def winner(a,n):
    c0=0
    c1=0
    c2=0
    c3=0
    for i in range(n):
        if(a[i]%4==0):
            c0+=1
        elif(a[i]%4==1):
            c1+=1
        elif(a[i]%4==2):
            c2+=1
        elif(a[i]%4==3):
            c3+=1
    if(c0%2==0 and c1%2==0 and c2%2==0 and c3==0):
        return 1
    else:
        return 2
n=int(input())
a=list(map(int,input().split()))
if(winner(a,n)==1):
    print("X")
else:
    print("Y")