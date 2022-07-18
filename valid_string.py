from statistics import *
s=input()
arr=[]
c=0
for i in s:
    arr.append(s.count(i))
m=mode(arr)
for i in s:
    if s.count(i)!=m:
        if c<1:
            c+=1
        else:
            print("Not Valid")
            break
else:
    print("Valid String")