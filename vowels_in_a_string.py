s=input()
v=input()
for i in range(0,len(s)):
    if(s[i]==v):
        print("True")
        print(i)
        break
else:
    print("False")