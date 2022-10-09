class solution(object):
    def string(self,s):
        r,count=0,0
        for c in s:
            count+=1 if c=='L'else-1
            if count==0:
                r+=1
        return r
s=input()
ob1=solution()
print(ob1.string(s))
            