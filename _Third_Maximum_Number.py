class sol(object):
    def max(self,num):
        if num is None:
            return
        n=list(set(num))
        if len(n)<3:
            return max(n)
        else:
            return sorted(n)[-3]
n=int(input())
num=list(map(int,input().split()))
ob1=sol()
print(ob1.max(num))