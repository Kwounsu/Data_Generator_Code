from random import randint as r

print(1,0)
N=r(2,10)
print(N)
for i in range(2,N+1):
    print(r(1,i-1),end=' ')
print()
for i in range(1,N+1):
    l=r(0,5)
    print(l,r(l,10))

'''
test only when B=0.
'''
