n=input()
d=1
for i in range(1,len(n)-1):
    if n[i].isupper():
        d+=1
print(d)