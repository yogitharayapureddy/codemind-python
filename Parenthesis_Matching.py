s=input()
a=[]
f=1
for i in range(len(s)):
    if s[i] in '({[':
        a.append(s[i])
        f=1
    else:
        if len(a)>0:
            if a[-1]=='(' and s[i]==')':
                a.pop()
            elif a[-1]=='{' and s[i]=="}":
                a.pop()
            elif a[-1]=='[' and s[i]==']':
                a.pop()
            else:
                print(i+1)
                f=0
                break
        else:
            print(i+1)
            f=0
            break
if f==1:
    if len(a)==0:
        print(0)
    else:
        print(len(s)+1)