a,b,c=map(int,input().split())
l=list(map(int,input().split()))
s=l[-b:]+l[:-b]
for i in range(c):
    print(s[int(input())])