a=int(input())
arr=list(map(int,input().split()))
arr.sort()
if a%2!=0:
    for i in range(a-1,1,-2):
        if i==2:
            print(arr[i-1],end=" ")
            print(arr[i],end=" ")
        else:
            print(arr[i-1],end=" ")
            print(arr[i],end=" ")
    print(arr[0])
else:
    for i in range(a-1,0,-2):
        print(arr[i-1],end=" ")
        print(arr[i],end=" ")