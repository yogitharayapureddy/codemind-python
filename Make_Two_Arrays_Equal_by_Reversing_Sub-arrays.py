class solution:
    def equal(self,target,a):
        for i in a:
            if i in target:
                target.remove(i)
        if len(target)>0:
            return False
        else:
            return True
n=int(input())
target=list(map(int,input().split()))
n1=int(input())
a=list(map(int,input().split()))
ob1=solution()
print(ob1.equal(target,a))