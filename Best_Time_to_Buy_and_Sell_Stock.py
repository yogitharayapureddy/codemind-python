class solution(object):
    def maxprofit(self,price):
        if len(price)==0:
            return 0
        else:
            max_profit=0
            min_price=price[0]
            for i in range(len(price)):
                profit=price[i]-min_price
                max_profit=max(profit,max_profit)
                min_price=min(min_price,price[i])
            return max_profit
ob=solution()
n=int(input())
price=list(map(int,input().split()))
print(ob.maxprofit(price))