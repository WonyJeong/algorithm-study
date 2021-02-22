#배열 원소의 최댓값을 구해서 출력 ( 원소값을 난수로 발생)

import random
from b77 import max_of #b77.py의 max_of를 import

print('난수의 최댓값 구하기')

num = int(input("난수 개수 : "))
lo = int(input("난수의 최소 : "))
hi = int(input("난수의 최대 : "))

x = [None] * num

for i in range(num):
    x[i] = random.randint(lo,hi) #lo 이상 hi 이하인 정수 난수를 반환

print(f'{(x)}')
print(f'이 가운데 최대값은 {max_of(x)}이다')