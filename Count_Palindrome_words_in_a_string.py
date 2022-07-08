n=input().lower()
n=list(n.split(' '))
t=0
for i in n:
    if i==i[::-1]:
        t+=1
print(t)