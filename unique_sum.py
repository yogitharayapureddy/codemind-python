n=int(input()) 
a = list(map(int,input().split())) 
temp = []
sum=0
for element in a: 
    if(element not in temp):  
        temp.append(element)
        if element in temp:
            sum+=element
            continue
print(sum)