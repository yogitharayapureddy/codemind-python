n=int(input())
d=len(str(n))
sq=n**2
l=sq%pow(10,d)
if(l==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")