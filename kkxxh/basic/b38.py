#a~b 정수의 합 구하기 with 정렬
#for문, if문

print('a부터 b까지 정수의 합 구하기')
a = int(input('a : '))
b = int(input('b : '))

if a>b :
    a,b = b,a #a,b 오름차순으로 정렬(순서 바꾸기)

sum = 0
for i in range(a,b):
    print(f'{i} + ', end='')
    sum += i # sum에 i를 더함

print(f'{b} = ', end='')
sum += b

print(sum)