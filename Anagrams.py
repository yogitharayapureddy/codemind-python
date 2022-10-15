str1=input("")
str2=input("")
str1=str1.lower()
str2=str2.lower()
if(len(str1)==len(str2)):
    sortedstr1=sorted(str1)
    sortedstr2=sorted(str2)
    if(sortedstr1==sortedstr2):
        print("True")
    else:
        print("False")
else:
    print("False")
    