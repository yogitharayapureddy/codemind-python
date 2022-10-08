n,m=map(int,input().split())
test=[list(map(int,input().split())) for i in range(n)]
res=list(map(max,zip(*test)))
for i in res:
    print(i)