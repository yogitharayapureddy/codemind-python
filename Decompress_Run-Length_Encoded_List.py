class solution:
    def decompree(self,num):
        decompressed=[]
        for i in range(0,len(num)-1,2):
            decompressed=decompressed+num[i]*[num[i+1]]
        return decompressed
ob=solution()
n=int(input())
num=list(map(int,input().split()))
print(*(ob.decompree(num)))