class solution(object):
    def first(self,s):
        f={}
        for i in s:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        for i in range(len(s)):
            if f[s[i]]==1:
                return s[i]
        return -1
s=input('')
ab1=solution()
print(ab1.first(s))