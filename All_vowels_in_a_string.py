string=input()
v= [string.count('a'), string.count('e'), string.count(
        'i'), string.count('o'), string.count('u')]
n=vowel = [string.count('A'), string.count('E'), string.count(
        'I'), string.count('O'), string.count('U')]
if v.count(0)==0:
    print("True")
elif n.count(0)==0:
    print("True")
else:
    print("False")