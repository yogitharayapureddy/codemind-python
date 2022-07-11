a=int(input())
v=0
for i in range(a):
    t=input()
    if t=='++X':
        v+=1
    if t=='X++':
        v+=1
    if t=='--X':
        v-=1
    if t=='X--':
        v-=1
print(v)