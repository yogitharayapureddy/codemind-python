n=int(input())
while(n):
    n-=1
    a=input()
    a.casefold()
    if(a[::-1]==a and len(a)%2==0):
        print("YES EVEN")
    elif(a[::-1]==a and len(a)&2!=0):
        print("YES ODD")
    elif(a[::-1]!=a):
        print("NO")
    else:
        print("YES ODD")