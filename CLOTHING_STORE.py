from collections import Counter
def sockmerchant(n,arr):
    n=Counter(arr)
    return sum(i//2 for i in n.values())
n=input()
arr=list(map(int,input().split()))
print(sockmerchant(n,arr))