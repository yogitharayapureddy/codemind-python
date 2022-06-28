n=input()
s=0
v=0
c=0
d=0
vo='aeiou'
for i in range(len(n)):
    if n[i]==' ':
        s+=1
    elif n[i] in vo:
        v+=1
    elif n[i].isdigit():
        d+=1
    else:
        c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",s)