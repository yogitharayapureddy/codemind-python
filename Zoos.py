n=input()
a=0
b=0
for i in range(len(n)):
    if n[i]=='z':
        a+=1
    else:
        b+=1
if a==(b/2):
    print("Yes")
else:
    print("No")