#10~99사이의 난수 n개 생성
import random

n = int(input('난수의 개수 입력받기'))

for _ in range(n):
    r= random.randint(10,99)
    print(r, end=' ')
    if r == 13 :
        print('\n프로그램 종료')
        break
else :
    print('\n난수 생성 종료')