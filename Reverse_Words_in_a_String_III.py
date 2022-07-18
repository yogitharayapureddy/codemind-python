def reverse(s):
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    return s1
a=input()
ar=list(a.split())
for i in ar:
    print(reverse(i),end=" ")