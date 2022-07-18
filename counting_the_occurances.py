n=input().casefold()
a=input().casefold()
d=0
for i in range(len(n)):
    if n[i]==a:
        d+=1
if d==0:
    print("-1")
else:
    print(d)