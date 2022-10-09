class solution:
    def match(self,s):
        a=[i for i in range(len(s)+1)]
        return [a.pop((j=='I')-1) for j in s]+a
ob=solution()
print(*ob.match(input("")))