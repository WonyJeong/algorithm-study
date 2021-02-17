#1부터 n까지 정수의 합
#for

print("1~n합")
n =int(input("n : "))

sum = 0
for i in range(1, n+1):
    sum += i #sum에 i를 더함


print(f'1부터 {n}까지 정수의 합은 {sum}입니다')