a=input()
ar=list(a.split(","))
for i in ar:
    arr2=list(i.split(':'))
    name=arr2[0]
    n=arr2[1]
    m='0'
    for i in n:
        if ord(i)>ord(m):
            if ord(i)-48<=len(name):
                m=i
    ind=ord(m)-48
    name10=name*10
    if m=='0':
        print("X",end='')
    else:
        print(name10[ind-1],end='')