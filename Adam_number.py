def rev(n):
    r=0
    while(n>0):
        r=r*10+n%10
        n//=10
    return r
def sq(n):
    return(n*n)
def adamno(n):
    a=sq(n)
    b=sq(rev(n))
    if(a==rev(b)):
        return True
    else:
        return False
n=int(input())
if (adamno(n)):
    print("True")
else:
    print("False")