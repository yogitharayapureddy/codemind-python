class solution(object):
    def uniq(self,s):
        f={}
        for i in s:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        for i in range(len(s)):
            if f[s[i]]==1:
                return i
        return -1
s=input("")
ob1=solution()
print(ob1.uniq(s))