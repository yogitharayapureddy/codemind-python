class solution(object):
    def maxprofit(self,price):
        ans=0
        for i in range(1,len(price)):
            if price[i]-price[i-1]>0:
                ans+=(price[i]-price[i-1])
        return ans
ob=solution()
n=int(input())
price=list(map(int,input().split()))
print(ob.maxprofit(price))