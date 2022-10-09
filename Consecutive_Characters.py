def maxrep(str):
    l=len(str)
    count=0
    res=str[0]
    for i in range(l):
        ccount=1
        for j in range(i+1,l):
            if(str[i]!=str[j]):
                break
            ccount+=1
        if ccount>count:
            count=ccount
            res=str[i]
    return count
if __name__=="__main__":
    str=input("")
    print(maxrep(str))