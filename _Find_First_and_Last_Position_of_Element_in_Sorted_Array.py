class solution(object):
    def searchrange(self,num,target):
        res=[-1,-1]
        low=0
        high=len(num)
        while low<high:
            mid=int(low+(high-low)//2)
            if num[mid]==target:
                high=mid
                res[0]=mid
                res[1]=mid
            elif num[mid]<target:
                low=mid+1
            else:
                high=mid
        if res[0]==-1:
            return res
        low=res[0]+1
        high=len(num)
        while low<high:
            mid=int(low+(high-low)//2)
            if num[mid]==target:
                low=mid+1
                res[1]=mid
            elif num[mid]<target:
                low=mid+1
            else:
                high=mid
        return res
n=int(input())
num=list(map(int,input().split()))
target=int(input())
ob1=solution()
a=ob1.searchrange(num,target)
print(*a)
                