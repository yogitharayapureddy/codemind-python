s=input()
a=[]
f=0
for i in s:
    if i in '([{':
        a.append(i)
    else:
        if len(a)>0:
            if a[-1]=='('and i==')':
                f=1
                r=a.pop()
            elif a[-1]=='{'and i=='}':
                f=1
                r=a.pop()
            elif a[-1]=='['and i==']':
                f=1
                r=a.pop()
            else:
                f=0
                break
        else:
            f=0
            break
if f==1:
    print("True")
else:
    print("False")