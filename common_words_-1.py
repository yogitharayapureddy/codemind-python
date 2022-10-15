class solution:
    def solve(self,s0,s1):
        s0=s0.lower()
        s1=s1.lower()
        s0list=s0.split(" ")
        s1list=s1.split(" ")
        return len(list(set(s0list)&set(s1list)))
ob=solution()
s=input()
t=input()
print(ob.solve(s,t))