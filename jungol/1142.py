from random import randrange as r

### 소수점 두자리 안나오는 케이스 저격
# N = 2
# print(N)
# for i in range(N):
#     x,y,w,h = r(10,21), r(10,21), r(1,10), r(1,10)
#     print('%.1f %.1f %.1f %.1f'%(x/10,y/10,w/10,h/10))


### 그냥 일반 큰 데이터
N = 2
print(N)
for i in range(N):
    x,y,w,h = r(9000,10001), r(9000,10001), r(5000,9000), r(5000,9000)
    print('%.1f %.1f %.1f %.1f'%(x/10,y/10,w/10,h/10))
