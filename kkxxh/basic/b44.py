#1~n정수의 합

print('1부터 n까지 정수의 합')

while True :
    n= int(input('n : '))
    if n > 0 :
        break # n 이 0보다 커질 때까지 반복

sum = 0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}')