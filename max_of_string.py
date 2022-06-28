n=input()
m='0'
for i in range(len(n)):
    if ord(n[i])>ord(m):
        m=n[i]
print(m)