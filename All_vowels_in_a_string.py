s=input()
v=[s.count('a'),s.count('e'),s.count('i'),s.count('o'),s.count('u')]
n=vowel=[s.count('A'),s.count('E'),s.count('I'),s.count('O'),s.count('U')]
if v.count(0)==0:
    print("True")
elif n.count(0)==0:
    print("True")
else:
    print("False")