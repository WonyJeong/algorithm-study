#1000 이하의 소수 나열

counter = 0

for n in range(2, 1001):
    for i in range(2,n):
        counter += 1
        if n % i == 0 : #나누어 떨어지면 소수가 아님
            break # 반복 중단
    else : # 나누어 떨어지지 않는다면 소수
        print(n)
print(f'나눗셈을 실행한 횟수 : {counter}')